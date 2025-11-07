# Maktab Sharif - AI BootCamp Homework

This repository contains homework assignments for the AI BootCamp program. The project demonstrates fundamental machine learning concepts using Python and scikit-learn.

## 📚 Project Overview

This project implements a simple machine learning model for regression tasks, showcasing:
- Data loading and preprocessing
- Model training and evaluation
- Predictions and visualization
- Unit testing

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager) - optional for advanced features

### Quick Start (No Installation Required)

The project includes a pure Python implementation that works without any external dependencies:

```bash
cd src
python simple_ml_basic.py
```

Run tests:
```bash
cd src
python test_simple_ml_basic.py
```

### Advanced Setup (Optional)

For enhanced features with scikit-learn, pandas, and matplotlib:

1. Clone the repository:
```bash
git clone https://github.com/rezarabie/maktabsharif.git
cd maktabsharif
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Version (No Dependencies)

The basic implementation (`simple_ml_basic.py`) is a pure Python implementation of linear regression:

```bash
cd src
python simple_ml_basic.py
```

This will:
1. Generate sample data
2. Split data into training and test sets
3. Train a linear regression model from scratch
4. Evaluate the model's performance
5. Make sample predictions

### Advanced Version (With scikit-learn)

If you have installed the dependencies, you can run the advanced demo:

```bash
cd src
python simple_ml_model.py
```

This will:
1. Generate sample data
2. Split data into training and test sets
3. Train a linear regression model
4. Evaluate the model's performance
5. Create a visualization of predictions vs actual values

### Using with Your Own Data

**Basic Version:**

```python
from simple_ml_basic import SimpleLinearRegression, train_test_split

# Your data
X = [1.5, 2.3, 3.1, 4.2, 5.0]
y = [3.2, 4.8, 6.3, 8.5, 10.1]

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = SimpleLinearRegression()
model.train(X_train, y_train)

# Evaluate and predict
metrics = model.evaluate(X_test, y_test)
print(f"R² Score: {metrics['r2_score']:.4f}")
predictions = model.predict([6.0, 7.0])
```

**Advanced Version (with dependencies installed):**

You can use the model with your own CSV data:

```python
from simple_ml_model import SimpleMLModel, load_data, prepare_data

# Load your data
df = load_data('../data/sample_data.csv')

# Prepare data
X_train, X_test, y_train, y_test = prepare_data(df, 'target')

# Create and train model
model = SimpleMLModel()
model.train(X_train, y_train)

# Evaluate
metrics = model.evaluate(X_test, y_test)
print(f"R² Score: {metrics['r2_score']:.4f}")

# Make predictions
predictions = model.predict(X_test)
```

## 🧪 Running Tests

### Basic Version Tests

```bash
cd src
python test_simple_ml_basic.py
```

### Advanced Version Tests (requires pytest)

To run the test suite with pytest:

```bash
cd src
pytest test_simple_ml_model.py -v
```

Or install pytest first if not already installed:
```bash
pip install pytest
pytest test_simple_ml_model.py -v
```

## 📁 Project Structure

```
maktabsharif/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies (optional)
├── .gitignore                  # Git ignore rules
├── data/                       # Data directory
│   └── sample_data.csv         # Sample dataset
└── src/                        # Source code
    ├── simple_ml_basic.py      # Basic ML model (no dependencies)
    ├── test_simple_ml_basic.py # Tests for basic version
    ├── simple_ml_model.py      # Advanced ML model (requires sklearn)
    └── test_simple_ml_model.py # Tests for advanced version
```

## 📊 Model Details

### Basic Implementation (simple_ml_basic.py)

A pure Python implementation of linear regression using the least squares method:
- **No external dependencies required**
- **Training**: Implements the mathematical formula for linear regression
- **Prediction**: Uses the learned equation y = mx + b
- **Evaluation**: Calculates MSE, RMSE, and R² score from scratch

### Advanced Implementation (simple_ml_model.py)

The `SimpleMLModel` class provides a scikit-learn-based interface for:
- **Training**: Fit a linear regression model to your data
- **Prediction**: Make predictions on new data
- **Evaluation**: Calculate performance metrics (MSE, RMSE, R²)

### Features

- Easy-to-use API for beginners
- Comprehensive error handling
- Visualization support
- Unit tests for reliability

## 🎓 Learning Objectives

This homework demonstrates:
1. **Data Handling**: Loading and preparing data for machine learning
2. **Model Training**: Using scikit-learn to train a regression model
3. **Evaluation**: Understanding model performance metrics
4. **Visualization**: Creating plots to understand model behavior
5. **Testing**: Writing unit tests for ML code

## 📝 License

This project is for educational purposes as part of the AI BootCamp program.

## 👤 Author

Reza Rabie (@rezarabie)

## 🤝 Contributing

This is a homework project. If you're a fellow student and want to discuss approaches, feel free to open an issue!

## 📧 Contact

For questions or feedback, please open an issue in this repository.