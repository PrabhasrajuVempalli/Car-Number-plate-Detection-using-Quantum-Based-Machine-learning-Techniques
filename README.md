# Indian ANPR Full-Stack System

A high-precision Automatic Number Plate Recognition system specifically optimized for Indian vehicles.

## Features
- **YOLO Detection**: Latest YOLO models for vehicle and plate localization.
- **Ensemble OCR**: Combined EasyOCR + custom CNN + Super Resolution for maximum accuracy.
- **FastAPI Backend**: High-performance REST APIs for image and video processing.
- **MongoDB Storage**: Persistent storage of detection history.
- **Premium Dashboard**: Modern glassmorphism UI for real-time interaction.
- **Dockerized**: Easy deployment with Docker Compose.

## Project Structure
- `backend/`: FastAPI application, database logic, and processing utilities.
- `model/`: Pre-trained YOLO weights and training scripts.
- `frontend/`: Vanilla HTML/JS dashboard.
- `output/`: Processed video outputs.

## Setup & Running

### Using Docker (Recommended)
1. Ensure Docker and Docker Compose are installed.
2. Run:
   ```bash
   docker-compose up --build
   ```
3. Access the dashboard at `http://localhost`.
4. API docs available at `http://localhost:8000/docs`.

### Running Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start MongoDB locally (port 27017).
3. Run the backend:
   ```bash
   python -m backend.main
   ```
4. Open `frontend/index.html` in your browser.

## API Endpoints
- `POST /detect-image`: Upload an image to detect plates.
- `POST /detect-video`: Upload a video for frame-by-frame processing.
- `GET /health`: Check system status.
- `GET /recent`: Retrieve recent detections from MongoDB.

## Accuracy Notes
The system handles:
- Different Indian fonts and two-line plates.
- Low light and blurred conditions via sharpening and CLAHE enhancement.
- High-speed movement via temporal smoothing in video.
