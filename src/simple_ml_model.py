"""
Simple Linear Regression Model for AI BootCamp Homework
This module demonstrates basic machine learning concepts using scikit-learn.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


class SimpleMLModel:
    """A simple machine learning model for regression tasks."""
    
    def __init__(self):
        """Initialize the model."""
        self.model = LinearRegression()
        self.is_trained = False
    
    def train(self, X, y):
        """
        Train the model on the provided data.
        
        Args:
            X: Features (independent variables)
            y: Target (dependent variable)
        """
        self.model.fit(X, y)
        self.is_trained = True
        print("Model trained successfully!")
    
    def predict(self, X):
        """
        Make predictions using the trained model.
        
        Args:
            X: Features to predict on
            
        Returns:
            Predictions
        """
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions!")
        return self.model.predict(X)
    
    def evaluate(self, X, y):
        """
        Evaluate the model performance.
        
        Args:
            X: Features
            y: True values
            
        Returns:
            Dictionary containing evaluation metrics
        """
        if not self.is_trained:
            raise ValueError("Model must be trained before evaluation!")
        
        predictions = self.predict(X)
        mse = mean_squared_error(y, predictions)
        r2 = r2_score(y, predictions)
        
        return {
            'mse': mse,
            'rmse': np.sqrt(mse),
            'r2_score': r2
        }


def load_data(filepath):
    """
    Load data from a CSV file.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        pandas DataFrame
    """
    return pd.read_csv(filepath)


def prepare_data(df, target_column, test_size=0.2, random_state=42):
    """
    Prepare data for training by splitting into train and test sets.
    
    Args:
        df: pandas DataFrame
        target_column: Name of the target column
        test_size: Fraction of data to use for testing
        random_state: Random seed for reproducibility
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def plot_predictions(y_true, y_pred, title="Predictions vs Actual"):
    """
    Create a scatter plot comparing predictions with actual values.
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
        title: Plot title
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(y_true, y_pred, alpha=0.5)
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title(title)
    plt.tight_layout()
    plt.savefig('predictions_plot.png')
    print("Plot saved as 'predictions_plot.png'")


def main():
    """Main function to demonstrate the ML workflow."""
    print("=" * 50)
    print("AI BootCamp Homework - Simple ML Model Demo")
    print("=" * 50)
    
    # Generate sample data for demonstration
    print("\n1. Generating sample data...")
    np.random.seed(42)
    X = np.random.rand(100, 1) * 10
    y = 2 * X.squeeze() + 1 + np.random.randn(100) * 2
    
    # Split data
    print("2. Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Create and train model
    print("3. Training the model...")
    model = SimpleMLModel()
    model.train(X_train, y_train)
    
    # Evaluate on test set
    print("4. Evaluating the model...")
    metrics = model.evaluate(X_test, y_test)
    print(f"\nModel Performance:")
    print(f"  - RMSE: {metrics['rmse']:.4f}")
    print(f"  - R² Score: {metrics['r2_score']:.4f}")
    
    # Make predictions
    print("\n5. Making predictions on test data...")
    predictions = model.predict(X_test)
    
    # Plot results
    print("6. Creating visualization...")
    plot_predictions(y_test, predictions)
    
    print("\n" + "=" * 50)
    print("Demo completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
