# Overlay API Documentation

## Overview
The Overlay API is a RESTful service built with Flask and MongoDB that allows users to create, read, update, and delete overlay objects. It is designed to be used in conjunction with a React frontend, and CORS is enabled for cross-origin requests.

## Base URL
`http://localhost:5000`


## Endpoints

### 1. Welcome Endpoint
- **GET** `/`
- **Description**: Returns a welcome message.
- **Response**:
  - **200 OK**
    ```json
    {
      "message": "Hello User"
    }
    ```

### 2. Create Overlay
- **POST** `/overlays`
- **Description**: Creates a new overlay.
- **Request Body**:
  - Content-Type: `application/json`
  - **Example**:
    ```json
    {
      "content": "Overlay content here",
      "position": {"x": 100, "y": 200},
      "size": {"width": 300, "height": 150}
    }
    ```
- **Response**:
  - **201 Created**
    ```json
    {
      "id": "605c72bcf12345678abcd123"
    }
    ```

### 3. Get All Overlays
- **GET** `/overlays`
- **Description**: Retrieves a list of all overlays.
- **Response**:
  - **200 OK**
    ```json
    [
      {
        "id": "605c72bcf12345678abcd123",
        "content": "Overlay content here",
        "position": {"x": 100, "y": 200},
        "size": {"width": 300, "height": 150}
      },
      ...
    ]
    ```

### 4. Update Overlay
- **PUT** `/overlays/<id>`
- **Description**: Updates an existing overlay.
- **Path Parameters**:
  - `id`: The ID of the overlay to update.
- **Request Body**:
  - Content-Type: `application/json`
  - **Example**:
    ```json
    {
      "content": "Updated overlay content",
      "position": {"x": 150, "y": 250},
      "size": {"width": 350, "height": 200}
    }
    ```
- **Response**:
  - **200 OK**
    ```json
    {
      "msg": "Overlay updated"
    }
    ```

### 5. Delete Overlay
- **DELETE** `/overlays/<id>`
- **Description**: Deletes an overlay.
- **Path Parameters**:
  - `id`: The ID of the overlay to delete.
- **Response**:
  - **200 OK**
    ```json
    {
      "msg": "Overlay deleted"
    }
    ```

## Error Handling
- All endpoints will return appropriate HTTP status codes and error messages in case of failure.
- Common error responses include:
  - **400 Bad Request**: When the request is malformed or missing required fields.
  - **404 Not Found**: When the specified overlay ID does not exist.
  - **500 Internal Server Error**: For unexpected server errors.
