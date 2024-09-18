lucky_numbers = [4, 4, 4, 8, 19, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.clear()
print(friends)

lucky_numbers.pop()
print(lucky_numbers.index(4))
print(lucky_numbers.count(4))
print(lucky_numbers)

lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = lucky_numbers.copy()
print(friends2)
