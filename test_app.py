from app import app

def test_hello():
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
