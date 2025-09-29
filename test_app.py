from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"I'm once again trying" in res.data
