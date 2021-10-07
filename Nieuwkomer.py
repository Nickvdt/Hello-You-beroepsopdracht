import time
def start():
    print("Het is een lange, moeizame dag geweest,")
    time.sleep(3)
    print("je hebt een glas melk opgewarmd en gaat in bed nog een beetje liggen lezen.")
    time.sleep(5)
    print("De zon is al onder en de maan is verscholen achter donkere wolken,")
    time.sleep(5)
    print("waardoor het enige licht in je slaapkamer afkomstig is van de kandelaar naast je hoofdeinde.")
    time.sleep(5)
    print("Na een tijdje leg je het boek naast je neer,")
    time.sleep(3)
    print("blaas je de kaars uit en sluit je je ogen,")
    time.sleep(3)
    print("je vaag bewust zijnde van de regen die buiten op je raam klettert.")
    time.sleep(4)
    print("Langzaam zak je weg en val je in een diepe slaap...")
    time.sleep(10)
    print("Plots schrik je op van een heftige donderstoot.")
    time.sleep(2)
    print("Je weet niet hoe laat het is,")
    time.sleep(3)
    print("maar je ziet nog steeds geen steek,")
    time.sleep(3)
    print("de regen is nog niet opgehouden -integendeel,")
    time.sleep(3)
    print("het is alleen maar harder gaan regenen -en het is zelfs begonnen te onweren.")
    time.sleep(5)
    print("Wanneer een tweede bliksemschicht je raam oplicht zie je tot je afschuw het groene hoofd van een goblin naar binnen turen.")
    time.sleep(6)
    print("Geschokt val je uit je bed en grijp je vergeefs naar het zwaard dat op de gang en dus niet naast je bed ligt.")
    time.sleep(5)
    print(" Intussen veegt de goblin de regendruppels van het natte raam en besef je dat hij je heeft gezien. Je besluit om...")

    print("A. Te blijven liggen. ") #14
    print("B. ... naar buiten gaan") #13
    vraag1 = input('\n')
    if vraag1.lower() == "a":
      subvraag1 = True
      print("STUKJE 14\n")
    elif vraag1.lower() == "b":
      subvraag2 = True
      print("STUKJE 13")


    #Of je het programma opnieuw wilt opstarten
    print("Dat waren alle vragen")
    print ('\n')
    print ("wil jij dit programma nog een keer doen?")

    antwoord = input("Type Y/N: ") 

    if antwoord.lower() == "y": 
        start()
    
    elif antwoord.lower() == "n": 
        print("dankjewel")
start()