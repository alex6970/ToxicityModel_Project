import pytest

from src.app import app

from flask import url_for

@pytest.fixture
def client():
    client = app.test_client()

    with app.app_context():
        pass

    app.app_context().push()
    return client

def test_index(client):
    var = client.get('/')
    assert var.status_code == 200
    
def test_unit(client):
    p = {"inputedText":"Hello World"}
    response = client.post("/",data=p)
    assert b'<li class="list-group-item">Toxicity : 0.0 </li>' in response.data
    ### mettre les autres assertions
    
def test_inte(client):
    response = client.post("/")
    assert response.data.decode('UTF-8') == open('/app/src/templates/resultsPage.html').read()
    


