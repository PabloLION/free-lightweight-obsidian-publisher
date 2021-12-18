import eel
import EelExpose

global GUI_enabled
GUI_enabled = False


def check_GUI_enabled(func):
    if GUI_enabled:
        return func
    else:
        return lambda msg: print(
            "GUI is not enabled or not initiated yet, printing with Python console:"
            + msg
        )


def init_GUI():
    global GUI_enabled
    GUI_enabled = True
    eel.init("web")
    eel.start("app.html", size=(800, 800))


@check_GUI_enabled
def print_log(message):
    EelExpose.addText(message)


def expose(func):
    return eel.expose(func)
