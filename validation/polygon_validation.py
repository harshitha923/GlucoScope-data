import json
import os

folder = "annotations"

for file in os.listdir(folder):

    if not file.endswith(".json"):
        continue

    path = os.path.join(folder, file)

    with open(path) as f:
        data = json.load(f)

    for obj in data["shapes"]:

        pts = obj["points"]

        if len(pts) < 3:
            print(file, obj["label"], "Invalid polygon")