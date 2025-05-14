#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Drawer:
    def __init__(self, num_columns, num_rows, layout):
        self._num_columns = num_columns
        self._num_rows = num_rows
        self._layout = layout
        self._num_layouts = len(layout)
        self.size = 60
        self.padding = 5
        self.stride = self.size + self.padding
        self._im = Image.new(
            "RGB",
            (
                self.stride * self._num_columns + self.padding,
                int((self.stride * (self._num_rows + 1) + self.padding) * self._num_layouts - 0.3 * self.stride),
            ),
            "gray",
        )
        self._draw = ImageDraw.Draw(self._im)
        font = "DejaVuSans.ttf"
        self._fonts = [
            ImageFont.truetype(font, size=10),
            ImageFont.truetype(font, size=14),
            ImageFont.truetype(font, size=20),
            ImageFont.truetype(font, size=26),
            ImageFont.truetype(font, size=30),
        ]

        self._label_table = {
            "BSLH": "|\n\\",
            "BSPC": "⌫",
            "C_BRI_DN": "🔅",
            "C_BRI_UP": "🔆",
            "C_MUTE": "🔇",
            "C_NEXT": "⏭",
            "C_PP": "⏯",
            "C_PREV": "⏮",
            "C_VOL_DN": "🔉",
            "C_VOL_UP": "🔊",
            "COMMA": "<\n,",
            "DOT": ">\n.",
            "DOWN": "↓",
            "EQUAL": "+\n=",
            "GRAVE": "`\n~",
            "GT": ">",
            "K_APP": "🗉",
            "KP_DIVIDE": "KP /",
            "KP_DOT": "KP .",
            "KP_ENTER": "KP ⏎",
            "KP_MINUS": "KP -",
            "KP_MULTIPLY": "KP *",
            "KP_N0": "KP 0",
            "KP_N1": "KP 1",
            "KP_N2": "KP 2",
            "KP_N3": "KP 3",
            "KP_N4": "KP 4",
            "KP_N5": "KP 5",
            "KP_N6": "KP 6",
            "KP_N7": "KP 7",
            "KP_N8": "KP 8",
            "KP_N9": "KP 9",
            "KP_NLCK": "NUM\nLOCK",
            "KP_PLUS": "KP +",
            "LBKT": "{\n[",
            "LBRC": "{",
            "LEFT": "←",
            "LT": "<",
            "MINUS": "_\n-",
            "N0": ")\n0",
            "N1": "!\n1",
            "N2": "@\n2",
            "N3": "#\n3",
            "N4": "$\n4",
            "N5": "%\n5",
            "N6": "^\n6",
            "N7": "&\n7",
            "N8": "*\n8",
            "N9": "(\n9",
            "PG_DN": "PAGE\nDOWN",
            "PG_UP": "PAGE\nUP",
            "PLUS": "+",
            "PSCRN": "PRINT\nSCREEN",
            "RBKT": "}\n]",
            "RBRC": "}",
            "RET": "⏎",
            "RIGHT": "→",
            "SEMI": ":\n;",
            "SLASH": "?\n/",
            "SQT": "\"\n'",
            "TAB": "↹",
            "TILDE": "~",
            "trans": "⇩",
            "UNDER": "_",
            "UP": "↑",
        }

        emoji_fonts = [
            ImageFont.truetype("fonts/Noto_Emoji/static/NotoEmoji-Regular.ttf", size=18),
            ImageFont.truetype("fonts/Noto_Emoji/static/NotoEmoji-Regular.ttf", size=20),
        ]
        symbol_font2 = ImageFont.truetype("fonts/Noto_Sans_Symbols_2/NotoSansSymbols2-Regular.ttf", size=26)
        self._font_table = {
            "🔇": symbol_font2,
            "⏭": symbol_font2,
            "⏯": symbol_font2,
            "⏮": symbol_font2,
            "🔉": symbol_font2,
            "🔊": symbol_font2,
            "📷": symbol_font2,
            "🗉": symbol_font2,
            "🔅": emoji_fonts[0],
            "🔆": emoji_fonts[1],
            "⌫": self._fonts[2],
        }

        self._fill_table = {
            "⇩": (192, 192, 192),
        }

        self._draw_layout()

    def _draw_name(self, index, name):
        y = self.padding + index * (self._num_rows + 1) * self.stride - 0.1 * self.stride
        font = self._fonts[4]
        self._draw.text((self.padding, y + self.padding), f"{name} ({index})", fill="black", font=font)

    def _draw_button(self, index, side, x, y, label):
        x = x * self.stride + self.padding + side * 7 * self.stride
        y = y * self.stride + self.padding + index * 5 * self.stride + 0.5 * self.stride

        if label in self._label_table:
            label = self._label_table[label]

        fill = "black"
        if label in self._fill_table:
            fill = self._fill_table[label]

        font = self._fonts[0]
        if len(label) < 6:
            font = self._fonts[1]
        if len(label) < 4:
            font = self._fonts[2]
        if len(label) < 2:
            font = self._fonts[3]
        if label in self._font_table:
            font = self._font_table[label]

        self._draw.rounded_rectangle([x, y, x + self.size, y + self.size], 5, "white", "black", 2)
        self._draw.text((x + self.padding, y + self.padding), label, fill=fill, font=font)

    def _draw_layout(self):
        for index, (layer, keylist) in enumerate(self._layout.items()):
            self._draw_name(index, layer)
            for side_index, side in enumerate(keylist):
                for line_index, line in enumerate(side.splitlines()[1:]):
                    keys = line.split("|")
                    for key_index, key in enumerate(keys[1:]):
                        key = key.strip()
                        if key and key != "":
                            key = key.replace("none", "")
                            key = key.replace("&kp ", "")
                            key = key.replace("&", "")
                            key = key.replace(" ", "\n")
                            self._draw_button(index, side_index, key_index, line_index, key)

    def save(self, path):
        self._im.save(path)
