from app import app, users

def setup_client():
    users.clear()  # reset data sebelum test
    return app.test_client()


# REGISTER TEST

def test_register_success():
    client = setup_client()
    res = client.post("/register", json={"email": "a@mail.com", "password": "123456"})
    assert res.status_code == 201

def test_register_empty():
    client = setup_client()
    res = client.post("/register", json={})
    assert res.status_code == 400

def test_register_no_email():
    client = setup_client()
    res = client.post("/register", json={"password": "123456"})
    assert res.status_code == 400

def test_register_no_password():
    client = setup_client()
    res = client.post("/register", json={"email": "a@mail.com"})
    assert res.status_code == 400

def test_password_too_short():
    client = setup_client()
    res = client.post("/register", json={"email": "b@mail.com", "password": "123"})
    assert res.status_code == 400

def test_duplicate_email():
    client = setup_client()
    client.post("/register", json={"email": "c@mail.com", "password": "123456"})
    res = client.post("/register", json={"email": "c@mail.com", "password": "123456"})
    assert res.status_code == 400

def test_register_whitespace_email():
    client = setup_client()
    res = client.post("/register", json={"email": " ", "password": "123456"})
    assert res.status_code == 400
    
def test_register_invalid_email():
    client = setup_client()
    res = client.post("/register", json={"email": "invalidemail", "password": "123456"})
    assert res.status_code == 400

def test_register_long_password():
    client = setup_client()
    res = client.post("/register", json={"email": "long@mail.com", "password": "123456789"})
    assert res.status_code == 201


# LOGIN TEST

def test_login_success():
    client = setup_client()
    client.post("/register", json={"email": "d@mail.com", "password": "123456"})
    res = client.post("/login", json={"email": "d@mail.com", "password": "123456"})
    assert res.status_code == 200

def test_login_fail_wrong_password():
    client = setup_client()
    client.post("/register", json={"email": "e@mail.com", "password": "123456"})
    res = client.post("/login", json={"email": "e@mail.com", "password": "wrong"})
    assert res.status_code == 401

def test_login_no_user():
    client = setup_client()
    res = client.post("/login", json={"email": "none@mail.com", "password": "123456"})
    assert res.status_code == 401

def test_login_empty_data():
    client = setup_client()
    res = client.post("/login", json={})
    assert res.status_code == 401

def test_login_case_sensitive():
    client = setup_client()
    client.post("/register", json={"email": "case@mail.com", "password": "123456"})
    res = client.post("/login", json={"email": "CASE@mail.com", "password": "123456"})
    assert res.status_code == 401

# PROFILE TEST

def test_profile_empty():
    client = setup_client()
    res = client.get("/profile")
    assert res.status_code == 200

def test_profile_after_register():
    client = setup_client()
    client.post("/register", json={"email": "z@mail.com", "password": "123456"})
    res = client.get("/profile")
    assert res.status_code == 200