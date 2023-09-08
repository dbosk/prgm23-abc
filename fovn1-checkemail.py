"""
Avgöra om en e-postadress är giltig

Skriv ett program som tar en e-postadress som input och sedan returnerar om den givna e-postadressen är giltig eller inte. Går det att återanvända kod från föregående uppgift?
"""

def giltig_adress(adress):
    """
    Avgör om adress är giltig.
    """
    # Kolla efter @ och domän etc.
    # @ får inte vara första tecknet
    if adress.count("@") == 1:
        namn, domän = adress.split("@")
        #return len(namn) > 0 and "." in domän
        if len(namn) > 0 and "." in domän:
            return True
        else:
            return False
    else:
        return False

def giltig_adress_alt2(adress):
    """
    Avgör om adress är giltig.
    """
    # Kolla efter @ och domän etc.
    # @ får inte vara första tecknet
    namn, domän = adress.split("@")
    if adress.count("@") == 1 and len(namn) > 0 and "." in domän:
        return True
    return False

print(f"dbosk@kth.se {giltig_adress('dbosk@kth.se')}")
print(f"dbosk@@kth {giltig_adress('dbosk@@kth')}")
print(f"dbosk@kth {giltig_adress('dbosk@kth')}")