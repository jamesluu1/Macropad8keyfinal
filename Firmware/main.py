import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

# 1. DEFINE YOUR MATRIX CONNECTIONS
# Look at your KiCad schematic. List the XIAO pins that connect to your rows/columns!
keyboard.matrix = MatrixScanner(
    column_pins=[board.D0, board.D1, board.D2],  # Replace with your 3 Column Pin names
    row_pins=[board.D3, board.D4, board.D5],     # Replace with your 3 Row Pin names
)

# 2. DEFINE YOUR VISUAL 3-2-3 LAYOUT
# We use KC.NO to leave a structural "blank gap" for the missing key in the middle column.
keyboard.keymap = [
    [
        KC.A,    KC.D,    KC.F,  # Top Row    (Col 0, Col 1, Col 2)
        KC.B,    KC.E,    KC.G,  # Middle Row (Col 0, Col 1, Col 2)
        KC.C,    KC.NO,   KC.H,  # Bottom Row (Col 0, Structural Gap, Col 2)
    ]
]

if __name__ == '__main__':
    keyboard.go()
