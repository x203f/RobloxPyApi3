from enum import Enum
class Color3(Enum):
    new = 0
    fromRGB = 1
    fromHex = 2
    fromHSV = 3
class DefaultPropertyTypes(Enum):
    string = 0
    number = 1

    bool = 2
class BrickColor(Enum):
    new = 0

    Palette = 10
class UDim2(Enum):
    new = 0
    fromscale = 1
    fromoffset = 2
class BrickColor_Shorthanded(Enum):
    Random = 1
    Red = 2
    White = 3
    Gray = 4
    DarkGray = 5
    Black = 6
    Yellow = 7
    Green = 8
    Blue = 9