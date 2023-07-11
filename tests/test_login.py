from app import app

def test_login():
    client = app.test_client()
    response = client.post("/login", data={
        "email": "root@example.com",
        "password": "12345678"
    })
    assert response.status_code == 302
    assert response.location == "/"
