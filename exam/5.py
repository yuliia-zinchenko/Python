users = ['user1', 'user2', 'user3']
users_conf = []
while users:
    a = users.pop()
    print('Проверенные пользователи: ', a)
    users_conf.append(a)
print(users_conf)
