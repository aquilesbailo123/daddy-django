# Authentication Endpoints

This document provides detailed information about the authentication endpoints available in the Daddy Django project.

<div align="center">
  <img src="static/images/chadicon.svg" alt="Daddy Django Logo" width="80" height="80">
</div>

## Overview

Daddy Django provides a comprehensive authentication system built on `dj-rest-auth` and `allauth`. The following endpoints are available for handling user authentication, registration, email verification, and password management.

## Base URL

All endpoints are relative to your domain (e.g., `https://yourdomain.com/` or `http://localhost:8000/`).

## Authentication Endpoints

### Login

**Endpoint:** `auth/login/`  
**Method:** POST  
**Description:** Authenticates a user and returns authentication tokens.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword",
  "captcha": "captchaResponseIfEnabled"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "username": "username",
    "email": "user@example.com",
    "first_name": "",
    "last_name": "",
    "actions_freezed_till": null
  }
}
```

**Error Responses:**
- `400 Bad Request`: Invalid credentials or account issues
- `403 Forbidden`: Account blocked or requires email verification

### Registration

**Endpoint:** `auth/registration/`  
**Method:** POST  
**Description:** Registers a new user account.

**Request Body:**
```json
{
  "email": "newuser@example.com",
  "password1": "securepassword",
  "password2": "securepassword",
  "first_name": "John",
  "last_name": "Doe",
  "captchaResponse": "captchaResponseIfEnabled"
}
```

**Response:**
```json
{
  "detail": "Verification e-mail sent."
}
```

**Error Responses:**
- `400 Bad Request`: Registration errors (email exists, weak password)
- `403 Forbidden`: Registration disabled

### Email Confirmation

**Endpoint:** `auth/registration/account-confirm-email/`  
**Method:** POST  
**Description:** Confirms a user's email using the verification key sent via email.

**Request Body:**
```json
{
  "key": "verification-key-from-email"
}
```

**Response:**
```json
{
  "detail": "Email verified successfully. You are now logged in.",
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Error Responses:**
- `404 Not Found`: Invalid confirmation key
- `400 Bad Request`: User account inactive

### Resend Email Confirmation

**Endpoint:** `resend-email-confirmation/`  
**Method:** POST  
**Description:** Resends the email verification link when a user hasn't received it or the previous one expired.

**Request Body:**
```json
{
  "token": "verification-token",
  "lang": "en"
}
```

**Response:**
```json
{
  "Status": true
}
```

**Error Responses:**
- `400 Bad Request`: Token not found, email already verified, or request in progress

### Password Change

**Endpoint:** `auth/password/change/`  
**Method:** POST  
**Description:** Changes the password for an authenticated user.

**Request Body:**
```json
{
  "old_password": "currentPassword",
  "new_password1": "newSecurePassword",
  "new_password2": "newSecurePassword"
}
```

**Response:**
```json
{
  "detail": "New password has been saved."
}
```

**Error Responses:**
- `400 Bad Request`: Invalid old password or new password validation failed
- `401 Unauthorized`: User not authenticated

### Password Reset Request

**Endpoint:** `auth/password/reset/`  
**Method:** POST  
**Description:** Initiates the password reset process by sending an email with reset instructions.

**Request Body:**
```json
{
  "email": "user@example.com",
  "captcha": "captchaResponseIfEnabled"
}
```

**Response:**
```json
{
  "detail": "Password reset e-mail has been sent."
}
```

**Error Responses:**
- `400 Bad Request`: Invalid email or captcha

### Password Reset Confirmation

**Endpoint:** `auth/password/reset/confirm/`  
**Method:** POST  
**Description:** Completes the password reset process using the token from email.

**Request Body:**
```json
{
  "uid": "base64EncodedUserId",
  "token": "passwordResetToken",
  "new_password1": "newSecurePassword",
  "new_password2": "newSecurePassword"
}
```

**Response:**
```json
{
  "detail": "Password has been reset with the new password."
}
```

**Error Responses:**
- `400 Bad Request`: Invalid token/uid or password validation failed

## Security Features

- **IP Tracking**: Login attempts are recorded with IP and device information
- **Action Freezing**: Certain operations (password reset/change) temporarily freeze account actions
- **Captcha**: Required for sensitive operations to prevent brute force attacks
- **Email Verification**: Required to activate new accounts

## Usage Notes

1. All authenticated requests should include the access token in the Authorization header:
   ```
   Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
   ```

2. Access tokens expire after a configured period. Use the refresh token to obtain a new access token:
   ```
   POST auth/token/refresh/
   {"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."}
   ```

3. When integrating with frontend applications, store tokens securely and implement proper token refresh mechanisms.

## Testing Authentication

You can test these endpoints using tools like Postman or curl:

```bash
# Example login request with curl
curl -X POST http://localhost:8000/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'
```
