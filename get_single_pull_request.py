import requests
from nose_parameterized import parameterized
from main import TestCore


class GetSinglePullRequest(TestCore):
    url = TestCore.base_url + 'pulls/1347'

    @parameterized.expand(['true', 'false', 'null'])
    def test_mergiable(self, state):
        response_obj = requests.get(self.url, headers=self.headers)
        json_resp = response_obj.json()
        # if state != 'null':
        #     assert json_resp[0]['mergeable'] == state, '%s != %s, Incorrect state of getting pull request!' % (json_resp[0]['state'],state)
        #     return self.test_test_type_and_status()
        # assert type(json_resp[0]['mergeable']) is bool, '%s != str, Incorrect type!' % type(json_resp[0]['state'])
        # assert response_obj.status_code == 200, '%s != 200 Something wrong!' % response_obj.status_code