# -*- coding: utf-8 -*-
import unittest
import requests


class TestCore (unittest.TestCase):

    headers = {'User-Agent': 'http://developer.github.com/v3/#user-agent-required',
               'Accept': 'application/vnd.github.symmetra-preview+json',
               'Content-Type': 'application/json'}
    access_token = 'access_token=380a049e1c8afdaf662141e6023a9e9001a9a241'
    base_url = 'https://api.github.com/repos/{owner}/{repo}/'.format(
        owner='octocat',
        repo='Hello-World'
    )

    def get_list_of_pull_requsts(self):
        response_obj_page = [(requests.get(self.base_url + 'pulls?page=%s' % i)) for i in range(1, 6)]
        list_of_pull_request = []
        for i in range(5):
            list_of_pull_request += response_obj_page[i].json()
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
