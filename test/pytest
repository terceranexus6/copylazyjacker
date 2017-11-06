import Flask
import connexion

flask_app = connexion.FlaskApp(__name__)

def test_health:
    response = get('/index.html')
    assert response.status_code == 200
