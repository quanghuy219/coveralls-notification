import pytest

from app import app as _app


@pytest.fixture
def client():
    """A test client for the app."""
    with _app.test_client() as client:
        yield client
