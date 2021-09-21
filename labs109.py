# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":
import itertools
import re


def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


def is_ascending(items):
    if len(items) == 1:
        return True
    elif items[0] < items[1]:
        return is_ascending(tail(items))
    else:
        return False


def tail(lst):
    return lst[1:] if len(lst) > 1 else lst


def riffle(items, out=True):
    i = 0
    j = len(items) // 2
    result = []
    for i in range(j):
        result.append(items[i] if out else items[i + j])
        result.append(items[i + j] if out else items[i])
    return result


def only_odd_digits(n):
    if (n % 10) % 2 == 0:
        return False
    else:
        if n < 10:
            return True
        else:
            return only_odd_digits(n // 10)


def is_cyclops(n):
    ints = int_to_list(n)
    if len(ints) % 2 == 0:
        return False
    m = len(ints) // 2
    if ints[m] != 0:
        return False
    for i in range(len(ints)):
        if ints[i] == 0 and i != m:
            return False
    return True


def int_to_list(n):
    if n < 10:
        return [n]
    else:
        return int_to_list(n // 10) + [n % 10]


def domino_cycle(tiles):
    if len(tiles) == 0:
        return True
    return domino_cycle_inner(tiles + [tiles[0]])


def domino_cycle_inner(tiles):
    if len(tiles) <= 1:
        return True
    if tiles[0][1] != tiles[1][0]:
        return False
    else:
        return domino_cycle_inner(tail(tiles))


def count_dominators(items):
    if len(items) == 0:
        return 0
    if len(items) == 1:
        return 1
    count = 1
    highest = items[len(items) - 1]
    for i in range(len(items) - 1, -1, -1):
        if items[i] > highest:
            highest = items[i]
            count += 1
    return count


def extract_increasing(digits):
    digits_list = digit_string_to_int_list(digits)
    results = [digits_list.pop(0)]
    building = 0
    while digits_list:
        building *= 10
        building += digits_list.pop(0)
        if building > results[-1]:
            results += [building]
            building = 0
    return results


def digit_string_to_int_list(string):
    return [int(i) for i in list(string)]


def words_with_letters(words, letters):
    regex = re.compile(".*" + ".*".join(letters) + ".*")
    return [word for word in words if regex.match(word)]


def taxi_zum_zum(moves):
    headings = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    heading = 0
    pos = (0, 0)
    for move in list(moves):
        if move == "F":
            pos = (pos[0] + headings[heading][0], pos[1] + headings[heading][1])
        elif move == "R":
            heading = (heading + 5) % 4
        elif move == "L":
            heading = (heading + 3) % 4
    return pos


def give_change(amount, coins):
    remnant = amount
    amounts = []
    for coin in coins:
        amounts += [coin for i in range(remnant // coin)]
        remnant = remnant % coin
    return amounts


def safe_squares_rooks(n, rooks):
    unsafe = [set(), set()]
    for rook in rooks:
        unsafe[0].add(rook[0])
        unsafe[1].add(rook[1])
    return (n - len(unsafe[0])) * (n - len(unsafe[1]))


def pancake_scramble(text):
    chars = list(text)
    prefix = True if len(chars) % 2 == 0 else False
    output = ""
    for char in chars:
        output = output + char if prefix else char + output
        prefix = not prefix
    return output


def words_with_given_shape(words, shape):
    return [word for word in words if len(word) == len(shape) + 1 and shape_of_word(word) == shape]


def shape_of_word(word):
    chars = list(word)
    return [compare_chars(chars[i], chars[i + 1]) for i in range(len(chars) - 1)]


def compare_chars(char1, char2):
    return 1 if ord(char1) < ord(char2) else (0 if ord(char1) == ord(char2) else -1)


def is_left_handed(pips):
    alignment = flip_die(rotate_die(list(pips)))
    return (alignment[1] + (1 if alignment[0][1] == 2 else 0)) % 2 == 1


def rotate_die(pips):
    new_die = pips
    while new_die[0] != 1 and new_die[0] != 6:
        new_die = tail(new_die) + [new_die[0]]
    return new_die


def flip_die(pips):
    new_die = []
    parity = 0
    for pip in pips:
        if pip > 3:
            new_die += [7 - pip]
            parity += 1
        else:
            new_die += [pip]
    return [new_die, parity]


card_values = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack": 11,
    "queen": 12,
    "king": 13,
    "ace": 14
}


def winning_card(cards, trump=None):
    trumps = [card for card in cards if trump and card[1] == trump]
    trumps.sort(key=(lambda card: card_values[card[0]]), reverse=True)
    if trumps:
        return trumps[0]
    in_suit = [card for card in cards if card[1] == cards[0][1]]
    in_suit.sort(key=(lambda card: card_values[card[0]]), reverse=True)
    return in_suit[0]


def knight_jump(knight, start, end):
    return set(knight) == set([abs(end[i] - start[i]) for i in range(len(start))])


def seven_zero(n):
    for i in seven_zero_generator():
        if i % n == 0:
            return i


def seven_zero_generator():
    for j in itertools.count(start=1):
        for k in range(j - 1, -1, -1):
            yield int(((j - k) * "7") + (k * "0"))


def can_balance(items):
    for i in range(len(items)):
        torques = get_torques(items, i)
        if sum(torques[slice(i)]) == sum(torques[slice(i + 1, len(torques))]):
            return i
    return -1


def get_torques(items, fulcrum):
    return [items[i] * abs(fulcrum - i) for i in range(len(items))]


def josephus(n, k):
    remaining = list(range(1, n+1))
    last_index = -1
    result = []
    for i in range(n):
        last_index = (last_index + k) % len(remaining)
        result += [remaining.pop(last_index)]
        last_index -= 1
    return result
