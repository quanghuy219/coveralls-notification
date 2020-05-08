def test_api(client):
    rv = client.get('/')
    assert b'Hello World' in rv.data
