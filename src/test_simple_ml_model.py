"""
Test suite for the Simple ML Model
"""

import numpy as np
import pytest
from simple_ml_model import SimpleMLModel, prepare_data
import pandas as pd


def test_model_initialization():
    """Test that the model initializes correctly."""
    model = SimpleMLModel()
    assert model.is_trained == False
    assert model.model is not None


def test_model_training():
    """Test that the model trains correctly."""
    model = SimpleMLModel()
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])
    
    model.train(X, y)
    assert model.is_trained == True


def test_model_prediction():
    """Test that the model makes predictions."""
    model = SimpleMLModel()
    X_train = np.array([[1], [2], [3], [4], [5]])
    y_train = np.array([2, 4, 6, 8, 10])
    
    model.train(X_train, y_train)
    
    X_test = np.array([[6], [7]])
    predictions = model.predict(X_test)
    
    assert len(predictions) == 2
    assert isinstance(predictions, np.ndarray)


def test_prediction_without_training():
    """Test that prediction fails without training."""
    model = SimpleMLModel()
    X_test = np.array([[1], [2]])
    
    with pytest.raises(ValueError, match="Model must be trained"):
        model.predict(X_test)


def test_model_evaluation():
    """Test that the model evaluation works."""
    model = SimpleMLModel()
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])
    
    model.train(X, y)
    metrics = model.evaluate(X, y)
    
    assert 'mse' in metrics
    assert 'rmse' in metrics
    assert 'r2_score' in metrics
    assert metrics['r2_score'] >= 0


def test_prepare_data():
    """Test data preparation function."""
    df = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [2, 4, 6, 8, 10],
        'target': [3, 6, 9, 12, 15]
    })
    
    X_train, X_test, y_train, y_test = prepare_data(df, 'target', test_size=0.2)
    
    assert len(X_train) == 4
    assert len(X_test) == 1
    assert len(y_train) == 4
    assert len(y_test) == 1
