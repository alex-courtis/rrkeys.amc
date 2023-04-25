from kmk.keys import KC
from qmkmapping import qmk_kmk_map, one_param_layers_starts, one_param_ctrl_shift_alt_starts

def key_startswith(key, array):
    for start in array:
        if key.startswith(start):
            return True
    return False


def lt_internal_finder(key, from_char, to_char):
    key = key[:]
    start = key.find(from_char)
    if start == -1:
        return "KC.NO"
    end = key.rfind(to_char)
    if end == -1:
        return "KC.NO"
    start += 1
    return key[start:end].strip()


def convert_lt_keycode(key):
    layer = lt_internal_finder(key, "(", ",")
    inner_kc = lt_internal_finder(key, ",", ")")

    if layer == "KC.NO" or inner_kc == "KC.NO":
        return "KC.NO"
    if inner_kc not in qmk_kmk_map:
        return "KC.NO"

    inner_kc = qmk_kmk_map.get(inner_kc)
    return "KC.LT(" + layer + "," + inner_kc + ")"


def load_file(file):
    import json
    f = open(file, "r")
    data = json.load(f)
    return data.get("layers")


def qmk_to_kmk(in_file):
    layers = load_file(in_file)

    content = "["
    for layer in layers:
        content += "["
        for key in layer:
            if key in qmk_kmk_map:
                k = qmk_kmk_map.get(key)

            elif key_startswith(key, one_param_layers_starts):
                k = "KC." + key

            elif key_startswith(key, one_param_ctrl_shift_alt_starts):
                split = key.split("(")
                key_main = "KC." + split[0] + "("
                sub_key = split[1]
                sub_key = sub_key[:-1]
                k = key_main + qmk_kmk_map.get(sub_key) + ")"

            elif key.startswith("LT("):
                k = convert_lt_keycode(key)

            elif key.startswith("KC_"):
                k = key.replace("_", ".", 1) # hope for the best...

            # TODO
            #KC.LM(layer, mod)
            content += k + ","
        content += "],"
    content += "]"
    return content


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
