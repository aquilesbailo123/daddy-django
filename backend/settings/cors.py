
# CORS Configuration
# NOTE adjust this for production
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",  # Vite default port
    "http://127.0.0.1:5173",
    "https://kuskapay.com",
    "https://www.kuskapay.com",
    f"https://{env('DOMAIN', default='localhost')}",
]

# Allow credentials to be included in CORS requests (for JWT cookies if needed)
CORS_ALLOW_CREDENTIALS = True