"""Finn fem fel, mycket förbättrat program"""

def fråga_ja_nej(frågan):
    """ställer frågan och returnerar True om användaren svarar 'inte nej',
    annars returnerar vi False."""
    svar = input(frågan)

    if svar != "nej":
        return True
    else:
        return False

def skriver_ut_sysslor():
    """Skriver ut sysslorna som finns"""
    SYSSLOR = ["Tömma diskmaskinen", "Dammsuga mormors hus", "Gå ut med hunden"]

    for syssla in SYSSLOR:
        print(syssla)

def main():
    """Huvudprogrammet"""
    if fråga_ja_nej("Vill du vattna blommorna? "):
        print("Vattnar blommorna!")
    else:
        print("Vattnar inte blommorna")

    if fråga_ja_nej("Vill du ta ut soporna?"):
        print("Tar ut soporna")

    print("Förutom att vattna blommor och ta ut sopor ska vi:")

    skriver_ut_sysslor()

main()