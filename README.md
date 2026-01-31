


XOR-AI: Solving Non-Linear Logic with PyTorch
A lightweight neural network implemented in Python using PyTorch to solve the Exclusive OR (XOR) logic gate problem.

📌 Project Overview
The XOR problem is a classic challenge in machine learning because it cannot be solved by a simple linear classifier. This project demonstrates how a multi-layer perceptron (MLP) with a hidden layer and non-linear activation functions (Sigmoid) can learn the XOR pattern.

The XOR Truth Table
Input 1	Input 2	Output (XOR)
0	0	0
0	1	1
1	0	1
1	1	0
🚀 Features
Neural Network Architecture: Built using torch.nn.Sequential.

Hidden Layer: Includes a 4-neuron hidden layer to capture non-linear relationships.

Optimization: Uses the Adam optimizer with a learning rate of 0.1.

Loss Function: Implements Binary Cross Entropy (BCELoss), ideal for binary classification tasks.

Training Loop: Runs for 2000 epochs with real-time loss reporting.

🛠️ Requirements
To run this script, you need Python and the PyTorch library installed.

Bash
pip install torch
💻 Usage
Simply run the script using Python:

Bash
python xor_ai.py
Expected Output
The model will print the loss every 500 epochs. After training, it will output the predictions. Because of the Sigmoid activation, the results will be very close to 0 and 1 (e.g., 0.001 or 0.998), which confirms the model has "solved" the gate.

🧠 Model Architecture
The model consists of:

Input Layer: 2 neurons (representing the two binary inputs).

Hidden Layer: 4 neurons with Sigmoid activation.


Output Layer: 1 neuron with Sigmoid activation (producing a probability between 0 and 1).
