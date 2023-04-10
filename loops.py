# for i in range(1, 11, 3):
#     print(i)

# l = ("Tanmay", "Yugandhar", "Raj")
# for s in l:
#     print(s)

from sys import stdout as std
from time import sleep
import os

buffers = ["Tanmay", "Yugandhar"]
buf = ""
temp = ""

while 1:
    std.write("\rHello, ")
    std.flush()
    sleep(.300)
    for s in buffers:
        for n in s:
            buf += n
            std.write(f"\rHello, {buf}")
            std.flush()
            sleep(.400)
        # for n in s:
        #     temp += "  "
        # std.write(f"\rHello, {temp}")
        # # std.write("\rHello,                                       ")
        # std.flush()
        temp = ""
        for n in s:
            buf = buf[:-1]
            # std.write(f"\rHello, {buf}{temp}")
            std.write(f"\rHello, {buf}")
            std.flush()
            # temp += " "
            sleep(.400)
            os.system('cls')
        buf = ""
        temp = ""
    std.flush()

# for i in range(1, 100001):
#     std.write(f"\r{i}. Good Morning!")
#     std.flush()
