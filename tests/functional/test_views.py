

def test_home_page(news_api_mock_client):
    """
    GIVEN a Flask application configured for testing, user not logged in
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """

    response = news_api_mock_client.get('/')
    assert response.status_code == 200
    assert b"Yahoo Entertainment" in response.data
    assert b"DeepSeek AI assistant" in response.data
    assert b"DeepSeek has become the top rated free app" in response.data

 
