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

**Installer prosjektet:**  
1. Klon prosjektet:  
cmd: `git clone https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-35.git`  
  
2. Last ned nyeste versjon av [python](https://www.python.org/downloads/) med en oppdatert versjon av [pip](https://pip.pypa.io/en/stable/installing/#upgrading-pip). Sørg for at python legges til i path under installasjonen.
  
3. Installer avhengigheter:   
cmd: `pip install -r requirements.txt`  
  
4. Kjør serveren:  
cmd: `python manage.py runserver`  
  
5. Naviger til:  
http://localhost:8000/   
  
Dersom du ser at noe ikke fungerer som det skal etter denne installasjonen, kan du henvende deg til Magnus Ramm på magnram@stud.ntnu.no.  
  
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
