from utils import scrap_input
from httpstatus import HTTPStatus
import logging

###
# --- Part One ---
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
    if response.status_code == HTTPStatus.OK:

        txt = response.text.split("\n")

        # txt = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        #          Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        #          Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        #          Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        #          Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        #          Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")

        cards = {k: 1 for k in range(1, len(txt))}
        current_card = 1
        to_be_processed = []
        for line in txt:

            if line:
                start_index = line.index(":") + 1
                line, current_set = line[start_index:].split(" "), set()
                for element in line:
                    if element.isdigit():
                        current_set.add(element)
                    elif element == "|":  # Here we reach the pipe
                        to_be_processed.append(current_set)
                        current_set = set()

                to_be_processed.append(current_set)
                matches = len(to_be_processed[0].intersection(to_be_processed[1]))

                current_card += 1
                for key in range(current_card, current_card + matches):

                    if (key) < len(cards):
                        cards[key] += cards[current_card - 1]

                to_be_processed.clear()

        return sum(list(cards.values()))

def main():
    logging.basicConfig(format='Answer is: %(message)s', level=logging.INFO)
    logging.info(solve_first_problem())
    logging.info(solve_second_problem())


if __name__ == "__main__":
    main()
