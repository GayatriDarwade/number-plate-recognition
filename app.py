import cv2
import pytesseract
from flask import Flask, render_template, request, send_file, jsonify
from ultralytics import YOLO
import os
from pathlib import Path
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load the trained YOLOv8 model
model_path = Path("runs") / "detect" / "train" / "weights" / "best.pt"
if not model_path.exists():
    logger.warning(f"Custom model not found at {model_path}, using YOLOv8s")
    model = YOLO("yolov8s.pt")
else:
    logger.info(f"Loading custom model from {model_path}")
    model = YOLO(str(model_path))

logger.info("Application initialized successfully (Pytesseract)")

def clean_text(text):
    """Clean OCR output"""
    text = re.sub(r'[^A-Z0-9]', '', text.upper())
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    recognized_text_easyocr = None

    if request.method == "POST":
        try:
            uploaded_file = request.files["file"]
            if uploaded_file.filename != "":
                image_path = "uploaded_image.jpg"
                uploaded_file.save(image_path)

                img = cv2.imread(image_path)

                # YOLOv8 detection
                results = model(img)
                number_plate_coords = results[0].boxes.xyxy

                if len(number_plate_coords) > 0:
                    for bbox in number_plate_coords:
                        x1, y1, x2, y2 = map(int, bbox)
                        cropped_number_plate = img[y1:y2, x1:x2]

                        # Upscale for better OCR
                        plate_upscaled = cv2.resize(cropped_number_plate, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
                        
                        # Convert to grayscale
                        gray = cv2.cvtColor(plate_upscaled, cv2.COLOR_BGR2GRAY)
                        
                        # Denoise
                        denoised = cv2.bilateralFilter(gray, 11, 17, 17)
                        
                        # Threshold
                        thresh = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

                        # Pytesseract OCR
                        custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                        text = pytesseract.image_to_string(thresh, config=custom_config)
                        
                        recognized_text_easyocr = clean_text(text)
                        
                        if not recognized_text_easyocr:
                            recognized_text_easyocr = "No text detected"

                        # Save cropped plate
                        cv2.imwrite("cropped_number_plate.jpg", cropped_number_plate)

                else:
                    recognized_text_easyocr = "No number plate detected."
        except Exception as e:
            logger.error(f"Error processing image: {str(e)}")
            recognized_text_easyocr = f"Error: {str(e)}"

    return render_template("index.html",
                           recognized_text_easyocr=recognized_text_easyocr)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Number Plate Recognition API is running"}), 200

@app.route('/cropped_number_plate.jpg')
def send_cropped_image():
    return send_file("cropped_number_plate.jpg", mimetype='image/jpeg')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
