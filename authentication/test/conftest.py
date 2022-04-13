from django.urls import reverse
import pytest
from config.settings import AUTH_USER_MODEL


@pytest.fixture
def create_user_url() -> str:
    return reverse("authtentication:create_user")
