import os
import glob

dataset_files = glob.glob(os.path.join(
    "./dataset_splits/", "*" + "train" + ".*"))
dataset_files = [x for x in dataset_files if "json" not in x]
dataset_files = glob.glob(
    os.path.join(
        "./dataset_splits/",
        "*" + "train" + ".*." + "pt",
    )
)
json_files = json_files = glob.glob(
    os.path.join("./dataset_splits/", "*" + "train" + ".json*")
)
# print(os.path.join('./dataset_splits/', "*" + 'train' + ".*"))
print(os.path.join(
    "./dataset_splits/",
    "*" + 'train' + "." + 'txt',
))
