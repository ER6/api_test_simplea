# -*- coding: utf-8 -*-
import unittest
import requests


class TestCore (unittest.TestCase):

    headers = {'User-Agent': 'http://developer.github.com/v3/#user-agent-required',
               'Accept': 'application/vnd.github.symmetra-preview+json',
               'Content-Type': 'application/json'}

    owner = 'octocat/'
    repo = 'Hello-World/'
    base_url = 'https://api.github.com/repos/' + owner + repo

    def get_list_of_pull_requsts(self):
        response_obj_page1 = requests.get(self.base_url + 'pulls?page=1')
        response_obj_page2 = requests.get(self.base_url + 'pulls?page=2')
        response_obj_page3 = requests.get(self.base_url + 'pulls?page=3')
        response_obj_page4 = requests.get(self.base_url + 'pulls?page=4')
        response_obj_page5 = requests.get(self.base_url + 'pulls?page=5')
        list_of_pull_request_page1 = response_obj_page1.json()
        list_of_pull_request_page2 = response_obj_page2.json()
        list_of_pull_request_page3 = response_obj_page3.json()
        list_of_pull_request_page4 = response_obj_page4.json()
        list_of_pull_request_page5 = response_obj_page5.json()
        list_of_pull_request = list_of_pull_request_page1+list_of_pull_request_page2+list_of_pull_request_page3+list_of_pull_request_page4+list_of_pull_request_page5
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
