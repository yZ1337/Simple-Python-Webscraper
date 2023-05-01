import sys
import time


def loading(value):
    animation_chars = ['-', '\\', '|', '/']

    for i in range(20):
        animation_index = i % len(animation_chars)
        sys.stdout.write(f'\r{value} {animation_chars[animation_index]}')
        sys.stdout.flush()
        time.sleep(0.1)

    return

