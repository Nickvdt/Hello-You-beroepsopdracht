import time
import os
os.system('cls')

def stukje1():
  stukje1 = input(" Het was een normale dag totdat de oorlog uit brak in mijn land. Ik hoorde kogels en bommen vallen midden in de nacht. \n Ik besluit te vluchten uit mijn land. \n Ik heb familie in Nederland dus mijn uiteindelijk doel is om Nederland te bereiken. \n Maar wat neem ik mee? Je hebt beperkt ruimte in je tas. \n A: Geld en een Tent \n B: Extra kleren en Eten \n ")
  if stukje1.lower() == "a":
    stukje2()
  elif stukje1.lower() == "b":
    stukje3()

def stukje2():
  os.system('cls')
  stukje2 = input(" Je gaat met een groep mensen op de vlucht en het is een lange tocht. \n Je komt een smokkelaar tegen en die kan je met een vrachtwagen verder brengen maar hij wilt veel geld. \n Ga je geld uitgeven of niet? \n A: Ja \n B: Nee \n ")
  if stukje2.lower() == "a":
    stukje4()
  elif stukje2.lower() == "b":
    stukje7()

def stukje3():
  os.system('cls')
  stukje3 = input(" Helaas kan je niet met een smokkelaar mee omdat je geen geld hebt. \n maar Je ziet wel iemand bij een tankstation en je kan met hem meeliften. \n Wil je dat? \n A: Ja \n B: Nee \n ")
  if stukje3.lower() == "a":
    stukje4()
  elif stukje3.lower() == "b":
    stukje8()

def stukje4():
  os.system('cls')
  stukje4 = input(" Uiteindelijk kom je bij een haven er daar ligt een speedboot met sleutels in het contact en een boot die vluchtelingen opvangt \n welke kies je? \n A: Speedboot \n B: Vluchtelingenboot \n ")
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
  stukje6 = input(" Je pakt een Vluchtelingenboot en de tocht duurt een paar dagen voordat aan komt. \n Uiteindelijk kom je bij de grens van Europa aan \n Je wilt de grens van Europa over maar je wordt tegengehouden. \n Wat ga je doen? \n A: Terugkeren \n B: een andere manier vinden om in Europa te komen \n ")
  if stukje6.lower() == "a":
    stukje11()
  elif stukje6.lower() == "b":
    stukje12()

def stukje7():
  os.system('cls')
  print(" Dan besluit je te lopen en als de nacht valt ga je slapen in je tent \n Helaas ben je gewond geraakt tijdens een bomaanslag vlak bij je tent. \n Helaas kan je niet verder. \n ")
  time.sleep(3)
  stukje1()

def stukje8():
  os.system('cls')
  print(" Je besluit te overnachten in het bos naast het tankstation \n  Maar helaas je bent onderkoeld geraakt en kan niet verder. \n ")
  time.sleep(3)
  stukje1()
  
def stukje9():
  os.system('cls')
  stukje9 = input(" De Politie houdt je aan, maar je mag gelukkig toch mee op de vluchtelingenboot. \n Uiteindelijk ben je in Europa. \n In Europa ga je een keuze maken neem je de trein naar Duitsland of Frankrijk. \n Welke Trein neem je? \n A: Duitsland \n B: Frankrijk \n ")
  if stukje9.lower() == "a":
    stukje14()
  elif stukje9.lower() == "b":
    stukje18()

def stukje10():
  os.system('cls')
  print(" Je pakt de speedboot en vaart weg. \n De politie achtervolgd je \n maar helaas knal je tegen een rots aan. \n Je kan niet verder \n ")
  time.sleep(3)
  stukje1()

def stukje11():
  os.system('cls')
  print(" Je keert terug en het is niet gelukt. \n Je kunt niet verder. \n " )
  time.sleep(3)
  stukje1()

def stukje12():
  os.system('cls')
  stukje12 = input(" Je bent al dagen aan het lopen en uiteindelijk kom je iemand tegen die je een lift kan geven naar België. \n Maar je wilt naar Nederland \n Ga je met hem mee of loop je door \n A: Je gaat met de persoon mee \n B: Je loopt door \n ")
  if stukje12.lower() == "a":
    stukje17()
  elif stukje12.lower() == "b":
    stukje13()

