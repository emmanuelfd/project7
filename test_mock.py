import requests
import requests_mock
import module as script



def mock_requests(results):

    session = requests.Session()
    adapter = requests_mock.Adapter()
    session.mount('mock', adapter)
    adapter.register_uri('GET', 'mock://test.com', json=results)
    resp = session.get('mock://test.com')
    return resp

#testing pageid from wiki
def test_wikimedia_return_page_id(monkeypatch):
    results = {"batchcomplete": "true", "continue": {"sroffset": 10, "continue": "-||revisions"},
                "query": {"searchinfo": {"totalhits": 15622}, "search": [
                    {"ns": 0, "title": "Dijon", "pageid": 3235267, "timestamp": "2018-11-19T11:49:51Z"}]}}

    def mockreturn(request):
        return mock_requests(results)

    monkeypatch.setattr(requests, 'get', mockreturn)

    x = script.wikipedia(results)

    assert x.Pageid == 3235267



