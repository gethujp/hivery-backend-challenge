import pytest
from app.main import Server
server = Server('test')
# Creates a fixture whose name is "app"
# and returns our flask server instance
@pytest.fixture
def app():
    app = server.app
    return app

