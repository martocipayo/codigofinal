import cv2
import torch
from db import db_call

def obtener_camaras():
    return [
        {
            "id": 1,
            "ubicacion": "Orbitty",
            "estado": "Activo",
            "direccionIP": "http://127.0.0.1:5000/video_feed"
        }
    ]

def procesar_stream_orbitty():
    """
    Procesa la cámara USB de Orbitty usando YOLOv5 
    y guarda los eventos detectados en la base de datos mediante db_call.
    """
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("No se pudo conectar a la cámara de Orbitty.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        detections = results.pandas().xyxy[0]

        for _, row in detections.iterrows():
            label = row['name']
            confidence = row['confidence']
            
            if label == 'person' and confidence > 0.5:
                query = f"INSERT INTO detecciones (camara, descripcion, timestamp) VALUES ('Orbitty', 'Detección YOLOv5: {label} ({confidence:.2f})', datetime('now'))"
                db_call(query)
                print(f"[Backend] Objeto guardado en BD: {label} ({confidence:.2f})")

        break

    cap.release()
