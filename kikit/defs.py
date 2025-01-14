from enum import Enum, IntEnum
from .units import mm, inch
from pcbnewTransition import isV9

# These classes miss in the exported interface

class Layer(IntEnum):
    if isV9():
        F_Cu = 0
        B_Cu = 2
        In1_Cu = 4
        In2_Cu = 6
        In3_Cu = 8
        In4_Cu = 10
        In5_Cu = 12
        In6_Cu = 14
        In7_Cu = 16
        In8_Cu = 18
        In9_Cu = 20
        In10_Cu = 22
        In11_Cu = 24
        In12_Cu = 26
        In13_Cu = 28
        In14_Cu = 30
        In15_Cu = 32
        In16_Cu = 34
        In17_Cu = 36
        In18_Cu = 38
        In19_Cu = 40
        In20_Cu = 42
        In21_Cu = 44
        In22_Cu = 46
        In23_Cu = 48
        In24_Cu = 50
        In25_Cu = 52
        In26_Cu = 54
        In27_Cu = 56
        In28_Cu = 58
        In29_Cu = 60
        In30_Cu = 62
        B_Adhes = 11
        F_Adhes = 9
        B_Paste = 15
        F_Paste = 13
        B_SilkS = 7
        F_SilkS = 5
        B_Mask = 3
        F_Mask = 1
        Dwgs_User = 17
        Cmts_User = 19
        Eco1_User = 21
        Eco2_User = 23
        Edge_Cuts = 25
        Margin = 27
        B_CrtYd = 29
        F_CrtYd = 31
        B_Fab = 33
        F_Fab = 35
        User_1 = 39
        User_2 = 41
        User_3 = 43
        User_4 = 45
        User_5 = 47
        User_6 = 49
        User_7 = 51
        User_8 = 53
        User_9 = 55
    else:
        F_Cu = 0
        B_Cu = 31
        In1_Cu = 1
        In2_Cu = 2
        In3_Cu = 3
        In4_Cu = 4
        In5_Cu = 5
        In6_Cu = 6
        In7_Cu = 7
        In8_Cu = 8
        In9_Cu = 9
        In10_Cu = 10
        In11_Cu = 11
        In12_Cu = 12
        In13_Cu = 13
        In14_Cu = 14
        In15_Cu = 15
        In16_Cu = 16
        In17_Cu = 17
        In18_Cu = 18
        In19_Cu = 19
        In20_Cu = 20
        In21_Cu = 21
        In22_Cu = 22
        In23_Cu = 23
        In24_Cu = 24
        In25_Cu = 25
        In26_Cu = 26
        In27_Cu = 27
        In28_Cu = 28
        In29_Cu = 29
        In30_Cu = 30
        B_Adhes = 32
        F_Adhes = 33
        B_Paste = 34
        F_Paste = 35
        B_SilkS = 36
        F_SilkS = 37
        B_Mask = 38
        F_Mask = 39
        Dwgs_User = 40
        Cmts_User = 41
        Eco1_User = 42
        Eco2_User = 43
        Edge_Cuts = 44
        Margin = 45
        B_CrtYd = 46
        F_CrtYd = 47
        B_Fab = 48
        F_Fab = 49
        User_1 = 50
        User_2 = 51
        User_3 = 52
        User_4 = 53
        User_5 = 54
        User_6 = 55
        User_7 = 56
        User_8 = 57
        User_9 = 58

    @staticmethod
    def allCu():
        if isV9():
           return list(range(0, 64, 2))
        return list(range(Layer.F_Cu, Layer.B_Cu + 1))

    @staticmethod
    def all():
        if isV9():
           return list(range(0, 63))
        return list(range(Layer.F_Cu, Layer.User_4 + 1))

    @staticmethod
    def allTech():
        if isV9():
           return [Layer.B_Adhes, Layer.F_Adhes, Layer.B_Paste, Layer.F_Paste, Layer.B_SilkS, Layer.F_SilkS, Layer.B_Mask,
                   Layer.F_Mask, Layer.Dwgs_User, Layer.Cmts_User, Layer.Eco1_User, Layer.Eco2_User, Layer.Edge_Cuts,
                   Layer.Margin, Layer.B_CrtYd, Layer.F_CrtYd, Layer.B_Fab, Layer.F_Fab, Layer.User_1, Layer.User_2,
                   Layer.User_3, Layer.User_4, Layer.User_5, Layer.User_6, Layer.User_7, Layer.User_8, Layer.User_9]
        return list(x for x in range(Layer.Dwgs_User, Layer.User_4 + 1))

    @staticmethod
    def allSilk():
        return [Layer.F_SilkS, Layer.B_SilkS]

class STROKE_T(IntEnum):
    S_SEGMENT = 0
    S_RECT = 1
    S_ARC = 2
    S_CIRCLE = 3
    S_POLYGON = 4
    S_CURVE = 5

class EDA_TEXT_HJUSTIFY_T(IntEnum):
    GR_TEXT_HJUSTIFY_LEFT   = -1
    GR_TEXT_HJUSTIFY_CENTER = 0
    GR_TEXT_HJUSTIFY_RIGHT  = 1

class EDA_TEXT_VJUSTIFY_T(IntEnum):
    GR_TEXT_VJUSTIFY_TOP    = -1
    GR_TEXT_VJUSTIFY_CENTER = 0
    GR_TEXT_VJUSTIFY_BOTTOM = 1

class MODULE_ATTR_T(IntEnum):
    MOD_DEFAULT = 0,
    MOD_CMS     = 1
    MOD_VIRTUAL = 2

PAPER_SIZES = [f"A{size}" for size in range(6)] + ["A", "B", "C", "D", "E"] + \
              ["USLetter", "USLegal", "USLedger"]
PAPER_SIZES = PAPER_SIZES + [f"{paper}-portrait" for paper in PAPER_SIZES]

PAPER_DIMENSIONS = {
    "A5": (210 * mm, 148 * mm),
    "A4": (297 * mm, 210 * mm),
    "A3": (420 * mm, 297 * mm),
    "A2": (594 * mm, 420 * mm),
    "A1": (841 * mm, 594 * mm),
    "A0": (1198 * mm, 841 * mm),
    "A": (11 * inch, 8.5 * inch),
    "B": (17 * inch, 11 * inch),
    "C": (22 * inch, 17 * inch),
    "D": (34 * inch, 22 * inch),
    "E": (44 * inch, 34 * inch),
    "USLetter": (11 * inch, 8.5 * inch),
    "USLegal": (14 * inch, 8.5 * inch),
    "USLedger": (17 * inch, 11 * inch)
}
