"""
Simple Linear Regression Model for AI BootCamp Homework (No Dependencies Version)
This module demonstrates basic machine learning concepts using only standard Python.
"""

import random
import math


class SimpleLinearRegression:
    """A simple linear regression model implemented from scratch."""
    
    def __init__(self):
        """Initialize the model."""
        self.slope = 0
        self.intercept = 0
        self.is_trained = False
    
    def train(self, X, y):
        """
        Train the model using the least squares method.
        
        Args:
            X: List of feature values
            y: List of target values
        """
        if len(X) != len(y):
            raise ValueError("X and y must have the same length")
        
        n = len(X)
        
        # Calculate means
        mean_x = sum(X) / n
        mean_y = sum(y) / n
        
        # Calculate slope and intercept
        numerator = sum((X[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = sum((X[i] - mean_x) ** 2 for i in range(n))
        
        if denominator == 0:
            raise ValueError("Cannot train model: no variance in X")
        
        self.slope = numerator / denominator
        self.intercept = mean_y - self.slope * mean_x
        self.is_trained = True
        
        print("Model trained successfully!")
        print(f"  Equation: y = {self.slope:.4f}x + {self.intercept:.4f}")
    
    def predict(self, X):
        """
        Make predictions using the trained model.
        
        Args:
            X: List of feature values or single value
            
        Returns:
            List of predictions or single prediction
        """
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions!")
        
        if isinstance(X, (int, float)):
            return self.slope * X + self.intercept
        
        return [self.slope * x + self.intercept for x in X]
    
    def evaluate(self, X, y):
        """
        Evaluate the model performance.
        
        Args:
            X: List of features
            y: List of true values
            
        Returns:
            Dictionary containing evaluation metrics
        """
        if not self.is_trained:
            raise ValueError("Model must be trained before evaluation!")
        
        predictions = self.predict(X)
        n = len(y)
        
        # Calculate Mean Squared Error
        mse = sum((y[i] - predictions[i]) ** 2 for i in range(n)) / n
        rmse = math.sqrt(mse)
        
        # Calculate R² Score
        mean_y = sum(y) / n
        ss_total = sum((y[i] - mean_y) ** 2 for i in range(n))
        ss_residual = sum((y[i] - predictions[i]) ** 2 for i in range(n))
        
        r2 = 1 - (ss_residual / ss_total) if ss_total != 0 else 0
        
        return {
            'mse': mse,
            'rmse': rmse,
            'r2_score': r2
        }


def train_test_split(X, y, test_size=0.2, random_seed=42):
    """
    Split data into training and test sets.
    
    Args:
        X: List of features
        y: List of targets
        test_size: Fraction of data to use for testing
        random_seed: Random seed for reproducibility
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    random.seed(random_seed)
    
    # Create indices and shuffle
    indices = list(range(len(X)))
    random.shuffle(indices)
    
    # Calculate split point
    split_idx = int(len(X) * (1 - test_size))
    
    # Split data
    train_indices = indices[:split_idx]
    test_indices = indices[split_idx:]
    
    X_train = [X[i] for i in train_indices]
    X_test = [X[i] for i in test_indices]
    y_train = [y[i] for i in train_indices]
    y_test = [y[i] for i in test_indices]
    
    return X_train, X_test, y_train, y_test


def main():
    """Main function to demonstrate the ML workflow."""
    print("=" * 60)
    print("AI BootCamp Homework - Simple ML Model Demo (Pure Python)")
    print("=" * 60)
    
    # Generate sample data for demonstration
    print("\n1. Generating sample data...")
    random.seed(42)
    X = [random.random() * 10 for _ in range(100)]
    y = [2 * x + 1 + random.gauss(0, 2) for x in X]
    print(f"   Generated {len(X)} data points")
    
    # Split data
    print("\n2. Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    print(f"   Training set: {len(X_train)} samples")
    print(f"   Test set: {len(X_test)} samples")
    
    # Create and train model
    print("\n3. Training the model...")
    model = SimpleLinearRegression()
    model.train(X_train, y_train)
    
    # Evaluate on test set
    print("\n4. Evaluating the model...")
    metrics = model.evaluate(X_test, y_test)
    print(f"   Model Performance:")
    print(f"   - RMSE: {metrics['rmse']:.4f}")
    print(f"   - R² Score: {metrics['r2_score']:.4f}")
    
    # Make predictions
    print("\n5. Making sample predictions...")
    test_values = [1.0, 5.0, 10.0]
    for x in test_values:
        pred = model.predict(x)
        expected = 2 * x + 1  # True relationship without noise
        print(f"   x={x:.1f} -> predicted={pred:.2f}, expected≈{expected:.2f}")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)
    print("\nNote: For advanced features, install dependencies:")
    print("  pip install -r requirements.txt")
    print("  Then run: python simple_ml_model.py")


if __name__ == "__main__":
    main()
