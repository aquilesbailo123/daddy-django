import os
import uuid
from typing import Optional
from django.conf import settings
from google.cloud import storage
from google.oauth2 import service_account
import logging

logger = logging.getLogger(__name__)


class GCSUploader:
    """Google Cloud Storage file uploader utility"""
    
    def __init__(self):
        self.bucket_name = settings.GCS_BUCKET_NAME
        self.credentials_path = settings.GCS_CREDENTIALS_PATH
        self.project_id = settings.GCS_PROJECT_ID
        self._client = None
        self._bucket = None
    
    @property
    def client(self):
        """Lazy initialization of GCS client"""
        if self._client is None:
            if self.credentials_path and os.path.exists(self.credentials_path):
                credentials = service_account.Credentials.from_service_account_file(
                    self.credentials_path
                )
                self._client = storage.Client(
                    credentials=credentials,
                    project=self.project_id
                )
            else:
                # Use default credentials (for production environments)
                self._client = storage.Client(project=self.project_id)
        return self._client
    
    @property
    def bucket(self):
        """Lazy initialization of GCS bucket"""
        if self._bucket is None:
            self._bucket = self.client.bucket(self.bucket_name)
        return self._bucket
    
    def upload_file(self, file, folder: str = "uploads", filename: Optional[str] = None) -> str:
        """
        Upload a file to Google Cloud Storage
        
        Args:
            file: Django UploadedFile object
            folder: Folder path in the bucket (default: "uploads")
            filename: Custom filename (optional, will generate UUID if not provided)
            
        Returns:
            str: Public URL of the uploaded file
            
        Raises:
            Exception: If upload fails
        """
        try:
            # Generate filename if not provided
            if not filename:
                file_extension = os.path.splitext(file.name)[1]
                filename = f"{uuid.uuid4()}{file_extension}"
            
            # Create blob path
            blob_name = f"{folder}/{filename}"
            blob = self.bucket.blob(blob_name)
            
            # Set content type based on file
            content_type = file.content_type or 'application/octet-stream'
            blob.content_type = content_type
            
            # Upload file
            file.seek(0)  # Reset file pointer
            blob.upload_from_file(file, content_type=content_type)
            
            # Make blob publicly readable
            blob.make_public()
            
            logger.info(f"Successfully uploaded file to GCS: {blob_name}")
            return blob.public_url
            
        except Exception as e:
            logger.error(f"Failed to upload file to GCS: {str(e)}")
            raise Exception(f"File upload failed: {str(e)}")
    
    def delete_file(self, file_url: str) -> bool:
        """
        Delete a file from Google Cloud Storage using its public URL
        
        Args:
            file_url: Public URL of the file to delete
            
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        try:
            # Extract blob name from URL
            # URL format: https://storage.googleapis.com/bucket-name/path/to/file
            if f"storage.googleapis.com/{self.bucket_name}/" in file_url:
                blob_name = file_url.split(f"storage.googleapis.com/{self.bucket_name}/")[1]
                blob = self.bucket.blob(blob_name)
                blob.delete()
                logger.info(f"Successfully deleted file from GCS: {blob_name}")
                return True
            else:
                logger.warning(f"Invalid GCS URL format: {file_url}")
                return False
                
        except Exception as e:
            logger.error(f"Failed to delete file from GCS: {str(e)}")
            return False


# Global instance
gcs_uploader = GCSUploader()


def upload_project_file(file, file_type: str, project_id: Optional[str] = None) -> str:
    """
    Upload a project-related file to GCS
    
    Args:
        file: Django UploadedFile object
        file_type: Type of file (logo, document, etc.)
        project_id: Optional project ID for organizing files
        
    Returns:
        str: Public URL of the uploaded file
    """
    folder = f"projects/{project_id or 'temp'}/{file_type}" if project_id else f"projects/temp/{file_type}"
    return gcs_uploader.upload_file(file, folder=folder)


def upload_member_photo(file, project_id: Optional[str] = None, member_name: Optional[str] = None) -> str:
    """
    Upload a project member photo to GCS with validation
    
    Args:
        file: Django UploadedFile object
        project_id: Optional project ID for organizing files
        member_name: Optional member name for file organization
        
    Returns:
        str: Public URL of the uploaded file
        
    Raises:
        Exception: If file validation fails
    """
    # Validate file type
    allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp']
    if file.content_type not in allowed_types:
        raise Exception(f"Invalid file type. Allowed types: {', '.join(allowed_types)}")
    
    # Validate file size (max 5MB)
    max_size = 5 * 1024 * 1024  # 5MB in bytes
    if file.size > max_size:
        raise Exception(f"File too large. Maximum size: 5MB, got: {file.size / (1024*1024):.1f}MB")
    
    # Create folder structure
    folder = f"projects/{project_id or 'temp'}/members"
    
    # Generate filename with member name if provided
    if member_name:
        # Sanitize member name for filename
        safe_name = "".join(c for c in member_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_name = safe_name.replace(' ', '_').lower()
        file_extension = os.path.splitext(file.name)[1]
        filename = f"{safe_name}_{uuid.uuid4().hex[:8]}{file_extension}"
    else:
        filename = None
    
    return gcs_uploader.upload_file(file, folder=folder, filename=filename)
