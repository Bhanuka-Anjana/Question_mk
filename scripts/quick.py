import torch
print("torch.cuda.is_available():", torch.cuda.is_available())
print("torch.version.cuda:", torch.version.cuda)
if torch.cuda.is_available(): print("GPU:", torch.cuda.get_device_name(0))