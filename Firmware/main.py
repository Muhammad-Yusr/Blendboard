import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

# 6 switches
PINS = [board.D3, board.D4, board.D2, board.D1, board.D0, board.D5]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        # Switch 1: Undo (Ctrl+Z)
        KC.Macro(Press(KC.LCTRL), Tap(KC.Z), Release(KC.LCTRL)),

        # Switch 2: Redo (Ctrl+Y)
        KC.Macro(Press(KC.LCTRL), Tap(KC.Y), Release(KC.LCTRL)),

        # Switch 3: Duplicate selection (Shift+D)
        KC.Macro(Press(KC.LSHIFT), Tap(KC.D), Release(KC.LSHIFT)),

        # Switch 4: Save file (Ctrl+S)
        KC.Macro(Press(KC.LCTRL), Tap(KC.S), Release(KC.LCTRL)),

        # Switch 5: X-Ray Mode (Alt+Z)
        KC.Macro(Press(KC.LALT), Tap(KC.Z), Release(KC.LALT)),

        # Switch 6: Wireframe view (Z, then 4)
        KC.Macro(Tap(KC.Z), Tap(KC.FOUR))
    ]
]

if __name__ == '__main__':
    keyboard.go()
