from pycocotools.coco import COCO

coco = COCO("instances_train.json")

print(len(coco.imgs))
print(len(coco.anns))
print(len(coco.cats))