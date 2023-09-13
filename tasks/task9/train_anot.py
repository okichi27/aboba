import os
import csv
import cv2
def convert_sku_to_yolo():
    annotation_file = open("/home/rodion/yuliia0/aboba/tasks/task10.net/train_solution.xls")
    annotation_file = csv.reader(annotation_file, delimiter=" ")
image_paths = os.listdir("/home/rodion/yuliia0/aboba/tasks/task10.net/data/training_images/vid_4_600.jpg")

prev_img_path = ""
counter = 0
for annotation in annotation_file:
    if counter % 12084 == 0:
        print(counter)
    counter += 1
    annotation = annotation[0].split(",")
    img_path = "PATH_TO\\images\\" + annotation[0]
    resize_factor = 640 / max(int(annotation[6]), int(annotation[7]))
    if img_path != prev_img_path:
        img = cv2.imread(img_path)
        img = cv2.resize(img, (int(img.shape[1] * resize_factor), int(img.shape[0] * resize_factor)))
        cv2.imwrite(img_path, img)
        prev_img_path = img_path
    bbox = f"{(int(annotation[1]) * resize_factor) / (int(annotation[6]) * resize_factor)} {(int(annotation[2]) * resize_factor) / (int(annotation[7]) * resize_factor)} {(int(annotation[3]) * resize_factor) / (int(annotation[6]) * resize_factor)} {(int(annotation[4]) * resize_factor) / (int(annotation[7]) * resize_factor)}"
    x1 = (int(annotation[1]) * resize_factor)
    y1 = (int(annotation[2]) * resize_factor)
    x2 = (int(annotation[3]) * resize_factor)
    y2 = (int(annotation[4]) * resize_factor)
    width = (int(annotation[6]) * resize_factor)
    height = (int(annotation[7]) * resize_factor)
    bbox = f"{((x1 + x2) / 2) / width} {((y1 + y2) / 2) / height} {(x2 - x1) / width} {(y2 - y1) / height}"
    label_path = img_path.replace("images", "labelsval").replace("jpg", "txt")
    with open(label_path, "a") as file:
        file.write("1 " + bbox + "\n")
def check_sku_imgs():
    image_paths = os.listdir("/home/rodion/yuliia0/aboba/tasks/task10.net/data/training_images/vid_4_600.jpg")
for img in image_paths:
    if img.find("train") != -1:
        image = cv2.imread("/home/rodion/yuliia0/aboba/tasks/task10.net/data/training_images/vid_4_600.jpg" + img)
        if image.shape[1] > 640:
            print(img)
convert_sku_to_yolo()