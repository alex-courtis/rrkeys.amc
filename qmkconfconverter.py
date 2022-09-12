from kmk.keys import KC

def layer_converter(qmk_layer):
  layer = []
  # Assumes dactyl manuform 6x5 layout
  for i in range(0, 48):
    layer.append(qmk_layer[i])

  layer.append(KC.NO)
  layer.append(KC.NO)
  layer.append(qmk_layer[48])
  layer.append(qmk_layer[49])
  layer.append(qmk_layer[52])
  layer.append(qmk_layer[53])

  layer.append(qmk_layer[54])
  layer.append(qmk_layer[55])
  layer.append(qmk_layer[50])
  layer.append(qmk_layer[51])
  layer.append(KC.NO)
  layer.append(KC.NO)


  layer.append(KC.NO)
  layer.append(KC.NO)
  layer.append(qmk_layer[60])
  layer.append(qmk_layer[61])
  layer.append(qmk_layer[56])
  layer.append(qmk_layer[57])

  layer.append(qmk_layer[58])
  layer.append(qmk_layer[59])
  layer.append(qmk_layer[62])
  layer.append(qmk_layer[63])
  layer.append(KC.NO)
  layer.append(KC.NO)

  return layer

def layers_converter(qmk_layers):
  layers = []
  for qmk_layer in qmk_layers:
    layers.append(layer_converter(qmk_layer))
  return layers


def qmk_to_kmk(in_file):
    #get layers from file
    import json
    f = open(in_file, "r")
    data = json.load(f)
    layers = data.get("layers")

    content = "["

    for layer in layers:
        content += "["
        for key in layer:
            k = key.replace("_", ".", 1)

            # check if it is number. (Not very save this)
            if "KC" in k and k[3].isdigit():
                k = k[:3] + "N" + k[3:] # insert an N
            elif "MO(" in k:
                k= "KC." + k

            if k == "KC.BTN1":
                k = "KC.MB_LMB"
            elif k == "KC.BTN2":
                k = "KC.MB_RMB"
            elif k == "KC.BTN3":
                k = "KC.MB_MMB"
            elif k == "KC.WH_U":
                k = "KC.MW_UP"
            elif k == "KC.WH_D":
                k = "KC.MW_DOWN"
            elif k == "KC.MS_L":
                k = "KC.MS_LEFT"
            elif k == "KC.MS_R":
                k = "KC.MS_RIGHT"
            elif k == "KC.MS_U":
                k = "KC.MS_UP"
            elif k == "KC.MS_D":
                k = "KC.MS_DOWN"

            content += k + ","
        content += "],"

    content += "]"
    return content

# Convert from this:
#[
#  00_KC.ESC,  01_KC.N1, 02_KC.N2, 03_KC.N3, 04_KC.N4, 05_KC.N5,            06_KC.N6,  07_KC.N7, 08_KC.N8,   09_KC.N9,  10_KC.N0,   11_KC.BSPC,
#  12_KC.TAB,  13_KC.Q,  14_KC.W,  15_KC.E,  16_KC.R,  17_KC.T,             18_KC.Y,   19_KC.U,  20_KC.I,    21_KC.O,   22_KC.P,    23_KC.MINS,
#  24_KC.LSFT, 25_KC.A,  26_KC.S,  27_KC.D,  28_KC.F,  29_KC.G,             30_KC.H,   31_KC.J,  32_KC.K,    33_KC.L,   34_KC.SCLN, 35_KC.QUOT,
#  36_KC.LCTL, 37_KC.Z,  38_KC.X,  39_KC.C,  40_KC.V,  41_KC.B,             42_KC.N,   43_KC.M,  44_KC.COMM, 45_KC.DOT, 46_KC.SLSH, 47_KC.BSLS,
#                  48_KC.A,  49_KC.B,                                                   50_KC.J,    51_KC.I,
#                                52_KC.C,  53_KC.D,                            54_KC.M, 55_KC.L,
#                                       56_KC.E, 57_KC.F,                 58_KC.O, 59_KC.N,
#                                       60_KC.G, 61_KC.H,                 62_KC.Q, 63_KC.P
#],
# To This:
#[
#  KC.ESC,  KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,            KC.N6,  KC.N7, KC.N8,   KC.N9,  KC.N0,   KC.BSPC,
#  KC.TAB,  KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,             KC.Y,   KC.U,  KC.I,    KC.O,   KC.P,    KC.MINS,
#  KC.LSFT, KC.A,  KC.S,  KC.D,  KC.F,  KC.G,             KC.H,   KC.J,  KC.K,    KC.L,   KC.SCLN, KC.QUOT,
#  KC.LCTL, KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,             KC.N,   KC.M,  KC.COMM, KC.DOT, KC.SLSH, KC.BSLS,
#  KC.NO,   KC.NO, KC.A,  KC.B,  KC.C,  KC.D,             KC.M,   KC.L,  KC.J,    KC.I,   KC.NO,   KC.NO,
#  KC.NO,   KC.NO, KC.E,  KC.F,  KC.G,  KC.H,             KC.Q,   KC.P,  KC.O,    KC.N,   KC.NO,   KC.NO,
#
#],
