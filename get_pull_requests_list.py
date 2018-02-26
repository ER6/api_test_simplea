import requests
from nose_parameterized import parameterized
from main import TestCore

test_parameters = {
    "state": ['closed', 'open', 'all'],
    "head": ['sergeypyrkin:master', 'smassy:comma', 'Wasapon7763:patch-1'], # didn't work for user akhileswar
    "base": ['test', 'master', 'patch-3'],
    "sort": ['created', 'updated', 'popularity', 'long-running'],
    "direction": ['asc', 'desc']
}

class GetPullRequestList(TestCore):
    url = TestCore.base_url + 'pulls'

    @parameterized.expand(test_parameters["state"])
    def test_state_parameter(self, state):
        response_obj = requests.get(self.url, headers=self.headers, params={'state': state})
        list_of_pull_requests = response_obj.json()
        list_of_states = [i["state"] for i in list_of_pull_requests if i['state'] is str]  # do we need this check?
        uniq_list = list(set(list_of_states))
        assert response_obj.status_code == 200, '%s != 200 Something wrong!' % response_obj.status_code
        if state == 'closed':
            for i in list_of_states:
                assert i == 'closed', '%s != %s, Incorrect state of getting pull request!' % (i, state)
        if state == 'open':
            for i in list_of_states:
                assert i == 'open', '%s != %s, Incorrect state of getting pull request!' % (i, state)
        if state != 'all':
            for i in list_of_states:
                assert uniq_list != 2
                assert i == 'open' or i == 'closed', '%s != %s, Incorrect state of getting pull request!' % (i, state)

    @parameterized.expand(test_parameters["head"])
    def test_head_parameter(self, head):
        response_obj = requests.get(self.url, headers=self.headers, params={'head': head})
        list_of_pull_requests = response_obj.json()
        assert len(list_of_pull_requests) != 0, "Nothing to show"
        assert response_obj.status_code == 200, '%s != 200 Something wrong!' % response_obj.status_code
        assert list_of_pull_requests[0]["head"]["label"] == head, '%s != %s wrong request param!' % (list_of_pull_requests[0]["head"]["label"], head)

    @parameterized.expand(test_parameters["base"])
    def test_base_parameter(self, base):
        response_obj = requests.get(self.url, headers=self.headers, params={'base': base})
        list_of_pull_requests = response_obj.json()
        assert response_obj.status_code == 200, '%s != 200 Something wrong!' % response_obj.status_code
        for i in list_of_pull_requests:
            assert i["base"]["ref"] == base, '%s != %s Wrong branch in list for id = %d!' % (i["head"]["ref"], base, i["id"])

    @parameterized.expand(test_parameters["sort"])
    def test_sort_parameter(self, sort):
        response_obj = requests.get(self.url, headers=self.headers, params={'sort': sort})
        list_of_pull_requests = response_obj.json()
        assert response_obj.status_code == 200, '%s != 200 Something wrong!' % response_obj.status_code
        if sort == 'created':
            list_of_creating_dates = [i["created_at"] for i in list_of_pull_requests]
            sorted_list_of_creating_dates = sorted(list_of_creating_dates)
            assert list_of_creating_dates == sorted_list_of_creating_dates, "Sort by 'Created_date' doesn't work"
        if sort == 'updated':
            list_of_updating_dates = [i["updated_at"] for i in list_of_pull_requests]
            sorted_list_of_updating_dates = sorted(list_of_updating_dates)
            assert list_of_updating_dates == sorted_list_of_updating_dates, "Sort by 'Created_date' doesn't work"
        # if sort == 'popularity':
        #     list_of_urls_of_pull_requests = [i["url"] for i in list_of_pull_requests]  ## to many requests
        #     for i in list_of_urls_of_pull_requests:
        #         new_obj = requests.get(i)
        #         new_json = new_obj.json()

    @parameterized.expand(test_parameters["direction"])
    def test_direction_parameter(self, direction):
        response_obj = requests.get(self.url, headers=self.headers, params={'direction': direction})
        list_of_pull_requests = response_obj.json()
        assert response_obj.status_code == 200, '%s != 200 Something wrong!' % response_obj.status_code
        list_of_creating_dates = [i["created_at"] for i in list_of_pull_requests]
        sorted_list_of_creating_dates = sorted(list_of_creating_dates)
        reversed_list_of_creating_dates = sorted(list_of_creating_dates, reverse=True)
        if direction == 'desk':
            assert list_of_creating_dates == sorted_list_of_creating_dates, "Sort by 'Created_date' doesn't work"
        if direction == 'asc':
            print(list_of_creating_dates)
            print(reversed_list_of_creating_dates)
            assert list_of_creating_dates == reversed_list_of_creating_dates, "Sort by 'Created_date' doesn't work"
