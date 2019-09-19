import pytest

@pytest.fixture
def client_app():
    from src.setup_app import sleepyapp
    api = sleepyapp.get_api()
    api.testing = True
    from src.app import tie_resources
    #tie_resources(api)
    yield sleepyapp.get_api().app.test_client()
