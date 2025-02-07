# HNG12 Stage 0 - Public API

This is a simple Flask-based API that returns:
- Your registered HNG12 email.
- The current UTC datetime in ISO 8601 format.
- Your GitHub repository link.

## API Endpoint
- **Base URL:** `https://your-deployed-url.com`
- **GET / Response:**
  ```json
  {
    "email": "your-email@example.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/your-repo"
  }
