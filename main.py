# -*- coding: utf-8 -*-
import unittest
import requests


class TestCore (unittest.TestCase):

    headers = {'User-Agent': 'http://developer.github.com/v3/#user-agent-required',
               'Accept': 'application/vnd.github.symmetra-preview+json',
               'Content-Type': 'application/json'}
    access_token = 'access_token=380a049e1c8afdaf662141e6023a9e9001a9a241'
    base_url = 'https://api.github.com/repos/{owner}/{repo}'.format(
        owner='octocat',
        repo='Hello-World'
    )

    def paginator(self, url, pages=int):
        list_of_responces = []
        for i in range(1, pages+1):
            response_obj = requests.get(url + '?page=%s' % i)
            response = response_obj.json()
            assert response_obj.status_code == 200, '%s != 200 Something wrong!' % response_obj.status_code
            if len(response) == 0:
                break
            else:
                list_of_responces += response
        return list_of_responces

    def get_list_of_pull_requsts(self):
        pull_request_url = "%s/pulls" % self.base_url
        list_of_pull_request = self.paginator(pull_request_url, 5)
        return list_of_pull_request

    def get_pull_request_numbers(self):
        list_of_pull_request = self.get_list_of_pull_requsts()
        numbers_of_pull_requests = [i["number"] for i in list_of_pull_request]
        return numbers_of_pull_requests

    def get_list_of_users(self):
        list_of_pull_request = self.get_list_of_pull_requsts()
        list_of_users = list(set([i["user"]["login"] for i in list_of_pull_request]))
        return list_of_users

    def get_list_of_branches(self):
        list_of_pull_request = self.get_list_of_pull_requsts()
        list_of_branches = list(set([i["head"]["ref"] for i in list_of_pull_request]))
        return list_of_branches

    def get_list_of_commits(self, author=""):
        url = "%s/commits" % self.base_url
        list_of_commits = self.paginator(url, 5)
        return list_of_commits
