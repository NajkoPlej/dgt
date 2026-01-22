from browser import document

# TODO: STATUS
# Skús zmeniť text v prvku 'status' tak, aby si videl, že Brython beží.
document["status"].text = "Status: Fakčí to" #yes

# premenná na počítanie pozdravov
count = 0

def greet(ev):
    meno = document["inp_name"].value #fakci
    if meno == "":
        document["out"].text = "Napíš meno"#yess
    else:
        document["out"].text = f"Ahoj {meno}" #yesss
    """Spustí sa po kliknutí na tlačidlo."""
    # TODO: načítaj meno z inputu inp_name, ošetri prázdny vstup a vypíš do prvku out
    # Nápoveda: document["inp_name"].value
    # Nápoveda: document["out"].text = "..."
    pass

document["btn_greet"].bind("click", greet)
# TODO: BIND
# Pripoj funkciu greet na kliknutie tlačidla btn_greet.
# Nápoveda: document["btn_greet"].bind("click", greet)
