import os
from flask import Flask, render_template, request, redirect, url_for
from ultralytics import YOLO

app = Flask(__name__)

# Ensure folders exist
UPLOAD_FOLDER = "static/uploads/"
RESULT_FOLDER = "static/results/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load YOLO model
model = YOLO("model/train22/weights/best.pt")

@app.route("/", methods=["GET", "POST"])
def index():
    result_image = None
    message = ""
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            from werkzeug.utils import secure_filename
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            # Run prediction
            results = model.predict(filepath, imgsz=640, conf=0.25, device='cpu')
            
            result_path = os.path.join(RESULT_FOLDER, "result_" + filename)
            result_img = results[0].plot()
            import cv2
            cv2.imwrite(result_path, result_img)

            result_image = result_path

            if len(results[0].boxes) > 0:
                message = "⚠️ Microplastics detected! Water is NOT suitable for drinking."
            else:
                message = "✅ No microplastics detected. Water is suitable for drinking."

    return render_template("index.html", result_image=result_image, message=message)


if __name__ == "__main__":
    app.run(debug=True)
