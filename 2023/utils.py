import requests

def scrap_input(day):

    url = f'https://adventofcode.com/2023/day/{day}/input'
    headers = {
        "Cookie": "session=53616c7465645f5f29f6b6ef09489e18587511951aaa10b3747ac0b1b8f6660a5010b8bbad728879f3368302ad09e311dace83f0612f8c318363ba1f6974fcde"
    }

    return requests.get(url, headers=headers)