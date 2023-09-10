#!/usr/bin/env python3

from draw import Drawer

layout = {
    "base":
    [
        """
        | &kp ESC   | &kp Q    | &kp W    | &kp E    | &kp R   | &kp T     |           |
        | &kp TAB   | &kp A    | &kp S    | &kp D    | &kp F   | &kp G     |           |
        | &kp LSHFT | &kp Z    | &kp X    | &kp C    | &kp V   | &kp B     |           |
        | &kp LCTRL | &kp LGUI | &kp LALT | &kp LALT | &mo NAV | &mo LOWER | &kp SPACE |
        """,
        """
        |         | &kp Y     | &kp U   | &kp I     | &kp O    | &kp P     | &kp BSPC  |
        |         | &kp H     | &kp J   | &kp K     | &kp L    | &kp SEMI  | &kp SQT   |
        |         | &kp N     | &kp M   | &kp COMMA | &kp DOT  | &kp SLASH | &kp RSHFT |
        | &kp RET | &mo LOWER | &mo NAV | &kp RALT  | &kp RALT | &kp RGUI  | &kp RCTRL |
        """
    ],

    "nav":
    [
        """
        | &trans | &kp F1 | &kp F2     | &kp F3 | &kp F4 | &kp F5    |        |
        | &trans | &none  | &none      | &none  | &none  | &kp F11   |        |
        | &trans | &none  | &none      | &none  | &none  | &kp K_APP |        |
        | &trans | &trans | &tog MOUSE | &trans | &trans | &trans    | &trans |
        """,
        """
        |        | &kp F6    | &kp F7   | &kp F8    | &kp F9    | &kp F10   | &trans  |
        |        | &kp F12   | &kp LEFT | &kp DOWN  | &kp UP    | &kp RIGHT | &kp INS |
        |        | &kp K_APP | &kp HOME | &kp PG_DN | &kp PG_UP | &kp END   | &trans  |
        | &trans | &trans    | &trans   | &trans    | &tog MISC | &trans    | &trans  |
        """
    ],

    "lower":
    [
        """
        | &kp GRAVE | &kp N1    | &kp N2        | &kp N3        | &kp N4        | &kp N5 |        |
        | &trans    | &kp PSCRN | &none         | &none         | &none         | &none  |        |
        | &trans    | &none     | &kp LC(LS(X)) | &kp LC(LS(C)) | &kp LC(LS(V)) | &none  |        |
        | &trans    | &trans    | &tog MOUSE    | &trans        | &trans        | &trans | &trans |
        """,
        """
        |        | &kp N6    | &kp N7    | &kp N8    | &kp N9    | &kp N0   | &kp DEL  |
        |        | &kp TILDE | &kp MINUS | &kp EQUAL | &kp LBKT  | &kp RBKT | &kp BSLH |
        |        | &none     | &none     | &none     | &kp LT    | &kp GT   | &trans   |
        | &trans | &trans    | &trans    | &trans    | &tog MISC | &trans   | &trans   |
        """
    ],

    "misc":
    [
        """
        | &to CONF | &none      | &none      | &none        | &none        | &none      |        |
        | &kp C_PP | &kp C_PREV | &kp C_NEXT | &kp C_VOL_DN | &kp C_VOL_UP | &kp C_MUTE |        |
        | &trans   | &none      | &none      | &none        | &none        | &none      |        |
        | &trans   | &trans     | &tog MISC  | &trans       | &trans       | &trans     | &trans |
        """,
        """
        |              | &kp KP_NLCK | &kp KP_N7 | &kp KP_N8 | &kp KP_N9 | &kp KP_MULTIPLY | &kp KP_MINUS |
        |              | &none       | &kp KP_N4 | &kp KP_N5 | &kp KP_N6 | &kp KP_DIVIDE   | &kp KP_PLUS  |
        |              | &kp KP_N0   | &kp KP_N1 | &kp KP_N2 | &kp KP_N3 | &kp KP_DOT      | &trans       |
        | &kp KP_ENTER | &trans      | &trans    | &trans    | &tog MISC | &trans          | &trans       |
        """
    ],

    "mouse":
    [
        """
        | &to CONF | &none | &none      | &none | &none | &none |       |
        | &none    | &none | &none      | &none | &none | &none |       |
        | &none    | &none | &none      | &none | &none | &none |       |
        | &none    | &none | &tog MOUSE | &none | &none | &none | &none |
        """,
        """
        |       | &none | &none | &none | &none      | &none | &none |
        |       | &none | &none | &none | &none      | &none | &none |
        |       | &none | &none | &none | &none      | &none | &none |
        | &none | &none | &none | &none | &tog MOUSE | &none | &none |
        """
    ],

    "conf":
    [
        """
        | &to BASE | &bt BT_SEL 0 | &bt BT_SEL 1 | &bt BT_SEL 2 | &bt BT_SEL 3      | &bt BT_SEL 4 |       |
        | &none    | &bt BT_CLR   | &none        | &none        | &ext_power EP_TOG | &sys_reset   |       |
        | &none    | &out OUT_BLE | &out OUT_USB | &none        | &none             | &bootloader  |       |
        | &none    | &none        | &none        | &none        | &none             | &none        | &none |
        """,
        """
        |       | &none       | &none | &none | &none | &none | &to BASE |
        |       | &sys_reset  | &none | &none | &none | &none | &none    |
        |       | &bootloader | &none | &none | &none | &none | &none    |
        | &none | &none       | &none | &none | &none | &none | &none    |
        """
    ],
}


def get_layer_strings(layer):
    left_lines = [s.strip()[:-1].split("|")[1:] for s in layer[0].strip().split("\n")]
    left = ["".join(seg) for seg in left_lines]
    right_lines = [s.strip().split("|")[:-1] for s in layer[1].strip().split("\n")]
    right = ["".join(seg) for seg in right_lines]
    return [((l+r).strip()) for (l, r) in zip(left, right)]


if __name__ == "__main__":
    ofs = open("config/kbdkid3-keymap.overlay", "w")

    ofs.write("/*\n")
    ofs.write(" * Copyright (c) 2023 Tubbles\n")
    ofs.write(" *\n")
    ofs.write(" * SPDX-License-Identifier: MIT\n")
    ofs.write(" */\n")
    ofs.write("\n")
    ofs.write("#include <behaviors.dtsi>\n")
    ofs.write("#include <dt-bindings/zmk/bt.h>\n")
    ofs.write("#include <dt-bindings/zmk/ext_power.h>\n")
    ofs.write("#include <dt-bindings/zmk/keys.h>\n")
    ofs.write("#include <dt-bindings/zmk/outputs.h>\n")
    ofs.write("\n")

    layer_serial = 0
    for layer in layout:
        ofs.write(f"#define {layer.upper():<7} {layer_serial}\n")
        layer_serial += 1

    ofs.write("\n")
    ofs.write("/ {\n")
    ofs.write("    keymap {\n")
    ofs.write("        compatible = \"zmk,keymap\";\n")

    for layer, keylist in layout.items():
        layer_string = "\n                ".join(get_layer_strings(keylist))
        ofs.write(f"        {layer}_layer " + "{\n")
        ofs.write("            bindings = <\n")
        ofs.write(f"                {layer_string}\n")
        ofs.write("            >;\n")
        ofs.write("        };\n")

    ofs.write("    };\n")
    ofs.write("};\n")

    ofs.close()

    drawer = Drawer(14, 4, layout)
    drawer.save("layouts.png")
