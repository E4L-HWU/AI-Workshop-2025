import cv2
from cv2_enumerate_cameras import enumerate_cameras

# Enumerate all connected cameras
cameras = enumerate_cameras()

# Display the list of cameras with their indices and names
for cam in cameras:
    print(f"Index: {cam.index}, Name: {cam.name}")
# this script is to find the index of an external third part camera to be used on 
# Detect.py 
