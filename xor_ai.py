import torch
import torch.nn as nn
import torch.optim as optim

x = torch.tensor([
    [0,0],
    [0,1],
    [1,0],
    [1,1],
],dtype=torch.float32)

y = torch.tensor([
    [0],
    [1],
    [1],
    [0],
],dtype=torch.float32)

#Linear Model
model = nn.Sequential(
    #Layer 1--Hidden
    nn.Linear(2,4),
    nn.Sigmoid(),
    #Layer 2 
    nn.Linear(4,1),
    nn.Sigmoid()
)

# --- OPTIMIZER & LOSS ---
optimizer = optim.Adam(model.parameters(), lr=0.1)
loss_fn = nn.BCELoss()

# --- TRAINING LOOP ---
print("Training XOR (Linear)...")
for epoch in range(2000):
    optimizer.zero_grad()
    loss = loss_fn(model(x), y)
    loss.backward()
    optimizer.step()
    
    # Print loss every 500 steps to see if it's stuck
    if epoch % 500 == 0:
        print(f"Epoch {epoch}: Loss = {loss.item():.4f}")

# --- TEST IT ---
print("-" * 30)
print("Predictions (Should be 0, 1, 1, 0):")
print(model(x).detach()) # .detach() just cleans up the print output

# Answer With E and all reprsent very small number =====> It works bro
#This is called Exclusive OR or XOR hence the name XOR-ai
