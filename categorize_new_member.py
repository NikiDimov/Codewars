def open_or_senior(data):
    new_data = []
    for person in data:
        age = int(person[0])
        handicap = int(person[1])
        if -2 <= handicap <= 26:
            if age >= 55 and handicap >= 7:
                new_data.append("Senior")
            else:
                new_data.append("Open")
    return new_data


data = [(16, 23), (73, 1), (56, 20), (1, -1)]
open_or_senior(data)
print(open_or_senior(data))
