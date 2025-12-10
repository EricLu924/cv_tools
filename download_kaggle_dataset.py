import kagglehub
import shutil
import os

# 下載數據集
path = kagglehub.dataset_download("XXX")

# 目標路徑
target_dir = "/home/"
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 移動資料到指定目錄
for item in os.listdir(path):
    source = os.path.join(path, item)
    destination = os.path.join(target_dir, item)
    if os.path.isdir(source):
        shutil.move(source, destination)
    else:
        shutil.copy2(source, destination)

print("Path to dataset files:", target_dir)
