# Number Plate Recognition System

A web-based automatic number plate recognition system using YOLOv8 and EasyOCR.

## Features

- Automatic number plate detection using YOLOv8
- Text recognition using EasyOCR
- Simple web interface with Flask
- Image preprocessing for better accuracy

## Installation

1. **Create and activate virtual environment**
   ```bash
   python -m venv myenv_new
   myenv_new\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure model exists**
   - Place your trained model at: `runs/detect/train/weights/best.pt`

## Usage

```bash
# Activate environment
myenv_new\Scripts\activate

# Run application
python app.py
```

Open your browser and go to `http://localhost:5000`

1. Upload an image containing a number plate
2. Click "Upload Image"
3. View the detected plate and recognized text

## Technologies

- **YOLOv8** - Object detection
- **EasyOCR** - Text recognition
- **Flask** - Web framework
- **OpenCV** - Image processing

## Project Structure

```
Number_Plate/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── templates/
│   └── index.html     # Web interface
└── runs/detect/train/weights/
    └── best.pt        # Trained model
```

---

**Educational Project** - February 2026
