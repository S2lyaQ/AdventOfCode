import requests


def get_input():
    url = "https://adventofcode.com/2023/day/1/input"
    headers = {
        "Cookie": "session=53616c7465645f5f6958edbc6cf915e614c5ff0c57cb2b1914af92a68ea629194666b26a89a09cd1fd619cddf9c331c1953cb85ce8e497da155501a44c6c429b"
    }
    response = requests.get(url, headers=headers)
    return response


def solve_first_problem():
    response = get_input()

    if response.status_code == 200:
        data = response.text.strip().split("\n")
        answer = 0
        for line in data:
            found_numbers = list(filter(lambda x: x.isdigit(), line))
            if len(found_numbers) == 1:
                answer += int(f'{found_numbers[0]}{found_numbers[0]}')
            else:
                answer += int(f'{found_numbers[0]}{found_numbers[-1]}')
        return answer


def solve_second_problem():
    numbers_dict = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }

    response = get_input()

    if response.status_code == 200:
        modified_text = response.text
        for key in numbers_dict:
            modified_text = modified_text.replace(key, str(numbers_dict[key]))

        answer = 0
        for line in modified_text.split("\n"):
            found_numbers = list(filter(lambda x: x.isdigit(), line))
            if len(found_numbers) == 0:
                continue
            elif len(found_numbers) == 1:
                answer += int(f'{found_numbers[0]}{found_numbers[0]}')
            else:
                answer += int(f'{found_numbers[0]}{found_numbers[-1]}')
        return answer
    else:
        return f"Error: Unable to fetch data. Status code: {response.status_code}"


print(solve_first_problem())
print(solve_second_problem())
