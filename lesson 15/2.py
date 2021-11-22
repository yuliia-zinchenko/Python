gamers = []
for i in range(30):
    a = {'color':'green', 'speed': 'medium', 'coins': 15}
    gamers.append(a)
for a in gamers[4:9]:
    if a['color'] == 'green':
        a['color'] = 'blue'
        a['speed'] = 'fast'
        a['coins'] = 35
    if a['color'] == 'blue':
        a['color'] = 'white'
        a['speed'] = 'super-fast'
        a['coins'] = 50
for k in gamers:
    print(k)
print('-----------'*5)
print(f'Всего {len(gamers)} игроков')
