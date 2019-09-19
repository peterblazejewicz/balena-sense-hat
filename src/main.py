from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import signal
import atexit
import sys

x: int = 3  # type: int
y: int = 3

def clamp(value: int, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    if event.action != ACTION_RELEASED:
        global y
        y = clamp(y - 1)

def pushed_down(event):
    if event.action != ACTION_RELEASED:
        global y
        y = clamp(y + 1)

def pushed_left(event):
    if event.action != ACTION_RELEASED:
        global x
        x = clamp(x - 1)

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        global x
        x = clamp(x + 1)

def refresh():
    sense.clear()
    sense.set_pixel(x, y, 255, 255, 255)

@atexit.register
def clearAtExit(*arg):
    sense.clear()

if __name__ == '__main__':
    sense: SenseHat = SenseHat()
    sense.clear()
    sense.stick.direction_up = pushed_up
    sense.stick.direction_down = pushed_down
    sense.stick.direction_left = pushed_left
    sense.stick.direction_right = pushed_right
    sense.stick.direction_any = refresh

    signal.signal(signal.SIGINT, clearAtExit)
    signal.signal(signal.SIGTERM, clearAtExit)

    refresh()
    pause()
