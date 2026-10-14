import sys, torch, numpy, matplotlib

print("Python:", sys.version.split()[0])
print("PyTorch:", torch.__version__)
print("NumPy:", numpy.__version__)

x = torch.tensor(3.0, requires_grad=True)
y = x**2 + 2*x
y.backward()
print("dy/dx at x=3:", x.grad.item())  # should be 8.0