"""Olles repeterad"""

def addera(term1, term2):
    """Adderar termerna a och b och returnerar summan"""
    return term1 + term2 

def subtrahera(term1, term2):
    """Subtraherar termerna a och b och returnerar differensen"""
    return term1 - term2

print("5 + 7 = {addera(5, 7)} (utan f)")
print(f"5 + 7 = (addera(5, 7)) (parenteser)")
print(f"5 + 7 = {addera(5, 7)} (korrekt)")
print(f"5 + 7 = {5+7} (5+7 direkt)")
print("5 + 7 = " + str(addera(5, 7)) + " (str)")
print(f"5 - 7 = {subtrahera(5, 7)}")
