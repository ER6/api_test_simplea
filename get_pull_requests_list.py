import requests
import unittest
from nose_parameterized import parameterized

from main import TestCore


class GetPullRequestList(TestCore):
    url = TestCore.base_url + 'octocat/Hello-World/pulls'

    @parameterized.expand(['closed', 'open', 'all'])
    def test_test_type_and_status(self, state):
        response_obj = requests.get(self.url, headers=self.headers, params={'state': state})
        json_resp = response_obj.json()
        if state != 'all':
            assert json_resp[0]['state'] == state, '%s != %s, Incorrect state of getting pull request!' % (json_resp[0]['state'],state)
        assert type(json_resp[0]['state']) is unicode or str, '%s != str, Incorrect type!' % type(json_resp[0]['state'])
        assert response_obj.status_code == 200, '%s != 200 Something wrong!' % response_obj.status_code