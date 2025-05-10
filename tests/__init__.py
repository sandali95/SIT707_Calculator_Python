# Import the app instance to make it available to all tests
from app import app

# Optional: Add any test configuration here
import pytest

# Optional: Fixtures that should be available to all test modules
@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    with app.test_client() as client:
        yield client