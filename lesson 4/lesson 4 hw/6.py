countries = ['Italy', 'USA', 'France', 'England', 'Canada']
print(countries)
countries.insert(0, 'Japan')
message = f'I dream to visit {countries[1]}'
print(message)
countries.sort()
print(countries)
countries.sort(reverse = 1)
print(countries)
del1 = countries.pop(4)
print(countries)
