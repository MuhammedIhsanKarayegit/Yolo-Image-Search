from ultralytics import YOLO
from pathlib import Path
import torch
from PIL import Image
import numbers as np
from src.config import load_config


class YOLOv11Inference:
    def __init__(self, model_name, device="cuda", ):
        self.model = YOLO(model_name)
        self.model.to(device)

        #Loading config from defautlt.yaml
        config = load_config()
        self.conf_threshold = config["model"]["conf_threshold"]
        self.extensions = config["data"]["image_extension"]

    def process_image(self, image_path):
        pass

    def process_directory (self, directory):
        metadata = []

        patterns = [f"*{ext}" for ext in self.extensions] 

        image_path = []
        for pattern in patterns:
            image_path.extend(Path(directory).glob(pattern))

        for img_path in image_path:
            try:
                metadata.extend(self.process_image(img_path))
            except Exception as e:
                print(f"Error processing {img_path} {str(e)}")
                continue