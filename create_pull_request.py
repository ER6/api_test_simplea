# -*- coding: utf-8 -*-
from nose_parameterized import parameterized
import requests
from main import TestCore

data = {'one way': [{
            "title": "Amazing new feature",
            "body": "Please pull this in!",
            "head": "octocat:new-feature",
            "base": "master"
            }],
        'second way': [{
            "issue": 5,
            "head": "octocat:new-feature",
            "base": "master"
            }]}


class CreatePullRequest(TestCore):

    @parameterized.expand([data["one way"], data["second way"]])
    def test_create_PR(self, form):
        url = '{base_url}pulls?{access_token}'.format(
            base_url = self.base_url,
            access_token=self.access_token
        )
        create_pull_request = requests.post(url, data=form)
        print(create_pull_request)
        assert create_pull_request.status_code == 201, "code is wrong"
