from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
import torch
from cnn import CNN

model = CNN(784, 6, 10)
with torch.no_grad():
    output = model(torch.randn(4, 1, 28, 28))
assert output.shape == (4, 10)
print(output.shape)
