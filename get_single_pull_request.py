import requests
from nose_parameterized import parameterized
from main import TestCore


class GetSinglePullRequest(TestCore):

    @parameterized.expand(['true', 'false', 'null'])
    def test_mergiable(self, state):
        url = TestCore.base_url + 'pulls/' + TestCore.get_pull_request_numbers(self)[1]
        response_obj = requests.get(url, headers=self.headers)
        json_resp = response_obj.json()
        if state != 'null':
            assert json_resp[0]['mergeable'] == state, '%s != %s, Incorrect state of getting pull request!' % (json_resp[0]['state'],state)
            return self.test_mergiable()
        assert type(json_resp[0]['mergeable']) is bool, '%s != str, Incorrect type!' % type(json_resp[0]['state'])
        assert response_obj.status_code == 200, '%s != 200 Something wrong!' % response_obj.status_code
