# -*- coding:utf -8 -*-
#!/usr/bin/python3

import time
import random
import configparser
import os


def main():
    config = configparser.ConfigParser()
    config.read('conf.ini')

    LENGTH = int(config['main']['LENGTH'])
    CHARS = config['main']['CHARS']
    CHARS_FULL = config['main']['CHARS_FULL'].split()
    USERS = config['users']['USERS'].split(',')
    
    with open('passwords.txt', 'w', encoding='utf-8') as file:
        for user in range(len(USERS)):
            password =''
            for i in range(LENGTH):
                password += random.choice(CHARS)
            file.write(f'{USERS[user]}\n@modul.tech\n{password}\n\n')
            print(f'{USERS[user]}\n@modul.tech\n{password}\n\n')
    os.startfile('passwords.txt')


if __name__ == '__main__':
    main()
