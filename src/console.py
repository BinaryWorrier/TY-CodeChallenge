"""
Helpers for drawing on the screen and reading the keyboard.

You don't need to change this file, or understand how it works inside.
It does the fiddly bits that are different on Windows, Mac and Linux, so the
rest of the game can just say things like:

    console.clear()
    console.set_cursor_position(10, 5)
    console.write("@")

    if console.key_available():
        key = console.read_key()

It needs a real terminal window, such as the terminal inside VS Code.
IDLE won't work.

For the curious: it works by sending "ANSI escape codes" to the terminal.
These are bits of text, starting with the Escape character, that tell the
terminal to do something (move the cursor, change colour...) instead of
printing letters.
"""

import atexit
import os
import shutil
import sys

ESC = "\033"

# The colours you can use with set_colour and set_background_colour.
COLOURS = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
    "grey": 90,
    "bright_red": 91,
    "bright_green": 92,
    "bright_yellow": 93,
    "bright_blue": 94,
    "bright_magenta": 95,
    "bright_cyan": 96,
    "bright_white": 97,
}


class OffTheScreenError(Exception):
    """Happens when you try to put the cursor somewhere that isn't on the screen."""


# ---------------------------------------------------------------------------
# The screen
# ---------------------------------------------------------------------------


def clear():
    """Wipes the screen and puts the cursor in the top-left corner."""
    _mark_screen_used()
    _send(ESC + "[2J" + ESC + "[H")


def write(text):
    """Writes text where the cursor is. Unlike print, it doesn't start a new line."""
    _send(str(text))


def set_cursor_position(column, row):
    """
    Moves the cursor to a column (across) and a row (down).
    Counting starts at 0 in the top-left corner. Column first, then row!
    """
    _check_whole_number("column", column)
    _check_whole_number("row", row)

    width, height = _window_size()
    if column < 0 or column >= width or row < 0 or row >= height:
        raise OffTheScreenError(
            f"Can't move the cursor to column {column}, row {row}, because that's off the screen. "
            f"The screen has columns 0 to {width - 1} and rows 0 to {height - 1}."
        )

    _mark_screen_used()
    # The terminal counts from 1 instead of 0, and wants the row first.
    _send(f"{ESC}[{row + 1};{column + 1}H")


def hide_cursor():
    """Hides the flashing cursor."""
    _mark_screen_used()
    _send(ESC + "[?25l")


def show_cursor():
    """Brings the flashing cursor back."""
    _send(ESC + "[?25h")


def window_width():
    """How many columns wide the window is."""
    return _window_size()[0]


def window_height():
    """How many rows tall the window is."""
    return _window_size()[1]


def set_colour(name):
    """Changes the colour of the text you write next, for example set_colour("green")."""
    _send(f"{ESC}[{_colour_code(name)}m")


def set_background_colour(name):
    """Changes the colour behind the text you write next, for example set_background_colour("blue")."""
    _send(f"{ESC}[{_colour_code(name) + 10}m")


def reset_colour():
    """Goes back to the normal colours."""
    _send(ESC + "[0m")


def beep():
    """Makes a beep. If you hear nothing, check your volume."""
    _beep()


# ---------------------------------------------------------------------------
# The keyboard
# ---------------------------------------------------------------------------


def key_available():
    """True if a key has been pressed and is waiting to be read. It never waits."""
    _check_terminal()
    return _key_waiting()


def read_key():
    """
    Waits for a key to be pressed, and gives back its name. You'll get one of:

        "up", "down", "left", "right"       the arrow keys
        "escape", "enter", "space", "tab", "backspace"
        "a", "w", "7", "?" ...              letters (always lowercase), numbers and symbols
        "unknown"                           anything else, such as F1

    The key isn't printed on the screen.
    """
    _check_terminal()
    return _read_key()


# ---------------------------------------------------------------------------
# Everything below here is the behind-the-scenes part.
# ---------------------------------------------------------------------------

_sent_anything = False
_screen_used = False

_KEY_NAMES = {
    "\x1b": "escape",
    "\r": "enter",
    "\n": "enter",
    " ": "space",
    "\t": "tab",
    "\x08": "backspace",
    "\x7f": "backspace",
}


def _send(text):
    global _sent_anything
    _check_terminal()
    _sent_anything = True
    sys.stdout.write(text)
    sys.stdout.flush()


def _mark_screen_used():
    global _screen_used
    _screen_used = True


def _window_size():
    size = shutil.get_terminal_size()
    return size.columns, size.lines


def _check_whole_number(name, value):
    if isinstance(value, int) and not isinstance(value, bool):
        return

    message = f"The {name} has to be a whole number (an int), but it was {value!r}."
    if isinstance(value, float):
        message += " Did you divide with / ? Use // instead to get a whole number."
    raise TypeError(message)


def _colour_code(name):
    if isinstance(name, str) and name.lower() in COLOURS:
        return COLOURS[name.lower()]
    raise ValueError(f"There's no colour called {name!r}. Try one of these: {', '.join(COLOURS)}")


def _check_terminal():
    if "idlelib" in sys.modules:
        raise RuntimeError(
            "The Snake game needs a real terminal window, and IDLE isn't one. "
            "Open the terminal in VS Code (or Windows Terminal), go to the project folder, "
            "and type: python src/main.py"
        )