def stukje13():
  os.system('cls')
  print(" Je bent eindeloos aan het lopen langs een snelweg, je bent moe en slaperig, er komt geen eind aan. \n Uiteindelijk wordt je aangereden door een vrachtwagen . \n Je kunt niet verder. \n")
  time.sleep(3)
  stukje1()

def stukje14():
  os.system('cls')
  stukje14 = input(" Je bent in Duitsland en uiteindelijk beland je met andere vluchtelingen in een centrale opvanglocatie. \n Maar je wilt naar Nederland. \n Reis je veder naar Nederland of blijf je in Duitsland. \n A: Verder reizen naar Nederland \n B: Blijf in Duitsland \n ")
  if stukje14.lower() == "a":
    stukje15()
  elif stukje14.lower() == "b":
    stukje16()

def stukje15():
  os.system('cls')
  stukje15 = input(" Je reist veder naar Nederland ondertussen werk je ook zwart en uiteindelijk spaar je 500 euro. \n Maar wat ga je doen met dat geld? \n A: Tweedehands auto kopen om naar Nederland te rijden en daar asiel aan te vragen. \n B: Met de trein naar Nederland en daar asiel aanvragen \n ")
  if stukje15.lower() == "a":
    stukje22()
  elif stukje15.lower() == "b":
    stukje19()

def stukje16():
  os.system('cls')
  print(" Je blijft in Duitsland en krijg hier een verblijfsvergunning \n Je vind hier uiteindelijk een baan en je gaat werken. \n Soms ga je naar je Familie in Nederland om een bezoekje te doen. \n Einde 3 \n ")
  time.sleep(4)
  stukje1()

def stukje17():
  os.system('cls')
  stukje17 = input(" Je gaat met de persoon mee, en uiteindelijk kom je in België aan. \n Kies je om hier asiel aan te vragen of reis je veder naar Nederland  \n A: Hier asiel aanvragen \n B: Verder naar Nederland reizen met goederennachttrein \n ")
  if stukje17.lower() == "a":
    stukje20()
  elif stukje17.lower() == "b":
    stukje21()

def stukje18():
  os.system('cls')
  stukje18 = input(" Je bent in Frankrijk, blijf je in Frankrijk om hier asiel aantevragen of wil je naar Nederland. \n A: Blijf in Frankrijk \n B: Ga naar Nederland met de bus \n ")
  if stukje18.lower() == "a":
    stukje23()
  elif stukje18.lower() == "b":
    stukje24()

def stukje19():
  os.system('cls')
  print(" Je bent met de trein naar Nederland gegaan en je krijgt hier asiel  \n Je bent bij je familie, leert de nieuwe taal en je hebt een baan gevonden. \n Einde 1 \n ")
  time.sleep(4)
  stukje1()

def stukje20():
  os.system('cls')
  print(" Je blijft in België, krijgt hier asiel en uiteindelijk vind je hier een baan. \n 2 jaar later ga je naar Nederland toe om je familie optezoeken en verder woon je nog steeds in België. \n Einde 2 \n ")
  time.sleep(4)
  stukje1()

def stukje21():
  os.system('cls')
  print(" Je reist met de goederennachttrein naar Nederland maar je bent moe,koud en slaperig. \n Je valt helaas van de trein af \n Je kunt niet verder. \n ")
  time.sleep(3)
  stukje1()

def stukje22():
  os.system('cls')
  print(" Helaas ben je opgelicht! \n Je hebt een hele slechte auto gekocht de remmen weigerden \n Helaas kun je nu niet veder. \n ")
  time.sleep(3)
  stukje1()

def stukje23():
  os.system('cls')
  print(" Je krijgt asiel in Frankrijk, leert de taal en bouw je een nieuw leven op \n Soms ga op bezoek bij je familie in Nederland. \n Einde 4 \n ")
  time.sleep(4)
  stukje1()

def stukje24():
  os.system('cls')
  print(" Je gaat met de bus naar Nederland maar de douane houd je tegen. \n Je moet terug naar Frankrijk. \n ")
  time.sleep(5)
  stukje23()

stukje1()
     