from django.urls import reverse
import pytest


@pytest.fixture
def create_user_url() -> str:
    return reverse("authentication:create_user")
