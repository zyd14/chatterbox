import pytest

@pytest.fixture
def client_app():
    import src.app as app_module
    app_module.app.config['TESTING'] = True
    yield app_module.app.test_client()
