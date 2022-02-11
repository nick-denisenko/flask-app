from app import app

def test_get_hello():
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200


def test_get_new():
    with app.test_client() as test_client:
        response = test_client.get('/new')
        assert response.status_code == 200
