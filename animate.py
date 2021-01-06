import sys
import time

def runcursor():
    def spinning_cursor():
        cursor='/-\|'
        i = 0
        while 1:
            yield cursor[i]
            i = (i + 1) % len(cursor)


    for c in spinning_cursor():
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')