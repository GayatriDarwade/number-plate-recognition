import cv2
import easyocr
from flask import Flask, render_template, request, send_file
from ultralytics import YOLO
import os
from pathlib import Path

app = Flask(__name__)

# Load the trained YOLOv8 model
model_path = Path("runs") / "detect" / "train" / "weights" / "best.pt"
model = YOLO(str(model_path))

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

@app.route("/", methods=["GET", "POST"])
def index():
    recognized_text_easyocr = None

    if request.method == "POST":
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

                    # --- Preprocessing for OCR ---
                    # Upscale image for better OCR accuracy
                    plate_upscaled = cv2.resize(cropped_number_plate, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                    
                    # Slight contrast enhancement
                    lab = cv2.cvtColor(plate_upscaled, cv2.COLOR_BGR2LAB)
                    l, a, b = cv2.split(lab)
                    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
                    l = clahe.apply(l)
                    enhanced = cv2.merge([l, a, b])
                    enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)

                    # --- EasyOCR ---
                    ocr_result_easy = reader.readtext(enhanced, detail=1)
                    
                    # Filter by confidence and build text
                    if ocr_result_easy:
                        recognized_text_easyocr = " ".join([text[1] for text in ocr_result_easy if text[2] > 0.3])
                        if not recognized_text_easyocr:
                            recognized_text_easyocr = "No confident text detected"
                    else:
                        recognized_text_easyocr = "No text detected"

                    # Save cropped plate
                    cropped_image_path = "cropped_number_plate.jpg"
                    cv2.imwrite(cropped_image_path, cropped_number_plate)

            else:
                recognized_text_easyocr = "No number plate detected."

    return render_template("index.html",
                           recognized_text_easyocr=recognized_text_easyocr)

@app.route('/cropped_number_plate.jpg')
def send_cropped_image():
    return send_file("cropped_number_plate.jpg", mimetype='image/jpeg')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
