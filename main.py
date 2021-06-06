import random


# TODO: export as spreadsheet
def main():
    # TODO: read from file
    people = {
        'Alice',
        'Bob',
        'Carol',
        'Dave',
        'Eve',
        'Frodo',
        'Greta'
    }
    pairings = pair(people)
    display_pairings(pairings)


def pair(people: {str}):
    if len(people) <= 1:
        # TODO: throw instead
        return

    pairings = []
    already_paired = set()

    should_group_three = False
    if len(people) >= 3 and is_odd(len(people)):
        should_group_three = True

    for person in people:
        if person not in already_paired:
            already_paired.add(person)

            second_person = select_random_person(people, already_paired)
            already_paired.add(second_person)

            if should_group_three:
                third_person = select_random_person(people, already_paired)
                already_paired.add(third_person)
                should_group_three = False
                pairings.append((person, second_person, third_person))
            else:
                pairings.append((person, second_person))

    return pairings


def is_odd(n: int):
    return n % 2 != 0


def display_pairings(pairings: [str]):
    print('Pairings:')
    for p in pairings:
        print(p)


def select_random_person(people: {str}, already_paired: {str}):
    available = people.symmetric_difference(already_paired)
    return random.choice(list(available))


if __name__ == '__main__':
    main()
