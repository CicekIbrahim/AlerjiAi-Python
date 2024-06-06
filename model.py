# yolov9.py
import torch

def detect_with_yolov9(image_path):

    model_path = './yolov9'  # Replace with the actual path to your local YOLOv9 repo
    model = torch.hub.load(model_path, 'custom', path='bestf.pt', source='local', force_reload=True)
    

    results = model(image_path)
    

    if results.xyxy[0].size(0) > 0:  
        detected_items = []
        for *box, conf, cls in results.xyxy[0]:
            detected_items.append(model.names[int(cls)])
        return detected_items
    else:
        return None
