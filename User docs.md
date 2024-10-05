
---

# User Documentation

## 1. Introduction
This application allows users to stream live video using an RTSP URL and manage overlays (text or images) on top of the livestream. Users can create, position, resize, and delete overlays through an intuitive interface.

## 2. Setup Guide

### 2.1 Prerequisites
Before you can run the app, ensure the following are installed on your machine:
- **Python** (version 3.x)
- **Node.js** (version 14 or higher)
- **MongoDB** (running locally or on a cloud service)
- **React** (via Node.js)

### 2.2 Backend (Flask + MongoDB) Setup

1. **Clone the Repository**
   ```bash
   git clone <repo_url>
   cd <repo_directory>
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **MongoDB Configuration**
   Ensure MongoDB is running locally or provide a connection string to a MongoDB instance (for cloud MongoDB, update `.env`).

5. **Environment Variables**
   Create a `.env` file in the root directory and add the following variables:
   ```
   FLASK_APP=app.py
   MONGO_URI=mongodb://localhost:27017/overlays_db
   ```

6. **Run the Flask Backend**
   ```bash
   flask run
   ```
   The Flask server will run on `http://localhost:5000`.

### 2.3 Frontend (React) Setup

1. **Navigate to the React App Directory**
   ```bash
   cd client
   ```

2. **Install Node.js Dependencies**
   ```bash
   npm install
   ```

3. **Run the React Application**
   ```bash
   npm start
   ```
   The React app will run on `http://localhost:3000`.

---

## 3. Using the App

### 3.1 Inputting the RTSP URL
1. **Open the App**: Once both the Flask backend and the React frontend are running, open your browser and navigate to `http://localhost:3000`.
2. **RTSP URL Input**: On the landing page, you will see a field to input an RTSP URL. Enter a valid RTSP stream URL (you can use services like [RTSP.me](https://rtsp.me) to create a temporary stream).
3. **Play the Stream**: After entering the URL, press the "Play" button to start the livestream. Basic video controls such as play, pause, and volume adjustment are available.

### 3.2 Managing Overlays

1. **Creating an Overlay**:
   - Below the video stream, you’ll find an option to add an overlay.
   - You can choose between **text** or **image** as the type of overlay.
   - For text, simply enter the desired text content. For an image, provide the URL of the image to be overlaid.
   - Click **Create Overlay**.

2. **Positioning an Overlay**:
   - Once created, the overlay appears on top of the video.
   - Click and drag the overlay to move it around the video screen. It will remain within the bounds of the video.

3. **Resizing an Overlay**:
   - To resize the overlay, click on it and drag from any of the four corners. You can resize both text and image overlays.

4. **Deleting an Overlay**:
   - Each overlay has a close button (`×`) in the top-right corner. Click this button to remove the overlay from the video.
   - Alternatively, you can manage overlays from the sidebar, where you can view, edit, or delete overlays.

### 3.3 Saving Overlays
- The app supports saving overlay settings (content, position, size). You can retrieve and manage them through the API (details in the API documentation).

---

## 4. MongoDB Operations
All overlay data is stored in MongoDB. This includes:
- **Content**: The text or image URL.
- **Position**: Coordinates relative to the video (x, y).
- **Size**: The dimensions of the overlay.

You can view and manage this data using MongoDB GUI tools (like MongoDB Compass) or directly through the API.

---

## 5. Troubleshooting

- **RTSP URL Not Working**: Ensure that the URL is a valid RTSP stream. You can test the stream with external tools like VLC Player.
- **Overlays Not Appearing**: Refresh the page or check if the backend is running properly by visiting `http://localhost:5000`.
- **MongoDB Connection Issues**: Ensure MongoDB is running on your machine or that the cloud MongoDB URI is correctly configured in the `.env` file.

---
