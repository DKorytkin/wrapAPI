
import pytest

from wrapapi import web


@pytest.fixture()
def app() -> web.AppRequest:
    return web.Application().create()


def test_one(app):
    response = app.get('/health')
    response.status.should.be(200)

    response.json.should.has('key')
    response.json.should.has.dict({'key': 'value'})
    response.json.should.has.key('key')
    response.json.should.has.value('value')

    response.json.should.be.equal({'status': True})
    response.json.should.be.not_equal({'status': False})

    response.json.should.be.less(2)
    response.json.should.be.less_or_equal(2)
    response.json.should.be.greater(2)
    response.json.should.be.greater_or_equal(2)

    response.json.should.be.is_not([])


def test_two(app):
    app.get('/health')\
        .status.should.be(200)\
        .json.should.has('key')\
        .json.should.has.dict({'key': 'value'})\
        .json.should.has.key('key')\
        .json.should.has.value('value')
