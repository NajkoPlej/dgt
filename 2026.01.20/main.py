from browser import document
from browser.local_storage import storage
import json


btn_theme = document["btn_theme"]
theme_label = document["theme_label"]


inp = document["inp_item"]
btn_add = document["btn_add"]
btn_clear = document["btn_clear"]
btn_last = document["btn_last"]
out = document["out"]


items = []
theme = "light"
# TODO 1 vytvor premennú theme a pri štarte ju nastav z load_theme()
# theme = "light"


def render():
    if len(items) == 0:
        out.html = "<em>Zoznam je prázdny.</em>"
        return

    html = "<ul>"
    for it in items:
        html += f"<li>{it}</li>"
    html += "</ul>"
    out.html = html


def save_items():
    storage["todo_items"] = json.dumps(items)


def load_items():
    data = storage.get("todo_items")
    if data:
        return json.loads(data)
    return []


def add_item(ev):
    text = inp.value.strip()
    if text == "":
        out.html = "<em>Najprv napíš položku.</em>"
        return

    items.append(text)
    inp.value = ""
    render()
    save_items()


def clear_all(ev):
    items.clear()
    render()
    save_items()


def remove_last(ev):
    if len(items) == 0:
        out.html = "<em>Nie je čo zmazať.</em>"
        return
    items.pop()
    render()
    save_items()



def apply_theme(fn_theme_value):
    global theme_label #overim si farbu a 
    document.body.class_name = fn_theme_value #zmenim css calssname
    fn_theme_value.text = fn_theme_value #zmenim farbu na aku vybral pouzivatel
    


# TODO 3 doplň save_theme() a load_theme()
# - kľúč v storage: "theme"

def save_theme():
    pass


def load_theme():
    pass


# TODO 4 doplň toggle_theme()
# - prepni theme light/dark
# - zavolaj apply_theme(theme)
# - zavolaj save_theme()

def toggle_theme(ev=None):
    pass



btn_add.bind("click", add_item)
btn_clear.bind("click", clear_all)
btn_last.bind("click", remove_last)
btn_theme.bind("click", toggle_theme)

# (Pri hodnotení môže učiteľ požiadať o malú úpravu na preukázanie vedomostí)


items = load_items()
render()
# TODO 5 theme = load_theme(); apply_theme(theme)
