import allure
import pytest

from api.api_client import ApiClient

@allure.feature("API smoke tests")
@pytest.mark.api
def test_me_successfully(api_client):
    with allure.step("get user data"):
        response = api_client.get("/api/public/v1/me")
    
    allure.attach(
        body=response.text,
        name="Response Body",
        attachment_type=allure.attachment_type.JSON
    )

    assert response.status_code == 200
    body = response.json()
    assert body["profile"]["email"]== "user01@gmail.com"
    assert body["profile"]["display_name"] == "user01"

@allure.feature("API smoke tests")
@pytest.mark.api
def test_me_unsuccessfully_with_bad_api_key():
    with allure.step("get user data"):
        api_client = ApiClient(
                base_url="https://project--ac0e6745-4110-4788-8049-64a6a057c641.lovable.app",
                headers={
                    "X-API-Key": "xx_v2FlavslE58NB62WZG8Vycpm0VhBGdt0"
                }
        )
        response = api_client.get("/api/public/v1/me")
    
    allure.attach(
        body=response.text,
        name="Response Body",
        attachment_type=allure.attachment_type.JSON
    )

    assert response.status_code == 401

@allure.feature("API smoke tests")
@pytest.mark.api
def test_view_events(api_client):
    with allure.step("get events data"):
        response = api_client.get("/api/public/v1/events")
    
    allure.attach(
        body=response.text,
        name="Response Body",
        attachment_type=allure.attachment_type.JSON
    )

    assert response.status_code == 200
    body = response.json()
    # get size of items in the response body
    psize = len(body["items"])
    assert body["page_size"] == psize