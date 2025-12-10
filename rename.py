import os

def sort_photo_names(folder_path):
    try:
        # 獲取目錄中的所有檔案名稱
        file_names = os.listdir(folder_path)

        # 過濾照片檔案 (可以根據需要調整副檔名過濾)
        photo_files = [f for f in file_names if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

        # 排序照片檔案名稱
        sorted_files = sorted(photo_files)

        # 重新命名檔案
        for index, file_name in enumerate(sorted_files):
            # 新檔案名稱 (依序命名，例如 001.jpg)
            new_name = f"{index + 1:03d}{os.path.splitext(file_name)[1]}"
            
            # 取得完整路徑
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)

            # 重新命名檔案
            os.rename(old_path, new_path)
            print(f"{file_name} -> {new_name}")

        print("照片重新命名完成！")

    except Exception as e:
        print(f"發生錯誤：{e}")

# 指定目錄路徑
folder_path = "Dataset\XXX"
sort_photo_names(folder_path)
