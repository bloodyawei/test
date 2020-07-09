def see_joker(people_line):
    who_see_joker = []
    highest = max(people_line)
    highest_index = people_line.index(highest)
    who_see_joker.append(highest)
    while highest_index < len(people_line) - 1:
        other_height = max(people_line[highest_index + 1:])
        other_index = people_line[highest_index + 1:].index(other_height)
        if other_height != highest:
            who_see_joker.append(other_height)
        highest = other_height
        highest_index = highest_index + other_index + 1
    return who_see_joker

#test data
people = [1]
print(see_joker(people))

people = [1, 2, 3, 4]
print(see_joker(people))

people = [4, 3, 2, 1]
print(see_joker(people))

people = [1, 3, 2, 4]
print(see_joker(people))

people = [4, 2, 3, 1]
print(see_joker(people))

people = [1, 2, 6, 5, 3, 4]
print(see_joker(people))

people = [6, 2, 5, 3, 4, 1]
print(see_joker(people))

people = [6, 2, 3, 3, 5, 5]
print(see_joker(people))

people = [6, 5, 4, 5, 3, 3]
print(see_joker(people))