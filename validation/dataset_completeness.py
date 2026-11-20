import os

image_dir = "images"
label_dir = "annotations"

images = {os.path.splitext(f)[0] for f in os.listdir(image_dir)
          if f.lower().endswith((".jpg", ".jpeg", ".png"))}

labels = {os.path.splitext(f)[0] for f in os.listdir(label_dir)
          if f.endswith(".json")}

missing = images - labels

print(f"Total images: {len(images)}")
print(f"Annotated images: {len(labels)}")

if missing:
    print("\nMissing annotations:")
    for f in sorted(missing):
        print(f)
else:
    print("\nAll images have annotations.")