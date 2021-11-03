import time
import os
os.system('cls')

def stukje1():
  stukje1 = input(" Het was een normale dag totdat de oorlog uit brak in mijn land. Ik hoorde kogels en bommen midden in de nacht. \n Ik besluit te vluchten uit mijn land. \n Ik weet dat ik kennissen ken uit Nederland dus mijn uiteindelijk doel is om Nederland te bereiken. \n Maar wat neem ik mee? Je hebt beperkt ruimte in je tas. \n A: Geld en een Tent \n B: Geld en Eten \n ")
  if stukje1.lower() == "a":
    stukje2()
  elif stukje1.lower() == "b":
    stukje3()

def stukje2():
  os.system('cls')
  stukje2 = input(" Je gaat met een groep mensen op de vlucht & het is een lange tocht. \n Je komt een smokkelaar tegen en die kunt met een vrachtauto je veder brengen maar hij wilt geld. \n Ga je geld uitgeven of niet? \n A: Ja \n B: Nee \n ")
  if stukje2.lower() == "a":
    stukje4()
  elif stukje2.lower() == "b":
    stukje7()

def stukje3():
  os.system('cls')
  stukje3 = input(" Helaas kan je niet met een smokkelaar mee omdat je geen geld hebt. \n maar Je ziet wel een tankstation en je kan met iemand meeliften. \n Wil je dat? \n A: Ja \n B: Nee \n ")
  if stukje3.lower() == "a":
    stukje4()
  elif stukje3.lower() == "b":
    stukje8()

def stukje4():
  os.system('cls')
  stukje4 = input(" Uiteindelijk ben je bij een haven er staat een speedboot & en een boot die vluchtelingen opvangt \n welke kies je? \n A: Speedboot \n B: Vluchtelingenboot \n ")
  if stukje4.lower() == "a":
    stukje5()
  elif stukje4.lower() == "b":
    stukje6()

def stukje5():
  os.system('cls')
  stukje5 = input(" Je pakt de speedboot maar de politie ziet het. Wat ga je doen? \n A: Overgeven \n B: Vluchten \n ")
  if stukje5.lower() == "a":
    stukje9()
  elif stukje5.lower() == "b":
    stukje10()

def stukje6():
  os.system('cls')
  stukje6 = input(" Je pakt een Vluchtelingenboot en de tocht duurt een paar dagen voordat aan komt. \n Uiteindelijk ben je bij de grens van Europa \n Je wilt in Europa maar de poortwachters houden je tegen. \n Wat ga je doen? \n A: Wachten \n B: een andere manier vinden om in Europa te komen \n ")
  if stukje6.lower() == "a":
    stukje11()
  elif stukje6.lower() == "b":
    stukje12()

def stukje7():
  os.system('cls')
  print(" Dan besluit je te lopen en als de nacht valt zit te slapen in je tent \n Helaas ben je dood gegaan tijdens een aanslag. \n ")
  time.sleep(3)
  stukje1()

def stukje8():
  os.system('cls')
  print(" Je hebt nu wel genoeg voedsel om de nacht te overleven \n alleen je hebt geen onderdak meer omdat er recent een aanslag is geweest. \n Helaas ben je dood gegaan aan onderkoeling. \n ")
  time.sleep(3)
  stukje1()
  
def stukje9():
  os.system('cls')
  stukje9 = input(" De Politie pakt je op en je gaat met de vluchtelingen mee op de vluchtelingenboot. \n Opgegeven moment dan ben je in Europa. \n In Europa wil je een keuze maken of je de trein neemt naar Duitsland of Frankrijk. \n Welke Trein neem je? \n A: Duitsland \n B: Frankrijk \n ")
  if stukje9.lower() == "a":
    stukje14()
  elif stukje9.lower() == "b":
    stukje18()

def stukje10():
  os.system('cls')
  print(" Je pakt de speedboot en vaart weg. \n De politie achtervolgd je \n maar helaas knal je tegen een rots aan. \n ")
  time.sleep(3)
  stukje1()

def stukje11():
  os.system('cls')
  print(" Je wacht te lang en uiteindelijk overlijd aan honger. \n" )
  time.sleep(3)
  stukje1()

