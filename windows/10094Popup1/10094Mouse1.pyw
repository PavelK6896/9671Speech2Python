from ctypes import Structure, c_long
from ctypes import windll, wintypes, byref


def get_cursor_pos():
    cursor = wintypes.POINT()
    windll.user32.GetCursorPos(byref(cursor))
    return (cursor.x, cursor.y)


print(get_cursor_pos())


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return (pt.x, pt.y)


print(queryMousePosition())
