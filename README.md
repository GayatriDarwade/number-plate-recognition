# Number Plate Recognition System










































































































    app.run(host='0.0.0.0', port=port, debug=False)    port = int(os.environ.get("PORT", 5000))if __name__ == "__main__":    return send_file("cropped_number_plate.jpg", mimetype='image/jpeg')def send_cropped_image():@app.route('/cropped_number_plate.jpg')    return jsonify({"status": "healthy", "message": "Number Plate Recognition API is running (Tesseract)"}), 200    """Health check endpoint for Render"""def health():@app.route('/health')                           recognized_text_easyocr=recognized_text)    return render_template("index.html",            recognized_text = f"Error: {str(e)}"            logger.error(f"Error processing image: {str(e)}")        except Exception as e:                    recognized_text = "No number plate detected."                else:                        cv2.imwrite(cropped_image_path, cropped_number_plate)                        cropped_image_path = "cropped_number_plate.jpg"                        # Save cropped plate                            logger.info(f"Detected plate text: {recognized_text}")                        else:                            recognized_text = "No text detected"                        if not recognized_text:                                                recognized_text = clean_text(text)                        # Clean and format the text                                                text = pytesseract.image_to_string(thresh, config=custom_config)                        custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'                        # Configure pytesseract for license plates                        # --- Pytesseract OCR ---                        thresh = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)                        # Apply adaptive thresholding                                                denoised = cv2.bilateralFilter(gray, 11, 17, 17)                        # Apply bilateral filter to reduce noise while keeping edges sharp                                                gray = cv2.cvtColor(plate_upscaled, cv2.COLOR_BGR2GRAY)                        # Convert to grayscale                                                plate_upscaled = cv2.resize(cropped_number_plate, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)                        # Upscale image for better OCR accuracy                        # --- Preprocessing for OCR ---                        cropped_number_plate = img[y1:y2, x1:x2]                        x1, y1, x2, y2 = map(int, bbox)                    for bbox in number_plate_coords:                if len(number_plate_coords) > 0:                number_plate_coords = results[0].boxes.xyxy                results = model(img)                # YOLOv8 detection                img = cv2.imread(image_path)                uploaded_file.save(image_path)                image_path = "uploaded_image.jpg"            if uploaded_file.filename != "":            uploaded_file = request.files["file"]        try:    if request.method == "POST":    recognized_text = Nonedef index():@app.route("/", methods=["GET", "POST"])    return text    text = re.sub(r'[^A-Z0-9]', '', text.upper())    # Remove special characters except alphanumeric    """Clean OCR output to extract likely plate numbers"""def clean_text(text):logger.info("Application initialized successfully (Tesseract OCR version)")    model = YOLO(str(model_path))    logger.info(f"Loading custom model from {model_path}")else:    model = YOLO("yolov8s.pt")    logger.warning(f"Custom model not found at {model_path}, using YOLOv8s")if not model_path.exists():model_path = Path("runs") / "detect" / "train" / "weights" / "best.pt"# Load the trained YOLOv8 modelapp = Flask(__name__)logger = logging.getLogger(__name__)logging.basicConfig(level=logging.INFO)# Configure loggingimport reimport loggingfrom pathlib import Pathimport osfrom ultralytics import YOLOfrom flask import Flask, render_template, request, send_file, jsonifyA web-based automatic number plate recognition system using YOLOv8 and Pytesseract OCR.

## Features

- Automatic number plate detection using YOLOv8
- Text recognition using Pytesseract
- Simple web interface with Flask
- Image preprocessing for better accuracy
- Free tier deployment ready

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
- **Pytesseract** - Text recognition
- **Flask** - Web framework
- **OpenCV** - Image processing

## Project Structure

```
Number_Plate/
├── app.py              # Main application
├── config.py           # Configuration settings
├── requirements.txt    # Dependencies
├── Procfile           # Deployment configuration
├── render.yaml        # Render deployment config
├── templates/
│   └── index.html     # Web interface
└── runs/detect/train/weights/
    └── best.pt        # Trained model
```

## Deployment to Render

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to [render.com](https://render.com) and sign in
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: number-plate-recognition
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120`
     - **Plan**: Free tier works!
   - Add Environment Variable:
     - Key: `APT_PACKAGES`
     - Value: `tesseract-ocr`
   - Click "Create Web Service"

3. **Important Notes**
   - First deployment takes 3-5 minutes
   - Free tier (512MB) works perfectly with Pytesseract
   - Health check endpoint: `/health`

## Environment Variables (Optional)

- `PORT`: Auto-set by Render
- `FLASK_ENV`: `production` (default for deployment)
- `LOG_LEVEL`: `INFO` or `DEBUG`

## Troubleshooting Deployment

### Tesseract Not Found
**Problem**: `tesseract is not installed`
**Solution**: Add environment variable `APT_PACKAGES=tesseract-ocr` in Render

### No Open Ports Detected
**Problem**: `==> No open ports detected`
**Solution**: Ensure gunicorn binds to `$PORT` (already configured in Procfile)

---

**Educational Project** - February 2026
