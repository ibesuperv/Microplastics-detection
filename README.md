#  Microplastic Detection in Water

This project uses a **YOLOv8 deep learning model** to detect **microplastics in water samples**.  
It provides a **web interface** where users can upload water images and check if the sample is **suitable for drinking or not**.

---

##  Features
- Upload water sample images directly in the browser.
- Detect microplastics using a trained YOLOv8 model.
- Dynamic image display with detection results.
- Tailwind CSS styled UI with clean, responsive design.
- Simple drinking water suitability message:
  -  **Suitable for drinking** (no microplastics detected).
  -  **Not suitable for drinking** (microplastics detected).

---

## Project Structure
```
MiniProject/
│
├── model/
│   └── train22/weights/best.pt   # Trained YOLOv8 model weights
│
├── Resources/
│   └── 3_Testing/                # Test images
│
├── static/                       # CSS, JS, and uploaded result files
│
├── templates/
│   └── index.html                # Frontend UI
│
├── app.py                        # Flask backend
└── README.md                     # Project documentation
```

---

## ⚙Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/ibesuperv/Microplastics-detection.git
cd Microplastics-detection
```
### 2. Install dependencies
```bash
pip install ultralytics opencv-python
```

### 3. Run the Flask app
```bash
python app.py
```
App will run at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
--
## usage
1. Open the app in a browser.
2. Upload a water sample image (.jpg, .png, .jpeg).
3. Wait for detection results.
4. The page will show:
   - The uploaded image with detection boxes (if any).
   - A message: "Suitable for Drinking" or "Not Suitable for Drinking".

--
# Model and Dataset
- **Model**: YOLOv8 (Ultralytics)  
- **Trained on**: [Kaggle Microplastics Dataset](https://www.kaggle.com/datasets/imtkaggleteam/microplastic-dataset-for-computer-vision)  
- **Training Platform**: Google Colab with T4 GPU  
- **Training Notebook**: [Colab Link](https://colab.research.google.com/drive/14T0IYoGNf2OMkdKJrqLzFoNt4M1gppRF?usp=sharing)  

