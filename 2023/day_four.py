from utils import scrap_input
from httpstatus import HTTPStatus
import logging


###
# --- Part Two ---
###

def solve_first_problem():
    response = scrap_input(4)
    if response.status_code == HTTPStatus.OK:
        txt = response.text.split("\n")

    return process(txt)


def process(text):
    points = 0
    to_be_processed = []
    for line in text:
        line, current_set = line[10:].split(" "), set()
        for element in line:
            if element.isdigit():
                current_set.add(element)
            else:  # Here we reach the pipe
                to_be_processed.append(current_set)
                current_set = set()

        to_be_processed.append(current_set)
        matches = len(to_be_processed[0].intersection(to_be_processed[1]))
        if matches <= 1:
            points += matches
        else:
            nr = 1
            for el in range(2, matches + 1):
                nr = nr * 2
            points += nr
        to_be_processed.clear()
    return points


###
# --- Part Two ---
###

def solve_second_problem():
    response = scrap_input(4)
    if response.status_code == 200:
        txt = response.text.split("\n")


def main():
    logging.basicConfig(format='Answer is: %(message)s', level=logging.INFO)
    logging.info(solve_first_problem())
    logging.info(solve_second_problem())


if __name__ == "__main__":
    main()
