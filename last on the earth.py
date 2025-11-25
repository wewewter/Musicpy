import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("you're the moonlight of my life", 0.12),
        ("Every night", 0.17),
        ("Givin' all my love to u", 0.15),
        ("My beatin' heart belongs to u", 0.12),
        ("I walked for miles 'till i found you", 0.11),
        ("I here to honour you", 0.12),
        ("If i lose everything in the fire", 0.14),
        ("I'm sendin' all my love to you", 0.10),
        
    ]

    delays = [0.6, 2.0, 5.0 , 3.2, 5.0 , 0.5, 0.5, 0.1]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()