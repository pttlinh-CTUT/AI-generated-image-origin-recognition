# Dual-Stream Framework for Real/Fake Classification and Source Attribution of AI-Generated Images using Spatial and Frequency Features

This project implements a Deep Learning model to classify images as **Real** or **Fake** (Generated). The model utilizes a **Dual-Stream Architecture**, combining information from both the **Spatial domain** (RGB images) and the **Frequency domain** (spectrum analysis) to detect subtle artifacts often missed by traditional CNNs.

## Key Features
- **Dual-Stream Network:** Processes `spatial_x` (RGB) and `freq_x` (Frequency spectrum) inputs simultaneously using a two-branch architecture.
- **Optimized Pipeline:** Implements PyTorch `DataLoader` for efficient batch processing.
- **Robust Evaluation:** Includes detailed `classification_report`, `confusion_matrix`, and accuracy metrics.
- **GPU Acceleration:** Automatic CUDA support with Mixed Precision training (`torch.amp.autocast`) for faster performance.

## 📂 Project Structure
```text
my-project/
├── data/                  # Data directory (Ignored by .gitignore)
├── download_data.py       # Script to automatically download the dataset
├── main.ipynb             # Main Jupyter Notebook for training & evaluation
├── .gitignore             # Git configuration to ignore large files
├── LICENSE                # MIT License file
└── README.md              # Project documentation
```

## 🛠 Requirements
Ensure you have Python 3.x installed. Install the required dependencies using pip:
```text
  pip install torch torchvision torchaudio
  pip install numpy pandas scikit-learn matplotlib tqdm gdown
```

## 💾 Dataset Setup
Due to the large size of the dataset (~2.4GB), the data is hosted externally on Google Drive and is not included directly in this repository.

  - Option 1: Automated Download (Local / Colab)
If you are running this locally or on Google Colab, use the provided script to download and extract the dataset automatically:
```text
python download_data.py
This script will fetch the dataset from Google Drive and extract it into the data/ directory.
```
  - Option 2: Kaggle Notebooks
If you are running main.ipynb on Kaggle, do not download the data. Instead, mount it directly via Google Drive:
    + Go to File -> Add Input.
    + Select the Google Drive tab.
    + Search for your dataset file/folder and click Add.

## ▶️ Usage
- Open main.ipynb using Jupyter Notebook, Google Colab, or Kaggle.
- Workflow:
    + Import Libraries: Set up PyTorch, Scikit-learn, and helper modules.
    + Data Loading: The script loads images from the data/ directory.
    + Model Initialization: Defines the Dual-Stream architecture.
    + Training: Trains the model using CrossEntropyLoss.
    + Evaluation: Runs validation on the Test set and outputs metrics.

## 📊 Results
(To be updated after training)
- Binary Classification Report:
  + Class 0: Real
  + Class 1: Fake
- Confusion Matrix: (See the output cell at the end of the notebook)

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
