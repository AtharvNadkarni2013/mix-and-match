from enum import Enum, auto


class Colors(Enum):
    empty = auto()
    red = auto()
    orange = auto()
    yellow = auto()
    green = auto()
    blue = auto()
    purple = auto()


mixAndMatchDict = {
    Colors.red: {
        Colors.red: Colors.red,
        Colors.yellow: Colors.orange,
        Colors.blue: Colors.purple
    },
    Colors.yellow: {
        Colors.red: Colors.orange,
        Colors.yellow: Colors.yellow,
        Colors.blue: Colors.green
    },
    Colors.blue: {
        Colors.red: Colors.purple,
        Colors.yellow: Colors.green,
        Colors.blue: Colors.blue
    }
}


def mixRed(s: Colors):
    if s != Colors.empty:
        return mixAndMatchDict[Colors.red][s]
    else:
        return Colors.red


def mixYellow(s: Colors):
    if s != Colors.empty:
        return mixAndMatchDict[Colors.yellow][s]
    else:
        return Colors.yellow


def mixBlue(s: Colors):
    if s != Colors.empty:
        return mixAndMatchDict[Colors.blue][s]
    else:
        return Colors.blue


def mixAndMatch(s: Colors, colors: str):
    for c in colors:
        c = c.lower()
        if c == "r":
            s = mixRed(s)
        elif c == "y":
            s = mixYellow(s)
        elif c == "b":
            s = mixBlue(s)
        elif c == "":
            s = s
        else:
            raise ValueError("Invalid")
    return s


def main():
    assert mixAndMatch(Colors.empty, "") is Colors.empty
    assert mixAndMatch(Colors.empty, "r") is Colors.red
    assert mixAndMatch(Colors.empty, "y") is Colors.yellow
    assert mixAndMatch(Colors.empty, "b") is Colors.blue
    assert mixAndMatch(Colors.empty, "ry") is Colors.orange
    assert mixAndMatch(Colors.empty, "rb") is Colors.purple
    assert mixAndMatch(Colors.empty, "rr") is Colors.red
    assert mixAndMatch(Colors.empty, "yb") is Colors.green
    assert mixAndMatch(Colors.empty, "by") is Colors.green
    assert mixAndMatch(Colors.empty, "br") is Colors.purple


if __name__ == "__main__":
    main()
