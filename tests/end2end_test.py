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

##############
# We want here to test the application end to end
# Firstly we will test the home page
# our goal is to find the exact same sentences in the home page that we expect to have
##############

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the homepage' in response.data
    assert b'Toxicity Monitoring' in response.data
    assert b'Type something and a see if it is toxic or not.' in response.data

##############
# Now we will test the result after submitting the following sentence : 
# Hello, my name is Goldy and i want to say to you that i appreciate the fact you are an asshole.
# We expect to find the same page as the one we tested
##############

def test_resultpage(client):
    p = {"inputedText":"Hello, my name is Goldy and i want to say to you that i appreciate the fact you are an asshole."}
    response = client.post('/', data=p)
    assert response.status_code == 200
    

    ######## Webapp Build Test ###########
    assert b'Welcome to the results page.' in response.data
    assert b'The text you submitted is :' in response.data
    assert b'Hello, my name is Goldy and i want to say to you that i appreciate the fact you are an asshole.' in response.data

    ######## Results Values Tests ##########
    assert b'Toxicity : 0.93 ' in response.data 
    assert b'Severe Toxicity : 0.03 ' in response.data
    assert b'Obscene : 0.84' in response.data
    assert b'Threat : 0.0' in response.data
    assert b'Insult : 0.82' in response.data
    assert b'Identity attack : 0.01' in response.data

    
