import os
import random
from PIL import Image

# 設定資料夾路徑
folder_path = r"XXX"  # 請替換成你的資料夾路徑

# 設定圖片大小
image_size = (200, 200)  # 你可以根據需要調整圖片的大小


image_paths = []
for category in os.listdir(folder_path):
    category_path = os.path.join(folder_path, category)
    if os.path.isdir(category_path):
        images = [os.path.join(category_path, file) for file in os.listdir(category_path) if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
        image_paths.extend(images)

# 隨機挑選40張
selected_images = random.sample(image_paths, 40)

# 載入並調整圖片大小
resized_images = []
for img_path in selected_images:
    img = Image.open(img_path)
    img = img.resize(image_size)  # 調整圖片大小
    resized_images.append(img)

# 創建一張新的圖片，尺寸為4x10的拼圖
width, height = image_size
result = Image.new('RGB', (width * 10, height * 4))

# 將每張圖片放到新圖片中的指定位置
for i in range(4):
    for j in range(10):
        result.paste(resized_images[i * 10 + j], (j * width, i * height))

# 顯示或儲存結果
result.show()  # 顯示圖片
result.save("output_image.jpg")  # 保存成一張新的圖片