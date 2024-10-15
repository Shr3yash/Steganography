import tensorflow as tf
import torch
import cv2
from PIL import Image
import numpy as np

#tensorFlow installation
print(f"TensorFlow version: {tf.__version__}")


print(f"PyTorch version: {torch.__version__}")


print(f"OpenCV version: {cv2.__version__}")


try:
    image = Image.open("test_image.jpg")
    image.show()
    print("PIL is working correctly.")
except Exception as e:
    print(f"Error opening image: {e}")
