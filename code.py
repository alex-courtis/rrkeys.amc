print("Starting")

import board
import json

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
import qmkconfconverter as QC

QMK_FILE = "keys_config.json"
keyboard = KMKKeyboard()
#keyboard.debug_enabled = True

keyboard.row_pins = (board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16)
keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.coord_mapping = [
#   15  14  13  12  11  10          10  11  12  13  14  15

    0,  1,  2,  3,  4,  5,          41, 40, 39, 38, 37, 36,     #gp21
    6,  7,  8,  9,  10, 11,         47, 46, 45, 44, 43, 42,     #gp20
    12, 13, 14, 15, 16, 17,         53, 52, 51, 50, 49, 48,     #gp19
    18, 19, 20, 21, 22, 23,         59, 58, 57, 56, 55, 54,     #gp18
 24, 25,    26, 27, 28, 29,         65, 64, 63, 62,    61, 60,  #gp17
 30, 31,    32, 33, 34, 35,         71, 70, 69, 68,    67, 66,  #gp16
    ]

# Dont forget to switch TX and RX in hardware when connecting between the two picos
keyboard.modules.append(Split(
    data_pin=board.GP1,
    data_pin2=board.GP0,
    uart_flip=False,
    split_flip=False
))

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())


str_data = QC.qmk_to_kmk(QMK_FILE)
#exec(open(KMK_FILE).read())
exec("qmk_layers = " + str_data)
keyboard.keymap = QC.layers_converter(qmk_layers)
#print(keyboard.keymap)

print("Running main")
if __name__ == '__main__':
    keyboard.go()


# TODO in future convert qmk configurator to kmk
#try:
#    f = open(FILE_NAME)
#    data = json.load(f)
#    keyboard.keymap = data["layers"]
#except:
#    print("Failed to open file.")
#    # todo in future turn on pcb led to tell error
#keyboard.keymap = [
#    [
#      KC.ESC,  KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,            KC.N6,  KC.N7, KC.N8,   KC.N9,  KC.N0,   KC.BSPC,
#      KC.TAB,  KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,             KC.Y,   KC.U,  KC.I,    KC.O,   KC.P,    KC.MINS,
#      KC.LSFT, KC.A,  KC.S,  KC.D,  KC.F,  KC.G,             KC.H,   KC.J,  KC.K,    KC.L,   KC.SCLN, KC.QUOT,
#      KC.LCTL, KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,             KC.N,   KC.M,  KC.COMM, KC.DOT, KC.SLSH, KC.BSLS,
#      KC.NO,   KC.NO, KC.A,  KC.B,  KC.C,  KC.D,             KC.M,   KC.L,  KC.J,    KC.I,   KC.NO,   KC.NO,
#      KC.NO,   KC.NO, KC.E,  KC.F,  KC.G,  KC.H,             KC.Q,   KC.P,  KC.O,    KC.N,   KC.NO,   KC.NO,
#    ],
    # Original
    #[
    #  KC.ESC,  KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,            KC.N6,  KC.N7, KC.N8,   KC.N9,  KC.N0,   KC.BSPC,
    #  KC.TAB,  KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,             KC.Y,   KC.U,  KC.I,    KC.O,   KC.P,    KC.MINS,
    #  KC.LSFT, KC.A,  KC.S,  KC.D,  KC.F,  KC.G,             KC.H,   KC.J,  KC.K,    KC.L,   KC.SCLN, KC.QUOT,
    #  KC.LCTL, KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,             KC.N,   KC.M,  KC.COMM, KC.DOT, KC.SLSH, KC.BSLS,
    #                  KC.A,  KC.B,                                          KC.J,    KC.I,
    #                                KC.C,  KC.D,                   KC.M, KC.L,
    #                                       KC.E, KC.F,       KC.O, KC.N,
    #                                       KC.G, KC.H,       KC.Q, KC.P
    #],
#]


