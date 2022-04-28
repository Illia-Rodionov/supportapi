from django.urls import reverse
import pytest


from authentication.models import User
from authentication.serializers import UserCreateUpdateSerializer


pytestmark = pytest.mark.django_db


def test_user_create_invalid(client, create_user_url):
    url = create_user_url
    response = client.post(url, {})

    assert response.status_code == 400


def test_user_create(client, create_user_url):
    url = create_user_url
    payload = {
        "id": 1,
        "username": "admin",
        "email": "admin@admin.ru",
        "password": "12345",
    }
    response = client.post(url, payload)
    user = User.objects.first()
    expected_response = UserCreateUpdateSerializer(user).data

    assert response.status_code == 201
    assert User.objects.count() == 1
    assert response.data == expected_response
