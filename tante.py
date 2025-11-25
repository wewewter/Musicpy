import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("Tante.....", 0.12),
        ("Sudah terbiasa terjadi tanteee", 0.09),
        ("Teman datang ketika lagi butuh saja", 0.09),
        ("Coba Kalo lagi susah ", 0.10),
        ("Mereka Semua Menghilaaaaangg", 0.09),
    ]

    delays = [0.8, 1.5, 0.9 , 0.9, 5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()