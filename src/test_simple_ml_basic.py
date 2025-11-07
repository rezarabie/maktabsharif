"""
Test suite for the Simple ML Model (Basic Version)
Run with: python test_simple_ml_basic.py
"""

from simple_ml_basic import SimpleLinearRegression, train_test_split


def test_model_initialization():
    """Test that the model initializes correctly."""
    model = SimpleLinearRegression()
    assert model.is_trained == False
    assert model.slope == 0
    assert model.intercept == 0
    print("✓ Model initialization test passed")


def test_model_training():
    """Test that the model trains correctly."""
    model = SimpleLinearRegression()
    X = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    
    model.train(X, y)
    assert model.is_trained == True
    assert abs(model.slope - 2.0) < 0.01  # Should be close to 2
    assert abs(model.intercept - 0.0) < 0.01  # Should be close to 0
    print("✓ Model training test passed")


def test_model_prediction():
    """Test that the model makes predictions."""
    model = SimpleLinearRegression()
    X_train = [1, 2, 3, 4, 5]
    y_train = [2, 4, 6, 8, 10]
    
    model.train(X_train, y_train)
    
    # Test single prediction
    pred_single = model.predict(6)
    assert abs(pred_single - 12.0) < 0.01
    
    # Test multiple predictions
    predictions = model.predict([6, 7])
    assert len(predictions) == 2
    print("✓ Model prediction test passed")


def test_prediction_without_training():
    """Test that prediction fails without training."""
    model = SimpleLinearRegression()
    
    try:
        model.predict([1, 2])
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "must be trained" in str(e)
    print("✓ Prediction without training test passed")


def test_model_evaluation():
    """Test that the model evaluation works."""
    model = SimpleLinearRegression()
    X = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    
    model.train(X, y)
    metrics = model.evaluate(X, y)
    
    assert 'mse' in metrics
    assert 'rmse' in metrics
    assert 'r2_score' in metrics
    assert metrics['mse'] < 0.01  # Should be very low for perfect fit
    assert metrics['r2_score'] > 0.99  # Should be very high for perfect fit
    print("✓ Model evaluation test passed")


def test_train_test_split():
    """Test data splitting function."""
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    assert len(X_train) == 8
    assert len(X_test) == 2
    assert len(y_train) == 8
    assert len(y_test) == 2
    print("✓ Train-test split test passed")


def run_all_tests():
    """Run all tests."""
    print("Running tests for Simple ML Model (Basic Version)")
    print("=" * 50)
    
    try:
        test_model_initialization()
        test_model_training()
        test_model_prediction()
        test_prediction_without_training()
        test_model_evaluation()
        test_train_test_split()
        
        print("=" * 50)
        print("All tests passed! ✓")
        return True
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
