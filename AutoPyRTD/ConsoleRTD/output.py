import time

def toConsole(o):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'

#     print("Line 1: Static content")
#     print("-")
#     print("-")

#     for color_code in range(29, 37):
#         message = f"\033[{color_code}m  Text with color {color_code}\033[0m"
#         time.sleep(1)
#         print(LINE_UP, end=LINE_CLEAR)
#         print(LINE_UP, end=LINE_CLEAR)
#         print(message)
#         print(message)
# toConsole()
    [(print(LINE_CLEAR), print(LINE_UP)) for _ in range(144)]

    