# Gruppe 35 - Momentum  
  
Dette prosjektet er laget i samarbeid med kunden Momentum. Vi fikk i oppdrag å lage en plattform der startups, investorer og enkeltpersoner skal kunne registrere seg, finne hverandre og ta kontakt med hverandre.
  
# Motivasjon

Prosjektet ble laget i forbindelse med NTNU-emnet TDT4140: Programvareutvikling. Prosjektet gikk ut på at vi skulle få en studentassistent som vil virke som en kunde for bedriften Momentum. I dialog med denne kunden har vi utviklet et produkt i tråd med deres ønske. 
  
# Teknologier og rammeverk  
**Back-end:**  
[Python 3.7+](https://www.python.org/): Det valgte språket.  
[Django](https://www.djangoproject.com/): Web-rammeverk skrevet i Python, brukes til å tjene alle sider.  
[MySql](https://www.mysql.com/): Vår DBMS. Databasen er hostet på NTNU sine servere, krever VPN utenfor universitetets lokaler.  
  
**Front-end:**  
[crispy-forms](https://django-crispy-forms.readthedocs.io/): Django-applikasjon som lar deg enkelt style skjemaene dine, ved hjelp av Bootstrap.

Detaljert informasjon om rammeverk på **[wiki](https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-35/wikis/home)-siden**.
  
# Screenshots
<img src="https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-35/raw/master/screenshots/intro.PNG" width="400">
<img src="https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-35/raw/master/screenshots/forside.PNG" width="400">
<img src="https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-35/raw/master/screenshots/startups.PNG" width="400">
<img src="https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-35/raw/master/screenshots/adgogo.PNG" width="400">  
  

**Bilde 1**: Forside del 1  
**Bilde 2**: Forside del 2  
**Bilde 3**: Oversiktside over startups  
**Bilde 4**: Eksempel profilside for startup  

# Installasjon

**Installer prosjektet (Windows):**  
1. cmd: `git clone https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-35.git`
2. Last ned nyeste versjon av python på https://www.python.org/downloads/. Sørg for at python legges til i path under installasjonen.
3. Last ned en oppdatert versjon av pip https://pip.pypa.io/en/stable/installing/#upgrading-pip
4. cmd: `pip install Django`
5. cmd: `pip install Pillow`
6. cmd: `pip install django-crispy-forms`
7. Gå til: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient.Then. Sjekk hvilken versjon du kjører av Python og merk deg om det er 32-bits eller 64-bits. Søk etter “mysqlclient” på siden og last ned riktig versjon av mysqlclient.  
**NB:** Viktig å velge riktig version. Hvis du for eksempel kjører python 3.7.2 på windows 64-bits, så vil det stå 3.7 et sted i navnet på filen.
8. Last ned Microsoft Visual Studio https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15
9. Velg Visual C++ build tools fra workloads
10. Velg Windows 10 SDK og fjern avkrysning på de andre alternativene
11. Last ned wheel hvis nødvendig med pip install.
12. Finn lokasjonen til mysqlfilen og installer den med pip/wheel. Hvis du får problemer her kan du først forsøke å oppdatere pip og sjekke om du faktisk har installert wheel. Får du en feilmelding som sier at filen ikke støttes på denne plattformen, har du valgt feil mysqlclient-fil. Gå tilbake til steg 6 for å løse dette.
13. cmd: lokaliser mappen du klonet prosjektet til og gå inn i djangoframe
14. cmd: `python manage.py runserver`
Serveren kjører på localhost:8000

**Andre brukere: **

**NB**: Databasen ligger på NTNU sine servere, og man må derfor være koblet på NTNU-nettet eller VPN for å kunne kjøre prosjektet  
**NB2**: For å benytte deg av sidens fulle funksjonalitet, kan ikke AdBlock e.l. være aktivert i nettleseren din  

# Vedlikehold

**Nullstille database:**
1. cmd: `cd <mappen du klonet prosjektet i>/djangoframe`
2. cmd: `python manage.py flush`
svar ‘yes’ hvis du er sikker på at du vil nullstille  
*Når man nullstiller databasen må man på nytt legge til brukergruppene “Startup” og “Investor” osv  i databasen for å kunne gi disse rettighetene. Se neste steg.*

**Hvordan legge til brukergrupper på nytt:**
1. cmd: `python manage.py runserver`
2. Gå til `localhost:8000/admin`
3. Trykk på “Groups”
4. Trykk på “Add group”  
5. Lag nye grupper: “Startup”, “Investor”, “Person” (stor forbokstav)

**Lage en ny superbruker:**
1. cmd: `cd <mappen du klonet prosjektet i>/djangoframe`
2. cmd: `python manage.py createsuperuser`
3. skriv inn brukernavn og passord når cmd spør om det
  

# Testing

Alle unit-testene kjøres med følgende kommando  
cmd: `python manage.py test`
