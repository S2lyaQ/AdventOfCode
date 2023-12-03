from functools import reduce
from math import inf

import requests
import re


def get_input():
    day = 2
    url = f'https://adventofcode.com/2023/day/{day}/input'
    headers = {
        "Cookie": "session=53616c7465645f5f6958edbc6cf915e614c5ff0c57cb2b1914af92a68ea629194666b26a89a09cd1fd619cddf9c331c1953cb85ce8e497da155501a44c6c429b"
    }
    response = requests.get(url, headers=headers)

    return response


def solve_first_problem():
    data = get_input()
    game_id = 0
    valid_ids = set()

    if data.status_code == 200:

        for line in data.text.strip().split("\n"):

            game_id += 1
            validity = True

            for cubes_set in line.split(";"):

                available_cubes = {
                    'red': 12,
                    'green': 13,
                    'blue': 14
                }

                result = re.findall(pattern=r'\d+ \w+', string=cubes_set)

                for element in result:
                    quantity, color = element.split(" ")
                    available_cubes[color] -= int(quantity)
                    if available_cubes[color] < 0:
                        validity = False
            if validity is True:
                valid_ids.add(game_id)

        return sum(list(valid_ids))


def solve_second_problem():
    data = get_input()
    answer = 0

    if data.status_code == 200:

        for line in data.text.strip().split("\n"):

            cubes = {
                "red": float(-inf),
                "blue": float(-inf),
                "green": float(-inf)

            }
            for cubes_set in line.split(";"):

                result = re.findall(pattern=r'\d+ \w+', string=cubes_set)

                for element in result:
                    quantity, color = element.split(" ")
                    if cubes[color] < int(quantity):
                        cubes[color] = int(quantity)
            to_be_added = reduce(lambda x, y: x * y, cubes.values(), 1)
            answer += to_be_added

    return answer


print(solve_first_problem())
print(solve_second_problem())
