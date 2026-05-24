from app import app

def test_home_route():
    # Create a test client for the Flask app
    client = app.test_client()
    response = client.get('/')
    
    # Assert that the page loads successfully
    assert response.status_code == 200
    assert b"DevOps Weather API" in response.data