import json
import requests


class ResponseError(Exception):
    pass


class TransferRepos:
    def __init__(self, token, username, transfer_to):
        _BASE_URL = "https://api.github.com/{ext}"

        self._username = username
        self._transfer_to = transfer_to

        self._TRANSFER_URL = _BASE_URL.format(ext="repos/{username}/{repository}/transfer")
        self._REPOSITORY_URL = _BASE_URL.format(ext="users/{username}/repos")

        self._TRANSFER_HEADERS = {
            "Accept": "application/vnd.github.nightshade-preview+json",
            "Content-Type": "application/json",
            "Authorization": "token {}".format(token)
        }

    @staticmethod
    def _validate_response(response):
        if response.status_code >= 200 and response.status_code <= 300:
            return response.text

        raise ResponseError(f"Status code out of range: {response.status_code}\n{response.text}")

    def get_repos(self):
        response = requests.get(
            self._REPOSITORY_URL.format(username=self._username)
        )

        repos = json.loads(self._validate_response(response=response))

        return (repo['name'] for repo in repos)

    def transfer_repo(self, repo):
        print(f"Making request for {repo}")

        response = requests.post(
            self._TRANSFER_URL.format(
                username=self._username,
                repository=repo
            ),
            headers=self._TRANSFER_HEADERS,
            data=json.dumps({
                "new_owner": self._transfer_to
            })
        )

        if self._validate_response(response):
            print("Success")

    def main(self, keep=None, transfer=None):
        print("Starting transfer process")

        for repo in self.get_repos():
            if keep is not None and repo in keep:
                continue

            elif transfer is not None:
                if repo in transfer:
                    self.transfer_repo(repo)

            else:
                self.transfer_repo(repo)

        print("Done")
