
def decode(eco):
    dco = ""
    c=0
    while c < len(eco):
        if eco[c] == "0":
            dco += "7"
        elif eco[c] == "1":
            dco += "8"
        elif eco[c] == "2":
            dco += "9"
        elif eco[c] == "3":
            dco += "0"
        elif eco[c] == "4":
            dco += "1"
        elif eco[c] == "5":
            dco += "2"
        elif eco[c] == "6":
            dco += "3"
        elif eco[c] == "7":
            dco += "4"
        elif eco[c] == "8":
            dco += "5"
        elif eco[c] == "9":
            dco += "6"
        c += 1
    return dco

