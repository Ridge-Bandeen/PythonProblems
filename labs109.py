# # As an example, here is an implementation of
# # the first problem "Ryerson Letter Grade":
# import itertools
# import math
# import re
#
#
# def ryerson_letter_grade(n):
#     if n < 50:
#         return 'F'
#     elif n > 89:
#         return 'A+'
#     elif n > 84:
#         return 'A'
#     elif n > 79:
#         return 'A-'
#     tens = n // 10
#     ones = n % 10
#     if ones < 3:
#         adjust = "-"
#     elif ones > 6:
#         adjust = "+"
#     else:
#         adjust = ""
#     return "DCB"[tens - 5] + adjust
#
#
# def is_ascending(items):
#     if len(items) == 1:
#         return True
#     elif items[0] < items[1]:
#         return is_ascending(tail(items))
#     else:
#         return False
#
#
# def tail(lst):
#     return lst[1:] if len(lst) > 1 else lst
#
#
# def riffle(items, out=True):
#     i = 0
#     j = len(items) // 2
#     result = []
#     for i in range(j):
#         result.append(items[i] if out else items[i + j])
#         result.append(items[i + j] if out else items[i])
#     return result
#
#
# def only_odd_digits(n):
#     if (n % 10) % 2 == 0:
#         return False
#     else:
#         if n < 10:
#             return True
#         else:
#             return only_odd_digits(n // 10)
#
#
# def is_cyclops(n):
#     ints = int_to_list(n)
#     if len(ints) % 2 == 0:
#         return False
#     m = len(ints) // 2
#     if ints[m] != 0:
#         return False
#     for i in range(len(ints)):
#         if ints[i] == 0 and i != m:
#             return False
#     return True
#
#
# def int_to_list(n):
#     if n < 10:
#         return [n]
#     else:
#         return int_to_list(n // 10) + [n % 10]
#
#
# def domino_cycle(tiles):
#     if len(tiles) == 0:
#         return True
#     return domino_cycle_inner(tiles + [tiles[0]])
#
#
# def domino_cycle_inner(tiles):
#     if len(tiles) <= 1:
#         return True
#     if tiles[0][1] != tiles[1][0]:
#         return False
#     else:
#         return domino_cycle_inner(tail(tiles))
#
#
# def count_dominators(items):
#     if len(items) == 0:
#         return 0
#     if len(items) == 1:
#         return 1
#     count = 1
#     highest = items[len(items) - 1]
#     for i in range(len(items) - 1, -1, -1):
#         if items[i] > highest:
#             highest = items[i]
#             count += 1
#     return count
#
#
# def extract_increasing(digits):
#     digits_list = digit_string_to_int_list(digits)
#     results = [digits_list.pop(0)]
#     building = 0
#     while digits_list:
#         building *= 10
#         building += digits_list.pop(0)
#         if building > results[-1]:
#             results += [building]
#             building = 0
#     return results
#
#
# def digit_string_to_int_list(string):
#     return [int(i) for i in list(string)]
#
#
# def words_with_letters(words, letters):
#     regex = re.compile(".*" + ".*".join(letters) + ".*")
#     return [word for word in words if regex.match(word)]
#
#
# def taxi_zum_zum(moves):
#     headings = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     heading = 0
#     pos = (0, 0)
#     for move in list(moves):
#         if move == "F":
#             pos = (pos[0] + headings[heading][0], pos[1] + headings[heading][1])
#         elif move == "R":
#             heading = (heading + 5) % 4
#         elif move == "L":
#             heading = (heading + 3) % 4
#     return pos
#
#
# def give_change(amount, coins):
#     remnant = amount
#     amounts = []
#     for coin in coins:
#         amounts += [coin for i in range(remnant // coin)]
#         remnant = remnant % coin
#     return amounts
#
#
# def safe_squares_rooks(n, rooks):
#     unsafe = [set(), set()]
#     for rook in rooks:
#         unsafe[0].add(rook[0])
#         unsafe[1].add(rook[1])
#     return (n - len(unsafe[0])) * (n - len(unsafe[1]))
#
#
# def pancake_scramble(text):
#     chars = list(text)
#     prefix = True if len(chars) % 2 == 0 else False
#     output = ""
#     for char in chars:
#         output = output + char if prefix else char + output
#         prefix = not prefix
#     return output
#
#
# def words_with_given_shape(words, shape):
#     return [word for word in words if len(word) == len(shape) + 1 and shape_of_word(word) == shape]
#
#
# def shape_of_word(word):
#     chars = list(word)
#     return [compare_chars(chars[i], chars[i + 1]) for i in range(len(chars) - 1)]
#
#
# def compare_chars(char1, char2):
#     return 1 if ord(char1) < ord(char2) else (0 if ord(char1) == ord(char2) else -1)
#
#
# def is_left_handed(pips):
#     alignment = flip_die(rotate_die(list(pips)))
#     return (alignment[1] + (1 if alignment[0][1] == 2 else 0)) % 2 == 1
#
#
# def rotate_die(pips):
#     new_die = pips
#     while new_die[0] != 1 and new_die[0] != 6:
#         new_die = tail(new_die) + [new_die[0]]
#     return new_die
#
#
# def flip_die(pips):
#     new_die = []
#     parity = 0
#     for pip in pips:
#         if pip > 3:
#             new_die += [7 - pip]
#             parity += 1
#         else:
#             new_die += [pip]
#     return [new_die, parity]
#
#
# card_values = {
#     "one": 1,
#     "two": 2,
#     "three": 3,
#     "four": 4,
#     "five": 5,
#     "six": 6,
#     "seven": 7,
#     "eight": 8,
#     "nine": 9,
#     "ten": 10,
#     "jack": 11,
#     "queen": 12,
#     "king": 13,
#     "ace": 14
# }
#
#
# def winning_card(cards, trump=None):
#     trumps = [card for card in cards if trump and card[1] == trump]
#     trumps.sort(key=(lambda card: card_values[card[0]]), reverse=True)
#     if trumps:
#         return trumps[0]
#     in_suit = [card for card in cards if card[1] == cards[0][1]]
#     in_suit.sort(key=(lambda card: card_values[card[0]]), reverse=True)
#     return in_suit[0]
#
#
# def knight_jump(knight, start, end):
#     return set(knight) == set([abs(end[i] - start[i]) for i in range(len(start))])
#
#
# def seven_zero(n):
#     for i in seven_zero_generator():
#         if i % n == 0:
#             return i
#
#
# def seven_zero_generator():
#     for j in itertools.count(start=1):
#         for k in range(j - 1, -1, -1):
#             yield int(((j - k) * "7") + (k * "0"))
#
#
# def can_balance(items):
#     for i in range(len(items)):
#         torques = get_torques(items, i)
#         if sum(torques[slice(i)]) == sum(torques[slice(i + 1, len(torques))]):
#             return i
#     return -1
#
#
# def get_torques(items, fulcrum):
#     return [items[i] * abs(fulcrum - i) for i in range(len(items))]
#
#
# def josephus(n, k):
#     remaining = list(range(1, n + 1))
#     last_index = -1
#     result = []
#     for i in range(n):
#         last_index = (last_index + k) % len(remaining)
#         result += [remaining.pop(last_index)]
#         last_index -= 1
#     return result
#
#
# def group_and_skip(n, out, ins):
#     if n == 0:
#         return []
#     return [n % out] + group_and_skip((n // out) * ins, out, ins)
#
#
# def recaman(n):
#     found = {1}
#     sequence = [1]
#     for i in range(2, n + 1):
#         if sequence[-1] - i > 0 and sequence[-1] - i not in found:
#             next_element = sequence[-1] - i
#             sequence += [next_element]
#             found.add(next_element)
#         else:
#             next_element = sequence[-1] + i
#             sequence += [next_element]
#             found.add(next_element)
#     return sequence
#
#
# def pyramid_blocks(n, m, h):
#     lesser = n if n <= m else m
#     greater = m if n <= m else n
#     difference = greater - lesser
#     top = h + (lesser - 1)
#     full_pyramid = full_rectangular_pyramid(top, difference)
#     cap = full_rectangular_pyramid(lesser - 1, difference)
#     return full_pyramid - cap
#
#
# def full_rectangular_pyramid(h, d):
#     main_pyramid = ((2 * (h ** 3)) + (3 * (h ** 2)) + h) // 6
#     single_layer = h * (h + 1) // 2
#     return main_pyramid + (single_layer * d)
#
#
# def count_growlers(animals):
#     return iterate_animals(animals, False) + iterate_animals(reversed(animals), True)
#
#
# def iterate_animals(animals, right):
#     dogs = 0
#     cats = 0
#     growlers = 0
#     for animal in animals:
#         if dogs > cats and facing_left(animal) != right:
#             growlers += 1
#         if is_cat(animal):
#             cats += 1
#         else:
#             dogs += 1
#     return growlers
#
#
# def is_cat(animal):
#     return animal == "cat" or animal == "tac"
#
#
# def facing_left(animal):
#     return animal == "cat" or animal == "dog"
#
#
# def bulgarian_solitaire(piles, k):
#     piles = piles[:]
#     steady_state = set(range(1, k + 1))
#     rounds = 0
#     while set(piles) != steady_state:
#         piles = solitaire_round(piles)
#         rounds += 1
#     return rounds
#
#
# def solitaire_round(piles):
#     new_pile = len(piles)
#     return [pile - 1 for pile in piles if pile - 1 > 0] + [new_pile]
#
#
# def scylla_or_charybdis(moves, n):
#     results = [(k, test_k_value(moves, n, k)) for k in range(1, (len(moves) // 2) + 1)]
#     filtered_results = [t for t in results if t[1]]
#     sorted_results = sorted(filtered_results, key=lambda t: t[1])
#     lowest_results = [t for t in sorted_results if t[1] == sorted_results[0][1]]
#     return sorted(lowest_results, key=lambda t: t[0])[0][0]
#
#
# def test_k_value(moves, n, k):
#     pos = 0
#     i = k - 1
#     steps = 0
#     while abs(pos) < n and i < len(moves):
#         pos += 1 if moves[i] == "+" else -1
#         i += k
#         steps += 1
#     return steps if abs(pos) >= n else False
#
#
# # def arithmetic_progression(items):
# #     longest = (items[0], 0, 1)
# #     start = 0
# #     while len(items) - start > longest[2]:
# #         for step in range(1, items[-1] + 1):
# #             if (items[-1] - items[start]) // step < longest[2]:
# #                 break
# #             length = get_longest_progression(set(items), items[start], step)
# #             if length > longest[2]:
# #                 longest = (items[start], step, length)
# #         start += 1
# #     return longest
# #
# #
# # def get_longest_progression(items, start, step):
# #     i = 0
# #     while start + (i * step) in items:
# #         i += 1
# #     return i
#
#
# def tukeys_ninthers(items):
#     if len(items) == 1:
#         return items[0]
#     items = items[:]
#     new_items = []
#     while items:
#         new_items += [sorted([items.pop(), items.pop(), items.pop()])[1]]
#     return tukeys_ninthers(new_items)
#
#
# def is_zigzag(n, up=None):
#     digits = int_to_list(n)
#     if len(digits) <= 1:
#         return True
#     if len(digits) == 2:
#         return digits[0] != digits[1]
#     last = digits[1]
#     up = digits[1] > digits[0]
#     i = 2
#     while i < len(digits):
#         if (digits[i] > last) == up:
#             return False
#         last = digits[i]
#         i += 1
#         up = not up
#     return True
#
#
# def crag_score(dice):
#     return max([
#         50 if has_pair(dice) and sum(dice) == 13 else 0,
#         26 if sum(dice) == 13 else 0,
#         25 if dice[0] == dice[1] and dice[1] == dice[2] else 0,
#         20 if sorted(dice) == [1, 2, 3] else 0,
#         20 if sorted(dice) == [1, 3, 5] else 0,
#         20 if sorted(dice) == [4, 5, 6] else 0,
#         20 if sorted(dice) == [2, 4, 6] else 0,
#         sum([n for n in dice if n == 6]),
#         sum([n for n in dice if n == 5]),
#         sum([n for n in dice if n == 4]),
#         sum([n for n in dice if n == 3]),
#         sum([n for n in dice if n == 2]),
#         sum([n for n in dice if n == 1])
#     ])
#
#
# def has_pair(dice):
#     return dice[0] == dice[1] or dice[1] == dice[2] or dice[2] == dice[0]
#
#
# def three_summers(items, goal):
#     items = items[:]
#     while items:
#         x = items.pop()
#         if two_summers(items, goal - x):
#             return True
#     return False
#
#
# def two_summers(items, goal, i=0, j=None):
#     j = j if j is not None else len(items) - 1
#     while i < j:
#         x = items[i] + items[j]
#         if x == goal:
#             return True
#         elif x < goal:
#             i += 1
#         else:
#             j -= 1
#     return False
#
#
# def sum_of_two_squares(n):
#     if n % 2 == 0 and int(math.sqrt(n / 2)) ** 2 == n / 2:
#         return tuple([int(math.sqrt(n // 2)), int(math.sqrt(n // 2))])
#     squares = [i ** 2 for i in range(1, int(math.sqrt(n - 1)) + 1)]
#     result = return_two_summers(squares, n)
#     return tuple([int(math.sqrt(i)) for i in result]) if result is not None else None
#
#
# def return_two_summers(items, goal, i=0, j=None):
#     j = j if j is not None else len(items) - 1
#     while i < j:
#         x = items[i] + items[j]
#         if x == goal:
#             return [items[j], items[i]]
#         elif x < goal:
#             i += 1
#         else:
#             j -= 1
#     return None
#
#
# def count_carries(a, b, carry=0):
#     if (a == 0 or b == 0) and carry == 0:
#         return 0
#     next_carry = 1 if a % 10 + b % 10 + carry > 9 else 0
#     return next_carry + count_carries(a // 10, b // 10, next_carry)
#
#
# def leibniz(heads, positions):
#     last_row = []
#     this_row = []
#     for row in range(len(heads)):
#         for n in range(row + 1):
#             if n == 0:
#                 this_row += [heads[row]]
#             else:
#                 this_row += [last_row[n - 1] - this_row[n - 1]]
#         last_row = this_row[:]
#         this_row = []
#     return [last_row[i] for i in positions]
#
#
# def expand_intervals(intervals):
#     if intervals == "":
#         return []
#     interval_strings = intervals.split(",")
#     intervals = [interval_string.split("-") for interval_string in interval_strings]
#     results = []
#     for interval in intervals:
#         if len(interval) > 1:
#             results += range(int(interval[0]), int(interval[1]) + 1)
#         else:
#             results += [int(interval[0])]
#     return results
#
#
# def collapse_intervals(items):
#     if len(items) == 0:
#         return ""
#     intervals = []
#     working_interval = []
#     for item in items:
#         if len(working_interval) == 0 or item == working_interval[-1] + 1:
#             working_interval += [item]
#         else:
#             intervals += [working_interval]
#             working_interval = [item]
#     intervals += [working_interval]
#     interval_strings = [format_to_interval_string(interval) for interval in intervals]
#     return ",".join(interval_strings)
#
#
# def format_to_interval_string(interval):
#     if len(interval) > 1:
#         return str(interval[0]) + "-" + str(interval[-1])
#     else:
#         return str(interval[0])
#
#
# def prominences(heights):
#     heights = [0] + heights[:] + [0]
#     extremes = []
#     for i in range(1, len(heights) - 1):
#         if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
#             extremes += [(heights[i], "peak", i)]
#         elif heights[i] < heights[i - 1] and heights[i] < heights[i + 1]:
#             extremes += [(heights[i], "valley", i)]
#     return [tuple([extremes[j][2] - 1, extremes[j][0], deepest_valley_before_higher_peak(extremes, j)]) for j in
#             range(len(extremes)) if extremes[j][1] == "peak"]
#
#
# def deepest_valley_before_higher_peak(extremes, h):
#     i = h - 1
#     l_higher = False
#     l_lowest = extremes[h][0]
#     while i >= 0 and not l_higher:
#         if extremes[i][1] == "peak" and extremes[i][0] > extremes[h][0]:
#             l_higher = True
#         elif extremes[i][1] == "valley" and extremes[i][0] < l_lowest:
#             l_lowest = extremes[i][0]
#         i -= 1
#     if not l_higher:
#         l_lowest = 0
#
#     i = h + 1
#     r_higher = False
#     r_lowest = extremes[h][0]
#     while i < len(extremes) and not r_higher:
#         if extremes[i][1] == "peak" and extremes[i][0] > extremes[h][0]:
#             r_higher = True
#         elif extremes[i][1] == "valley" and extremes[i][0] < r_lowest:
#             r_lowest = extremes[i][0]
#         i += 1
#     if not r_higher:
#         r_lowest = 0
#
#     if not r_higher and not l_higher:
#         return extremes[h][0]
#     if r_higher and not l_higher:
#         return extremes[h][0] - r_lowest
#     if l_higher and not r_higher:
#         return extremes[h][0] - l_lowest
#     if l_lowest > r_lowest:
#         return extremes[h][0] - l_lowest
#     return extremes[h][0] - r_lowest
#
#
# def word_dominator_comparison(x, y):
#     if len(x) != len(y):
#         return x > y
#     else:
#         return len([i for i in range(len(x)) if x[i] > y[i]]) > (len(x) // 2)
#
#
# def count_dominators_exhaustive(items, comparison=(lambda x, y: x > y)):
#     if len(items) == 0:
#         return 0
#     if len(items) == 1:
#         return 1
#     count = 0
#     for i in range(len(items) - 1, -1, -1):
#         flag = False
#         for j in range(i + 1, len(items)):
#             if not comparison(items[i], items[j]):
#                 flag = True
#         count += 0 if flag else 1
#     return count
#
#
# def count_word_dominators(words):
#     return count_dominators_exhaustive(words, word_dominator_comparison)
#
#
# def duplicate_digit_bonus(n):
#     n = str(n)
#     last_digit = ""
#     count = 0
#     total = 0
#     for digit in n:
#         if digit == last_digit:
#             count += 1
#         else:
#             if count > 1:
#                 total += 10 ** (count - 2)
#             count = 1
#             last_digit = digit
#     if count > 1:
#         total += 2 * (10 ** (count - 2))
#     return total
#
#
# def nearest_single_smaller(items, index):
#     for offset in range(1, max(len(items) - index, index + 1)):
#         lower = items[index - offset] if index >= offset else items[index]
#         higher = items[index + offset] if index + offset < len(items) else items[index]
#         lowest = min(lower, higher)
#         if lowest < items[index]:
#             return lowest
#     return items[index]
#
#
# def nearest_smaller(items):
#     return [nearest_single_smaller(items, index) for index in range(len(items))]
#
#
# def squares_intersect(s1, s2):
#     return s1[0] + s1[2] >= s2[0] \
#            and s2[0] + s2[2] >= s1[0] \
#            and s1[1] + s1[2] >= s2[1] \
#            and s2[1] + s2[2] >= s1[1]
#
#
# def oware_move(board, house):
#     board = board[:]
#     hand = board[house]
#     index = house
#     board[house] = 0
#     upper_bound = len(board) - 1
#     while hand > 0:
#         index = index + 1 if index < upper_bound else 0
#         if index != house:
#             board[index] += 1
#             hand -= 1
#     midboard = (len(board) // 2) - 1
#     capture = True
#     while index > midboard and capture:
#         if board[index] == 2 or board[index] == 3:
#             board[index] = 0
#             index -= 1
#         else:
#             capture = False
#     return board
#
#
# def remove_after_kth(items, k=1):
#     counts = dict([])
#     new_items = []
#     for item in items:
#         counts[item] = counts.get(item, 0) + 1
#         if counts[item] <= k:
#             new_items += [item]
#     return new_items
#
#
# def first_preceded_by_smaller(items, k=1):
#     smallest_k = sorted(items[:k])
#     for item in items[k:]:
#         if smallest_k[-1] < item:
#             return item
#         smallest_k = sorted(smallest_k + [item])[:k]
#     return None
#
#
# def eliminate_neighbours(items):
#     items = items[:]
#     steps = 0
#     highest = len(items)
#     while highest in items:
#         steps += 1
#         lowest = sorted(items)[0]
#         i = items.index(lowest)
#         if i == 0:
#             items = items[2:]
#         elif i == len(items) - 1:
#             items = items[:-2]
#         else:
#             if items[i - 1] > items[i + 1]:
#                 items = items[:i - 1] + items[i + 1:]
#             else:
#                 items = items[:i] + items[i + 2:]
#     return steps
#
#
# def count_and_say(digits):
#     result = ""
#     counter = 0
#     current_digit = ''
#     for digit in list(digits):
#         if digit != current_digit:
#             if counter != 0:
#                 result += f"{counter}{current_digit}"
#             counter = 1
#             current_digit = digit
#         else:
#             counter += 1
#     result += f"{counter}{current_digit}"
#     return result
#
#
# def reverse_vowels(text):
#     chars = list(text)
#     sample_vowels = list("aeiouAEIOU")
#     vowels = []
#     for char in chars:
#         if char in sample_vowels:
#             vowels += [char]
#     result = ""
#     for char in chars:
#         if char in sample_vowels:
#             if str.isupper(char):
#                 result += str.upper(vowels.pop())
#             else:
#                 result += str.lower(vowels.pop())
#         else:
#             result += char
#     return result
#
#
# def conjugate_regular(verb, subject, tense):
#     if re.search("ar$", verb):
#         if tense == "presente":
#             if subject == "yo":
#                 return re.sub("ar$", "o", verb)
#             if subject == "tú":
#                 return re.sub("ar$", "as", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("ar$", "a", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("ar$", "amos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("ar$", "áis", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("ar$", "an", verb)
#         if tense == "pretérito":
#             if subject == "yo":
#                 return re.sub("ar$", "é", verb)
#             if subject == "tú":
#                 return re.sub("ar$", "aste", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("ar$", "ó", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("ar$", "amos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("ar$", "asteis", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("ar$", "aron", verb)
#         if tense == "imperfecto":
#             if subject == "yo":
#                 return re.sub("ar$", "aba", verb)
#             if subject == "tú":
#                 return re.sub("ar$", "abas", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("ar$", "aba", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("ar$", "ábamos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("ar$", "abais", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("ar$", "aban", verb)
#         if tense == "futuro":
#             if subject == "yo":
#                 return re.sub("ar$", "aré", verb)
#             if subject == "tú":
#                 return re.sub("ar$", "arás", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("ar$", "ará", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("ar$", "aremos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("ar$", "aréis", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("ar$", "arán", verb)
#     elif re.search("ir$", verb):
#         if tense == "presente":
#             if subject == "yo":
#                 return re.sub("ir$", "o", verb)
#             if subject == "tú":
#                 return re.sub("ir$", "es", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("ir$", "e", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("ir$", "imos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("ir$", "ís", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("ir$", "en", verb)
#         if tense == "pretérito":
#             if subject == "yo":
#                 return re.sub("ir$", "í", verb)
#             if subject == "tú":
#                 return re.sub("ir$", "iste", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("ir$", "ió", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("ir$", "imos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("ir$", "isteis", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("ir$", "ieron", verb)
#         if tense == "imperfecto":
#             if subject == "yo":
#                 return re.sub("ir$", "ía", verb)
#             if subject == "tú":
#                 return re.sub("ir$", "ías", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("ir$", "ía", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("ir$", "íamos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("ir$", "íais", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("ir$", "ían", verb)
#         if tense == "futuro":
#             if subject == "yo":
#                 return re.sub("ir$", "iré", verb)
#             if subject == "tú":
#                 return re.sub("ir$", "irás", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("ir$", "irá", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("ir$", "iremos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("ir$", "iréis", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("ir$", "irán", verb)
#     else:
#         if tense == "presente":
#             if subject == "yo":
#                 return re.sub("er$", "o", verb)
#             if subject == "tú":
#                 return re.sub("er$", "es", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("er$", "e", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("er$", "emos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("er$", "éis", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("er$", "en", verb)
#         if tense == "pretérito":
#             if subject == "yo":
#                 return re.sub("er$", "í", verb)
#             if subject == "tú":
#                 return re.sub("er$", "iste", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("er$", "ió", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("er$", "imos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("er$", "isteis", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("er$", "ieron", verb)
#         if tense == "imperfecto":
#             if subject == "yo":
#                 return re.sub("er$", "ía", verb)
#             if subject == "tú":
#                 return re.sub("er$", "ías", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("er$", "ía", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("er$", "íamos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("er$", "íais", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("er$", "ían", verb)
#         if tense == "futuro":
#             if subject == "yo":
#                 return re.sub("er$", "eré", verb)
#             if subject == "tú":
#                 return re.sub("er$", "erás", verb)
#             if subject in ["él", "ella", "usted"]:
#                 return re.sub("er$", "erá", verb)
#             if subject in ["nosotros", "nosotras"]:
#                 return re.sub("er$", "eremos", verb)
#             if subject in ["vosotros", "vosotras"]:
#                 return re.sub("er$", "eréis", verb)
#             if subject in ["ellos", "ellas", "ustedes"]:
#                 return re.sub("er$", "erán", verb)
#
#
# def frog_collision_time(frog1, frog2):
#     if ((frog1[2] - frog2[2] == 0) and not frog1[0] == frog2[0]) \
#             or ((frog1[3] - frog2[3] == 0) and not frog1[1] == frog2[1]):
#         return None
#     t_x = 0 if ((frog1[2] - frog2[2] == 0) and frog1[0] == frog2[0]) else \
#         (frog2[0] - frog1[0]) / (frog1[2] - frog2[2])
#     t_y = 0 if ((frog1[3] - frog2[3] == 0) and frog1[1] == frog2[1]) else \
#         (frog2[1] - frog1[1]) / (frog1[3] - frog2[3])
#     if t_x == 0 and t_y >= 0 and t_y.is_integer():
#         return int(t_y)
#     if t_y == 0 and t_x >= 0 and t_x.is_integer():
#         return int(t_x)
#     if t_x == t_y and t_x >= 0 and t_x.is_integer():
#         return int(t_x)
#     return None
#
#
import math


def nearest_polygonal_number(n, s):
    print(f'{n},{s}')
    exact = polygonal_number_i(n, s)
    lower_i = int(exact)
    lower = polygonal_number_at(s, lower_i)
    higher = polygonal_number_at(s, lower_i + 1)
    if higher - n < n - lower:
        return int(higher)
    return int(lower)


def polygonal_number_at(s, i):
    return (((s - 2) * (i ** 2)) - ((s - 4) * i)) // 2


def polygonal_number_i(n, s):
    return (math.sqrt((8 * n * (s - 2)) + ((s - 4) ** 2)) + s - 4) // (2 * (s - 2))
