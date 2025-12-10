import os
import random
from PIL import Image
import numpy as np

def augment_image(image):
    """對圖片應用隨機增強處理。"""
    # 隨機翻轉
    if random.choice([True, False]):
        image = image.transpose(Image.FLIP_LEFT_RIGHT)

    # 隨機旋轉
    angle = random.choice([0, 90, 180, 270])
    image = image.rotate(angle)

    # 隨機裁剪
    width, height = image.size
    crop_size = random.uniform(0.8, 1.0)  # 裁剪比例範圍 80% 到 100%
    new_width = int(width * crop_size)
    new_height = int(height * crop_size)

    left = random.randint(0, width - new_width)
    upper = random.randint(0, height - new_height)
    right = left + new_width
    lower = upper + new_height

    image = image.crop((left, upper, right, lower))
    image = image.resize((width, height))  # 調整回原始大小

    # 隨機加入雜訊
    image_np = np.array(image)
    noise = np.random.normal(0, 10, image_np.shape).astype(np.int16)  # 雜訊標準差 10
    image_np = np.clip(image_np + noise, 0, 255).astype(np.uint8)
    image = Image.fromarray(image_np)

    return image

def balance_dataset(base_path, target_count=None):
    """平衡資料集中各資料夾內圖片的數量。

    Args:
        base_path (str): 資料集的根目錄路徑。
        target_count (int, optional): 要平衡到的圖片總數。如果未指定，則以張數最多的類別為標準。
    """
    # 支援的圖片格式
    valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}

    # 獲取所有分級資料夾
    grade_folders = [os.path.join(base_path, folder) for folder in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, folder))]

    # 統計每個資料夾內的圖片數量
    image_counts = {folder: len([img for img in os.listdir(folder) if os.path.splitext(img)[-1].lower() in valid_extensions]) for folder in grade_folders}
    max_count = max(image_counts.values())

    # 使用指定的 target_count 或以最大圖片數量為基準
    target_count = target_count if target_count is not None else max_count

    print(f"平衡前的圖片數量：{image_counts}")
    print(f"目標平衡到的圖片數量：{target_count}")

    # 增強圖片數量較少的資料夾
    for folder in grade_folders:
        current_count = image_counts[folder]
        if current_count < target_count:
            images = [os.path.join(folder, img) for img in os.listdir(folder) if os.path.splitext(img)[-1].lower() in valid_extensions]
            if not images:
                print(f"警告：資料夾 {folder} 中沒有有效圖片，跳過增強。")
                continue

            while current_count < target_count:
                # 隨機選擇一張圖片進行增強
                image_path = random.choice(images)
                image = Image.open(image_path)

                # 應用增強
                augmented_image = augment_image(image)

                # 儲存增強後的圖片
                new_image_name = f"aug_{current_count}.png"
                augmented_image.save(os.path.join(folder, new_image_name))

                current_count += 1

    # 再次統計圖片數量以驗證平衡
    image_counts = {folder: len(os.listdir(folder)) for folder in grade_folders}
    print(f"平衡後的圖片數量：{image_counts}")

# 使用範例
base_path = r"\home\Dataset"  # 將此路徑替換為您的資料集路徑
target_count = 1000  # 設定目標平衡到的圖片數量。如果為 None，則以最大類別數為基準
balance_dataset(base_path, target_count)
