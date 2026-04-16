from app import app, users

def setup_client():
    users.clear()
    return app.test_client()

# INTEGRATION TEST

def test_full_flow():
    client = setup_client()

    # register
    res = client.post("/register", json={
        "email": "user@mail.com",
        "password": "123456"
    })
    assert res.status_code == 201

    # login
    res = client.post("/login", json={
        "email": "user@mail.com",
        "password": "123456"
    })
    assert res.status_code == 200


def test_login_wrong_password():
    client = setup_client()

    client.post("/register", json={
        "email": "u@mail.com",
        "password": "123456"
    })

    res = client.post("/login", json={
        "email": "u@mail.com",
        "password": "wrong"
    })
    assert res.status_code == 401


def test_register_then_profile():
    client = setup_client()

    client.post("/register", json={
        "email": "x@mail.com",
        "password": "123456"
    })

    res = client.get("/profile")
    assert res.status_code == 200


def test_duplicate_flow():
    client = setup_client()

    client.post("/register", json={
        "email": "dup@mail.com",
        "password": "123456"
    })

    res = client.post("/register", json={
        "email": "dup@mail.com",
        "password": "123456"
    })
    assert res.status_code == 400


def test_invalid_login_after_register():
    client = setup_client()

    client.post("/register", json={
        "email": "test@mail.com",
        "password": "123456"
    })

    res = client.post("/login", json={
        "email": "test@mail.com",
        "password": "wrongpass"
    })
    assert res.status_code == 401