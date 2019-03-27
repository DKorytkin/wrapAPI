
import pytest

from wrapapi import Application, Settings


@pytest.fixture(scope='session')
def settings() -> Settings:
    config = Settings()
    config.base_url = 'http://localhost:6543'
    config.headers['Autorization'] = 'Basic dev_shared_secret'
    return config


@pytest.fixture(scope='session')
def client(settings) -> Application:
    app = Application(settings)
    client = app.create()
    yield client
    client.close()


@pytest.fixture(scope='session')
def auth(client) -> Application:
    app.get('/api/debug/login', status=200)
    yield app


@pytest.fixture(scope='function')
def app(auth) -> Application:
    yield auth
    auth.report.build()
