from app import app



def test_homepage():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 302
    assert response.location == "/login?next=%2F"

def test_shorten_url():
    url = "https://www.youtube.com"

    client = app.test_client()
    response = client.post("/login", data={
        "email": "root@example.com",
        "password": "12345678"
    })
    assert response.status_code == 302
    assert response.location == "/"

    response = client.post("/", data={
        "url": url
    })
    assert b"URL Shortener" in response.data


def test_exist_url():
    test_url="https://www.facebook.com"
    result = "cVnQDG"

    client = app.test_client()
    response = client.post("/login", data={
        "email": "root@example.com",
        "password": "12345678"
    })
    assert response.status_code == 302
    assert response.location == "/"

    response = client.post("/", data={
        "url": test_url
    })
    assert response.status_code == 200
    assert result in response.data.decode("utf-8")

def test_redirect():
    test_url="https://www.facebook.com"
    shorten_url = "cVnQDG"

    client = app.test_client()
    response = client.get(f"/{shorten_url}")
    assert response.status_code == 302
    assert response.location == test_url
