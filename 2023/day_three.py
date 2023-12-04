import requests


def get_input():
    day = 3
    url = f'https://adventofcode.com/2023/day/{day}/input'
    headers = {
        "Cookie": "session=53616c7465645f5f6958edbc6cf915e614c5ff0c57cb2b1914af92a68ea629194666b26a89a09cd1fd619cddf9c331c1953cb85ce8e497da155501a44c6c429b"
    }
    response = requests.get(url, headers=headers)

    return response


def solve_first_problem():
    data = get_input()
    answer = 0

    if data.status_code == 200:
        matrix = [list(line) for line in data.text.strip().split("\n")]
        digits = []
        valid = False

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j].isdigit():
                    digits.append(matrix[i][j])
                    for a in range(-1, 2):
                        for b in range(-1, 2):
                            if 0 <= i + a < len(matrix) and 0 <= j + b < len(matrix[i]) and matrix[i + a][j + b] not in '0123456789.':
                                valid = True
                                break
                else:
                    if valid:
                        answer += int("".join(digits))
                        valid = False
                    digits.clear()

        if valid:
            answer += int("".join(digits))

    return answer


def solve_second_problem():
    data = get_input()
    answer = 0

    if data.status_code == 200:
        matrix = [list(line) for line in data.text.strip().split("\n")]
        digits = []
        coordinates = []
        coordinates_to_gear = dict()
        valid = False

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j].isdigit():
                    digits.append(matrix[i][j])
                    for a in range(-1, 2):
                        for b in range(-1, 2):
                            if 0 <= i + a < len(matrix) and 0 <= j + b < len(matrix[i]) and matrix[i + a][j + b] == '*':
                                coordinates.append((i + a, j + b))
                                valid = True
                                break
                else:
                    if valid:
                        if coordinates[0] in coordinates_to_gear.keys():
                            coordinates_to_gear[coordinates[0]].append(int("".join(digits)))
                        else:
                            coordinates_to_gear[coordinates[0]] = [int("".join(digits))]
                        valid = False
                        coordinates.clear()
                    digits.clear()

        if valid:
            if coordinates[0] in coordinates_to_gear.keys():
                coordinates_to_gear[coordinates[0]].append(int("".join(digits)))
            else:
                coordinates_to_gear[coordinates[0]] = [int("".join(digits))]

    for key in coordinates_to_gear.keys():
        if len(coordinates_to_gear[key]) == 2:
            answer += coordinates_to_gear[key][0] * coordinates_to_gear[key][1]
    return answer


def main():
    print(solve_first_problem())
    print(solve_second_problem())


if __name__ == "__main__":
    main()
