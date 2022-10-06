def load():
  return default_config.replace('\n', '').replace('\t', '').replace(' ', '')

# Key codes listed here: https://github.com/KMKfw/kmk_firmware/blob/682731bfe130cad9bbf94117cacd59be0842a1af/docs/keycodes.md
default_config = """
[
  [
    KC.ESC,  KC.N1,   KC.N2,  KC.N3,    KC.N4,   KC.N5,      KC.N6,   KC.N7,  KC.N8,    KC.N9,   KC.N0,   KC.BSPC,
    KC.TAB,  KC.Q,    KC.W,   KC.E,     KC.R,    KC.T,       KC.Y,    KC.U,   KC.I,     KC.O,    KC.P,    KC.MINS,
    KC.LSFT, KC.A,    KC.S,   KC.D,     KC.F,    KC.G,       KC.H,    KC.J,   KC.K,     KC.L,    KC.SCLN, KC.QUOT,
    KC.LCTL, KC.Z,    KC.X,   KC.C,     KC.V,    KC.B,       KC.N,    KC.M,   KC.COMM,  KC.DOT,  KC.SLSH, KC.BSLS,
             KC.LBRC, KC.RBRC,                                                          KC.PLUS, KC.EQL,
                              KC.MO(2), KC.SPC,                       KC.ENT, KC.MO(1),
                                        KC.TAB,  KC.HOME,    KC.END,  KC.DEL,
                                        KC.BSPC, KC.GRV,     KC.LGUI, KC.LALT
  ],
  [
    KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC,    KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.DEL,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LBRC,    KC.RBRC, KC.P7,   KC.P8,   KC.P9,   KC.TRNS, KC.PLUS,
    KC.TRNS, KC.HOME, KC.PGUP, KC.PGDN, KC.END,  KC.LPRN,    KC.RPRN, KC.P4,   KC.P5,   KC.P6,   KC.MINS, KC.PIPE,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.P1,   KC.P2,   KC.P3,   KC.EQL,  KC.UNDS,
             KC.TRNS, KC.PSCR,                                                          KC.TRNS, KC.P0,
                               KC.TRNS, KC.TRNS,                      KC.TRNS, KC.TRNS,
                                        KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS,
                                        KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS
  ],
  [
    KC.F12,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,     KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LBRC,   KC.RBRC, KC.TRNS, KC.NLCK, KC.INS,  KC.SLCK, KC.MUTE,
    KC.TRNS, KC.LEFT, KC.UP,   KC.DOWN, KC.RGHT, KC.LPRN,   KC.RPRN, KC.MPRV, KC.MPLY, KC.MNXT, KC.TRNS, KC.VOLU,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.VOLD,
             KC.TRNS, KC.TRNS,                                                         KC.EQL,  KC.TRNS,
                               KC.TRNS, KC.TRNS,                              KC.TRNS, KC.TRNS,
                                        KC.TRNS, KC.TRNS,   KC.TRNS, KC.TRNS,
                                        KC.TRNS, KC.TRNS,   KC.TRNS, KC.TRNS
  ],
]
"""