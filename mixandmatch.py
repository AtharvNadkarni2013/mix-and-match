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
    return mixAndMatchDict[0][s]


def mixYellow(s: Colors):
    return mixAndMatchDict[1][s]


def mixBlue(s: Colors):
    return mixAndMatchDict[2][s]


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
