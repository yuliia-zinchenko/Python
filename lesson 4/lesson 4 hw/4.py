name = ['Harry', 'Kate', 'Sarah', 'Melanie', 'Maria', 'Ricky']
message_1 = f'Sorry, only {name[2]} and {name[3]} are invited to dinner'
print(message_1)
message_2 = f'{name[0]}, sorry about canceled the invintation'
print(message_2)
message_3 = f'{name[1]}, sorry about canceled the invintation'
print(message_3)
message_4 = f'{name[4]}, sorry about canceled the invintation'
print(message_4)
message_5 = f'{name[5]}, sorry about canceled the invintation'
print(message_5)
del_1 = name.pop(0)
del_2 = name.pop(0)
del_3 = name.pop(2)
del_4 = name.pop(2)
message_6 = f'{name[0]}, you have been invited to dinner'
message_7 = f'{name[1]}, you have been invited to dinner'
print(message_6)
print(message_7)
del name[0]
del name[0]
print(name)
