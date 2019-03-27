

def test_one(app):
    response = app.get('/api/services', status=200)
    response.json.should.be.is_instance(list)


def test_two(app):
    response = app.get('/api/services/1', status=200)
    response.json.should.be.equal({'id': 9, 'name': 'Voice', 'slug': 'SERVICE_VOICE'})
