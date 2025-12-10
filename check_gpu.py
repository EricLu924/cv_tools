import torch

# 檢查 CUDA 是否可用
if torch.cuda.is_available():
    print("✅ CUDA 可用")
    print(f"GPU 數量：{torch.cuda.device_count()}")
    print(f"GPU 名稱：{torch.cuda.get_device_name(0)}")
else:
    print("❌ CUDA 不可用")

# 驗證 Tensor 是否在 GPU 上運算
tensor = torch.tensor([1.0, 2.0, 3.0])
device = "cuda" if torch.cuda.is_available() else "cpu"
tensor = tensor.to(device)

print(f"Tensor 裝置位置：{tensor.device}")