def stukje12():
  os.system('cls')
  stukje12 = input(" Je gaat heel ver lopen en uiteindelijk kom je iemand tegen die je kan brengen met de auto naar België. \n Maar je wilt naar Nederland \n Ga je met hem mee of loop je door \n A: Je gaat met de persoon mee \n B: Je loopt door \n ")
  if stukje12.lower() == "a":
    stukje17()
  elif stukje12.lower() == "b":
    stukje13()

def stukje13():
  os.system('cls')
  print(" Je bent eindeloos aan het lopen op een snelweg en er komt geen eind aan. \n Uiteindelijk ga dood door gebrek aan eten. \n ")
  time.sleep(3)
  stukje1()

def stukje14():
  os.system('cls')
  stukje14 = input(" Je bent in Duitsland en uiteindelijk kom je met vluchtelingen in een centrale opvanglocatie. \n Maar je wilt naar Nederland. \n Wil je als de nacht valt vluchten of niet. \n A: Vluchten \n B: Blijf in Duitsland \n ")
  if stukje14.lower() == "a":
    stukje15()
  elif stukje14.lower() == "b":
    stukje16()

def stukje15():
  os.system('cls')
  stukje15 = input(" Je vlucht uit centrale opvanglocatie en je komt op straat terecht. \n Je gaat bedelen en uiteindelijk krijg je totaal 50 euro. \n Maar wat ga je doen met dat geld? \n A: cursus taal \n B: Trein naar Nederland \n ")
  if stukje15.lower() == "a":
    stukje22()
  elif stukje15.lower() == "b":
    stukje19()

def stukje16():
  os.system('cls')
  print(" Je blijft in Duitsland \n Je vind hier uiteindelijk een baan en je gaat werken. \n Soms ga je naar je kennissen in Nederland om een bezoekje te doen. \n Einde 3 \n ")
  time.sleep(4)
  stukje1()

def stukje17():
  os.system('cls')
  stukje17 = input(" Je gaat met de persoon mee, en uiteindelijk ben je in België. \n Kies je om hier te blijven en werk te zoeken of naar Nederland toe te gaan \n A: Hier blijven \n B: Naar Nederland gaan \n ")
  if stukje17.lower() == "a":
    stukje20()
  elif stukje17.lower() == "b":
    stukje21()

def stukje18():
  os.system('cls')
  stukje18 = input(" Je bent in Frankrijk maar ga je blijven in Frankrijk of wil je naar Nederland. \n A: Blijf in Frankrijk \n B: Ga naar Nederland met de bus \n ")
  if stukje18.lower() == "a":
    stukje23()
  elif stukje18.lower() == "b":
    stukje24()

def stukje19():
  os.system('cls')
  print(" Je bent met de trein naar Nederland gegaan \n Je woon bij je kennissen, leert de nieuwe taal en je hebt een baan gevonden. \n Einde 1 \n ")
  time.sleep(4)
  stukje1()

def stukje20():
  os.system('cls')
  print(" Je blijft in België en uiteindelijk vind je een baan. \n 2 jaar later ga je naar Nederland toe om je kennissen zoeken en veders woon je nog steeds in België. \n Einde 2 \n ")
  time.sleep(4)
  stukje1()

def stukje21():
  os.system('cls')
  print(" Je gaat naar Nederland maar je hebt het heel koud \n en je kan helaas nergens warme kleding vinden. \n Uiteindelijk ga je dood door gebrek aan eten en onderkoeling. \n ")
  time.sleep(3)
  stukje1()

def stukje22():
  os.system('cls')
  print(" Helaas ben je opgelicht! \n Je hebt nu geen geld en je kan geen eten of drinken kopen. \n Uiteindelijk ga je dood door gebrek aan eten. \n ")
  time.sleep(3)
  stukje1()

def stukje23():
  os.system('cls')
  print(" In Frankrijk bouw je een nieuw leven op en werk je bij de lokale supermarkt \n Helaas heb je geen geld om naar Nederland te komen & je hebt je kennissen nooit gesproken. \n Einde 4 \n ")
  time.sleep(4)
  stukje1()

def stukje24():
  os.system('cls')
  print(" Je gaat met de bus naar Nederland maar de douane houd je tegen. \n Je moet terug naar Frankrijk. \n ")
  time.sleep(5)
  stukje23()

stukje1()
     