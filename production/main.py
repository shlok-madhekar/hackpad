import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# 6 physical buttons connected to D0 through D5
PINS = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,                         # Key 1
        KC.DELETE,                   # Key 2
        KC.MACRO("Hello world!"),    # Key 3
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),  # Key 4
        KC.ENTER,                    # Key 5
        KC.BACKSPACE                 # Key 6
    ]
]

if __name__ == '__main__':
    keyboard.go()