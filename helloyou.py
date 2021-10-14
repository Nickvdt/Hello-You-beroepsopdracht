import time
def start():
    print("Het was een normale dag totdat de oorlog uit brak in mijn land.")
    print("Ik hoorde kogels en bommen in de nacht."'\n')
    print("Ik besluit te vluchten uit mijn land maar wat neem ik mee?")
    print("A. voedsel, water, kleren en een oude telefoon met 30%")
    print("B. tent , geld en eten")
    vraag1 = input('\n')
    if vraag1.lower() == "a":
      subvraag1 = True
      print("Je gaat met een groep mensen op de vlucht het is een lange tocht.")
      print("Je komt een smokkelaar tegen en die kunt met een vrachtauto je veder brengen maar hij wilt geld."'\n')
      print("Ga je geld uitgeven of niet?")
    elif vraag1.lower() == "b":
      subvraag2 = True
      print("Je kan niet met een smokkelaar mee omdat je geen geld hebt")
      print("of wilt uit geven maar Je ziet wel een tankstation daar mee kun met iemand mee")


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