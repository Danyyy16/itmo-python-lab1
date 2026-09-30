import os
import time

RED = '\u001b[41m'
END = '\u001b[0m'
GOTO = '\u001b[{};{}H'

os.system('')


center = 3

for repeat in range(3):
    for k in range(4):
        os.system('cls')
        for y in range(7):
            print(GOTO.format(y + 3, 10), end='')
            for x in range(7):
                if abs(x - center) + abs(y - center) <= k:
                    print(RED + '  ' + END, end='')
                else:
                    print('  ', end='')
            print()
        time.sleep(0.2)
