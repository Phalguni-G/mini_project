# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a, b = sys.argv[1], sys.argv[2]
    print(a,b)
    print(add(a,b))
    print(sub(a,b))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
