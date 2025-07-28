# API Documentation 2

## Overview
This API provides comprehensive user management functionality with authentication and authorization.

## Authentication
All endpoints require Bearer token authentication.

## Endpoints

### GET /api/users
Retrieves a list of all users.

**Parameters:**
- `page` (optional): Page number
- `limit` (optional): Items per page

**Response:**
```json
{
  "users": [
    {
      "id": 1,
      "username": "john_doe",
      "email": "john@example.com"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150
  }
}
```

### POST /api/users
Creates a new user account.

**Request Body:**
```json
{
  "username": "new_user",
  "email": "user@example.com",
  "password": "secure_password"
}
```

## Error Codes
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error

## Rate Limiting
1000 requests per hour per API key.
