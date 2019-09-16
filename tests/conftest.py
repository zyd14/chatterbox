import pytest

@pytest.fixture
def client_app():
    from src import app
    app.app.config['TESTING'] = True
    test_client = app.app.test_client()
    return test_client