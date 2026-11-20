import hashlib
import os

folder="images"

hashes={}

for file in os.listdir(folder):

    path=os.path.join(folder,file)

    with open(path,"rb") as f:

        h=hashlib.md5(f.read()).hexdigest()

    if h in hashes:

        print("Duplicate:",file,"==",hashes[h])

    else:

        hashes[h]=file