def _name_of(character):
    if character == "\x03":  # Ctrl+C
        raise KeyboardInterrupt
    if character in _KEY_NAMES:
        return _KEY_NAMES[character]
    if character.isprintable():
        return character.lower()
    return "unknown"


if os.name == "nt":
    # ----- Windows -----
    import ctypes
    import msvcrt
    import winsound

    # The arrow keys send two characters: first 0 or 224, then one of these.
    _WINDOWS_ARROWS = {"H": "up", "P": "down", "K": "left", "M": "right"}

    def _beep():
        # Plays the Windows "ding" without stopping the game. (Terminals often have their own beep muted.)
        winsound.MessageBeep()

    def _start_terminal():
        # Windows 10 and 11 understand escape codes, but only once they're switched on.
        try:
            kernel32 = ctypes.windll.kernel32
            kernel32.GetStdHandle.restype = ctypes.c_void_p
            kernel32.GetConsoleMode.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
            kernel32.SetConsoleMode.argtypes = [ctypes.c_void_p, ctypes.c_uint32]

            screen = kernel32.GetStdHandle(-11)  # -11 means "standard output"
            mode = ctypes.c_uint32()
            if kernel32.GetConsoleMode(screen, ctypes.byref(mode)):
                kernel32.SetConsoleMode(screen, mode.value | 0x0004)  # 4 means "understand escape codes"
        except Exception:
            pass

    def _stop_terminal():
        pass

    def _key_waiting():
        return bool(msvcrt.kbhit())

    def _read_key():
        character = msvcrt.getwch()
        if character in ("\x00", "\xe0"):
            return _WINDOWS_ARROWS.get(msvcrt.getwch(), "unknown")
        return _name_of(character)

else:
    # ----- Mac and Linux -----
    import select
    import termios
    import tty

    # The arrow keys send Escape, then [ or O, then one of these letters.
    _ARROW_LETTERS = {"A": "up", "B": "down", "C": "right", "D": "left"}

    _saved_settings = None
    _input_finished = False

    def _beep():
        _send("\a")

    def _start_terminal():
        pass

    def _start_reading_keys():
        # Normally the terminal waits for Enter and prints what you type.
        # "cbreak" mode gives us each key straight away, without printing it.
        global _saved_settings
        if _saved_settings is None and sys.stdin.isatty():
            _saved_settings = termios.tcgetattr(sys.stdin.fileno())
            tty.setcbreak(sys.stdin.fileno())

    def _stop_terminal():
        global _saved_settings
        if _saved_settings is not None:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, _saved_settings)
            _saved_settings = None

    def _bytes_waiting(seconds):
        ready, _, _ = select.select([sys.stdin.fileno()], [], [], seconds)
        return bool(ready)

    def _read_byte():
        global _input_finished
        data = os.read(sys.stdin.fileno(), 1)
        if not data:
            _input_finished = True
        return data

    def _key_waiting():
        _start_reading_keys()
        return not _input_finished and _bytes_waiting(0)

    def _read_key():
        _start_reading_keys()
        first = b"" if _input_finished else _read_byte()
        if not first:
            # There's nothing left to read, so act as if Escape was pressed.
            return "escape"
        if first == b"\x1b":
            return _read_escape_sequence()

        # Some characters, such as é, are more than one byte long.
        data = first
        for _ in range(_extra_bytes(first[0])):
            data += _read_byte()
        return _name_of(data.decode("utf-8", errors="replace"))

    def _read_escape_sequence():
        # Pressing Escape sends Escape on its own. The arrow keys send Escape
        # with more characters straight after it, so wait a moment to see which.
        if not _bytes_waiting(0.05):
            return "escape"
        if _read_byte() not in (b"[", b"O"):
            return "unknown"

        # Some keys send numbers before the final letter, such as Escape [ 1 ; 5 A.
        while True:
            byte = _read_byte()
            if not byte:
                return "unknown"
            if 0x40 <= byte[0] <= 0x7E:
                return _ARROW_LETTERS.get(byte.decode(), "unknown")

    def _extra_bytes(first_byte):
        if first_byte >= 0xF0:
            return 3
        if first_byte >= 0xE0:
            return 2
        if first_byte >= 0xC0:
            return 1
        return 0


def _tidy_up():
    # Put the colours, cursor and keyboard back to normal when the program ends.
    if _sent_anything:
        sys.stdout.write(ESC + "[0m" + ESC + "[?25h")
        sys.stdout.flush()
    _stop_terminal()


_original_excepthook = sys.excepthook


def _excepthook(kind, error, traceback):
    # If the program crashes, tidy up first so the error message is easy to read.
    try:
        _tidy_up()
        if _screen_used:
            # Jump to the bottom row, so the message appears underneath the game.
            sys.stdout.write(f"{ESC}[{_window_size()[1]};1H\n")
            sys.stdout.flush()
    except Exception:
        pass

    if issubclass(kind, KeyboardInterrupt):
        print("Stopped (you pressed Ctrl+C).")
        return
    _original_excepthook(kind, error, traceback)


_start_terminal()
atexit.register(_tidy_up)
sys.excepthook = _excepthook
