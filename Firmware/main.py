from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.neo_pixel import Neopixel

keyboard = KMKKeyboard()

# ---------------------------
# MATRIX CONFIGURATION
# ---------------------------


# Columns: 26, 27, 28
# Rows:    29, 6, 7

keyboard.col_pins = (26, 27, 28)
keyboard.row_pins = (29, 6, 7)


keyboard.diode_orientation = keyboard.DIODE_COL2ROW

# ---------------------------
# ROTARY ENCODER
# ---------------------------

encoders = EncoderHandler()
keyboard.modules.append(encoders)

# Encoder A = GPIO3
# Encoder B = GPIO4
# Press switch = GPIO1

encoders.pins = (
    (3, 4),   # (A, B)
)

encoders.map = [
    ( (KC.VOLU, KC.VOLD), )   # clockwise → volume up, ccw → volume down
]

# Encoder push button
ENCODER_PRESS = KC.ENT  
keyboard.hotkey = {(1,): ENCODER_PRESS}

# ---------------------------
# RGB LED STRIP (SK6812 MINI)
# ---------------------------

# 4 LEDs on GPIO2
rgb = Neopixel(
    pin=2,
    num_pixels=4,
    brightness=0.4,
    pixel_order=Neopixel.GRB
)
keyboard.modules.append(rgb)

# ---------------------------
# KEYMAP
# ---------------------------




keyboard.keymap = [
    [
        KC.A, KC.B, KC.C,   # row 0
        KC.D, KC.NO, KC.NO, # row 1
        KC.NO, KC.NO, KC.NO # row 2
    ]
]

# ---------------------------
# START
# ---------------------------

if __name__ == '__main__':
    keyboard.go()


