# -*- coding: utf-8 -*-
import time
import requests
from main import TestCore


class GetSinglePullRequest(TestCore):

    def test_single_of_PR(self):
        url = '{base_url}pulls/{path}'.format(
            base_url=TestCore.base_url,
            path=TestCore.get_pull_request_numbers(self)[1],
        )
        for i in range(3):
            response_obj = requests.get(url)
            assert response_obj.status_code == 200, '%s != 200 Something wrong!' % response_obj.status_code
            json_resp = response_obj.json()
            mergeable_status = json_resp["mergeable"]
            if mergeable_status != 'null':
                assert type(json_resp['mergeable']) is bool, '%s != True or False, Incorrect type!' % type(json_resp['mergeable'])
            else:
                time.sleep(0.05)  # 50ms
        else:
            raise AssertionError('Run out of attemps, requested url %s mergeable_status is null' % url)
