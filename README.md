# DA6401
DL Assignments
DA6401 Assignment 1: Neural Network Implementation for Fashion-MNIST Classification
Project Overview
This repository contains the implementation of a flexible feedforward neural network trained and evaluated on the Fashion-MNIST dataset. Various optimization algorithms, hyperparameter tuning strategies, and visualizations using WandB are implemented.

Repository Structure
DLass1Q1.ipynb: Dataset visualization and initial analysis.
DLass1Q2.ipynb: Flexible feedforward neural network architecture implementation.
DLass1Q3.ipynb: Backpropagation implementation with optimizers (SGD, Momentum, NAG, RMSprop, Adam, Nadam).
DLass1Q4to6.ipynb: Hyperparameter tuning and WandB sweeps.
DLass1Q7.ipynb: Evaluation using a confusion matrix visualization.
DLass1Q8.ipynb: Comparison between cross-entropy and squared error losses.
DLass1Q10.ipynb: Applying insights from Fashion-MNIST to the MNIST digit recognition task.
Activations.ipynb: Exploration of various activation functions.
Loss.ipynb: Detailed experiments and comparisons for different loss functions.
Optimizers.ipynb: In-depth exploration of optimization algorithms.
README.md: Project description, setup, and execution instructions.
Setup Instructions
1. Clone Repository
bash
Copy code
git clone https://github.com/SubikkshaS/da6401_assignment1.git
cd da6401_assignment1
2. Create Virtual Environment and Install Dependencies
bash
Copy code
python -m venv env
source env/bin/activate  # (On Windows: env\Scripts\activate)
pip install -r requirements.txt
Dependencies (requirements.txt)
nginx
Copy code
numpy
matplotlib
tensorflow
keras
wandb
scikit-learn
tqdm
3. WandB Setup
Create an account at WandB and log in:
bash
Copy code
wandb login
Dataset
Fashion-MNIST: Automatically loaded via keras.datasets.fashion_mnist.
MNIST: Automatically loaded via keras.datasets.mnist.
Running Experiments
Question 2: Flexible Neural Network
Run the flexible neural network implementation:

bash
Copy code
python DLass1Q2.ipynb --num_layers 3 --hidden_size 128 --activation ReLU
Customize layers, neurons, and activations via parameters.
Question 3: Backpropagation with Optimizers
Run optimizer implementations:

bash
Copy code
python DLass1Q3.ipynb
Implemented optimizers: SGD, Momentum, NAG, RMSProp, Adam, Nadam.
Adjust hyperparameters directly within notebook.
Questions 4-6: Hyperparameter Sweeps
Perform hyperparameter sweeps:

bash
Copy code
python DLass1Q4to6.ipynb
Sweeps visualized via WandB.
Question 7: Confusion Matrix Visualization
Evaluate best model and plot confusion matrix:

bash
Copy code
python DLass1Q7.ipynb
Question 8: Loss Function Comparison
Compare Cross-Entropy vs. Squared Error:

bash
Copy code
python DLass1Q8.ipynb
WandB Visualization and Reports
Project Link: DA6401 Assignment 1 WandB Report
Includes:
Accuracy & loss curves
Hyperparameter importance
Parallel coordinate plots
Coding Style and Best Practices
Modular code structure for clarity.
Detailed comments explaining functionality.
Proper and random data splits into train/validation/test sets.
Extensive logging using WandB for reproducibility and transparency.
Results and Observations
Comprehensive experiment documentation in WandB dashboard.
Observations on optimization strategies clearly detailed in the reports.
Plagiarism Disclaimer
All code in this repository is original and written solely by the author. Proper dataset splitting was performed. No form of plagiarism or improper evaluation (e.g., data leakage) was conducted.

Author
Name: Subikksha
Roll Number: DA24D004
Institute: Indian Institute of Technology Madras (IIT Madras)
GitHub: https://github.com/SubikkshaS
You can directly copy this into your README.md file.




You said:
