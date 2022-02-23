import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    for host in dump:
        print(f'Pinging {host}...')
        print('-' * 60)
        os.system(f'ping -n 1 {host}')
        print('-' * 60)
        time.sleep(5)