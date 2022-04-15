# -*- coding:utf -8 -*-
#!/usr/bin/python3

from local_settings import USERS, LENGTH, CHARS
from alive_progress import alive_bar
import time
import random

with alive_bar(len(USERS), dual_line=True, title='Генерация паролей:') as bar:
    with open('passwords.txt', 'w', encoding='utf-8') as file:
        for user in range(len(USERS)):
            bar.text = f' ->Генерация пароля для пользователя: {USERS[user]}'
            password =''
            for i in range(LENGTH):
                password += random.choice(CHARS)
            file.write(f'{USERS[user]:35s}\t{password}\n')
            time.sleep(0.005)
            bar()