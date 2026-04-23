from ultralytics import YOLO
from PIL import Image
import io

FOOD_LABELS = {
    "banana", "apple", "sandwich", "orange", "broccoli",
    "carrot", "hot dog", "pizza", "donut", "cake",
    "bottle", "cup", "bowl"
}

model = YOLO("yolov8n.pt")

def detect_ingredients(image_bytes: bytes) -> list:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    results = model(image, conf=0.35)

    detected = []
    for result in results:
        for box in result.boxes:
            label = result.names[int(box.cls)]
            if label.lower() in FOOD_LABELS:
                detected.append(label)

    return sorted(set(detected))