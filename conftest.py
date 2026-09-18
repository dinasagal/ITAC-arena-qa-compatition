from playwright.sync_api import Page
import pytest
import os
from dotenv import load_dotenv
from api.api_client import ApiClient

load_dotenv()

@pytest.fixture(scope="session")
def base_url() -> str:
    url = os.getenv("BASE_URL")

    if not url:
        raise RuntimeError("BASE_URL is not set")

    return url

@pytest.fixture
def api_client():
    return ApiClient(
        base_url="https://project--ac0e6745-4110-4788-8049-64a6a057c641.lovable.app",
        headers={
            "X-API-Key": "ak_v2FlavslE58NB62WZG8Vycpm0VhBGdt0"
        }
    )