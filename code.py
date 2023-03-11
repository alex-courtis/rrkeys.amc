# ---------------------------------------------------- Imports
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
import default_config
import utils

# ---------------------------------------------------- Keyboard setup
keyboard = KMKKeyboard()
keyboard.debug_enabled = False
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
# Append required modules as needed
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())

# ---------------------------------------------------- Load up keys configuration
#json_config = utils.get_first_json_file()
print('all files: ', utils.get_all_json_files())
json_config = utils.get_most_recent_json_file()
print("loading config: ", json_config)
str_data = QC.qmk_to_kmk(json_config) if json_config is not None else default_config.load()
layers = None
try:
    exec("layers = " + str_data)
except Exception as e:
    print("Failed to load configuration: ", e)
    str_data = default_config.load()
    exec("layers = " + str_data)
    # TODO add bellow without remounting pico
    #with open("errors", "w") as f:
    #    f.write(str(e))

keyboard.keymap = QC.layers_converter(layers)

# ---------------------------------------------------- Main
print("Running main")
if __name__ == '__main__':
	keyboard.go()
