from ultralytics import YOLO

# Load model (seg_ppl.pt, RPS.pt, Default: Yolov8s.pt)
model = YOLO('yolov8s.pt') 

# Use the model's predict method with the webcam as the source
model.predict(source= 0, show=True, save=True)
# in source add wahat your video / image source should be, if it is a file add name in '' 
# if it is a camera /webcam add index default = 0 
# to find camera index run the find.py script 
# make sure ultralytics is installed before running the code 
# show = true to show output
#  save = true to save out (a new folder called 'runs' will be created