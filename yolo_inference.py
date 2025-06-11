from ultralytics import YOLO

model = YOLO("models/best.pt")  # Load a pretrained YOLOv8 model

results = model.predict('input_vidoes/08fd33_4.mp4',save=True)
print(results[0])  # Print the results of the prediction

print("=====================================")

for box in results[0].boxes:
    print(box)