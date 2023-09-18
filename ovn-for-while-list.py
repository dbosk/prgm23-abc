"""
Övningsmaterial om for-while-list och inmatning och felhantering

Specifikation:

Vi vill låta användaren mata in en lista med tal.
Användaren avslutar genom att mata in tomt.

Gränsnittet ska se ut något i stil med följande:

Mata in ett tal: *3*
Mata in ett tal: *5*
Mata in ett tal: *8*
Mata in ett tal: *a*
a är inte ett tal, försök igen.
Mata in ett tal: **
Talen i listan är 3, 5, 8
"""

"""
Skapa en tom lista
Vi behöver while
Vi behöver exceptions
Vi behöver input
Vi behöver funktioner
"""

def input_int(prompt):
    """
    Skriver ut prompt och låter användaren mata in ett tal.
    Fortsätter så länge användaren inte matat in ett tal.
    Om det inte går att konvertera till heltal, får användaren
    försöka igen.
    """
    while True:
        try:
            tal = input(prompt)
            if tal == "":
                return tal
            return int(tal)
        except ValueError as err:
            print(f"Det där är inte ett heltal, försök igen: {err}")

talen = []

while (tal := input_int("Mata in ett heltal: ")) != "":
    talen.append(tal)

print(f"Heltalen i listan är ", end="")
for tal in talen[:-1]:
    print(tal, end=", ")
print(talen[-1])