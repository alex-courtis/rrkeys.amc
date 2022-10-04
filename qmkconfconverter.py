from kmk.keys import KC

qmk_kmk_map = {
    "KC.BTN1": "KC.MB_LMB",
    "KC.BTN2": "KC.MB_RMB",
    "KC.BTN3": "KC.MB_MMB",
    "KC.WH_U": "KC.MW_UP",
    "KC.WH_D": "KC.MW_DOWN",
    "KC.MS_L": "KC.MS_LEFT",
    "KC.MS_R": "KC.MS_RIGHT",
    "KC.MS_U": "KC.MS_UP",
    "KC.MS_D": "KC.MS_DOWN",
}

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
            
            if k in qmk_kmk_map:
                k = qmk_kmk_map.get(k)

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