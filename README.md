# GlucoScope-data
## GlucoScope Dataset Validation Scripts

### Overview

This repository contains Python scripts developed for automated quality assurance of the **GlucoScope Food Image Dataset**. These scripts complement the manual annotation review process by verifying dataset completeness, annotation integrity, duplicate images, and compatibility of exported COCO annotations.

The scripts were used during the dataset validation stage described in the manuscript to ensure that the released dataset is complete, consistent, and suitable for computer vision applications.

---

### Repository Structure

```
validation_scripts/
│
├── coco_validation.py
├── dataset_completeness.py
├── duplicate_detector.py
├── polygon_validation.py
└── README.md
```

---

### Requirements

- Python 3.9 or later
- Required Python packages

Install dependencies using:

```bash
pip install pycocotools opencv-python pillow shapely numpy
```

---

## Scripts

### 1. dataset_completeness.py

### Purpose

Verifies that every image in the dataset has a corresponding annotation file.

### Checks Performed

- Missing annotation files
- Missing images
- One-to-one correspondence between images and annotations

### Usage

```bash
python dataset_completeness.py
```

### Output

Example:

```
Total Images           : 1188
Total Annotation Files : 1188

✓ Dataset is complete.
```

or

```
Missing annotation:
P014_M0032.jpg
```

---

### 2. polygon_validation.py

### Purpose

Validates polygon annotations exported from CVAT.

### Checks Performed

- Polygon contains at least three vertices
- Invalid polygon geometry
- Self-intersecting polygons
- Empty annotations

### Usage

```bash
python polygon_validation.py
```

### Output

```
Validation completed.

No invalid polygons detected.
```

or

```
Invalid polygon found

Image:
P008_M0021.jpg

Class:
Sambar
```

---

### 3. duplicate_detector.py

### Purpose

Detects duplicate images using image hashing.

### Checks Performed

- Exact duplicate images
- Repeated image files

### Usage

```bash
python duplicate_detector.py
```

### Output

```
Duplicate detected

P002_M0045.jpg
P002_M0046.jpg
```

If no duplicates exist:

```
No duplicate images detected.
```

---

### 4. coco_validation.py

### Purpose

Validates the exported COCO annotation file.

### Checks Performed

- COCO JSON loads successfully
- Image IDs are valid
- Annotation IDs are consistent
- Category IDs are valid
- Dataset is compatible with standard computer vision frameworks

### Usage

```bash
python coco_validation.py
```

### Output

```
COCO Dataset Loaded Successfully

Images      : 1188
Annotations : 16542
Categories  : 82
```

---
