# Gruppe 35 - Momentum  
  
Dette prosjektet er laget i samarbeid med kunden Momentum. Vi fikk i oppdrag å lage en plattform der startups, investorer og enkeltpersoner skal kunne registrere seg, finne hverandre og ta kontakt med hverandre.
  
# Motivasjon

Prosjektet ble laget i forbindelse med NTNU-emnet TDT4140: Programvareutvikling. Prosjektet gikk ut på at vi skulle få en studentassistent til å virke som en kunde for bedriften Momentum. I dialog med denne kunden har vi utviklet et produkt i tråd med kundens ønske. 
 
# Team
* Julie Sydow Mo
* Ask Berstad Kollstveit
* Catherine Xu
* Lars Digerud
* Magnus Ramm
  
# Teknologier og rammeverk  
**Back-end:**  
[Python 3.7+](https://www.python.org/): Det valgte språket.  
[Django](https://www.djangoproject.com/): Web-rammeverk skrevet i Python, brukes til å tjene alle sider.  
[MySql](https://www.mysql.com/): Vår DBMS. Databasen er hostet på NTNU sine servere, krever VPN utenfor universitetets lokaler.  
  
**Front-end:**  
[crispy-forms](https://django-crispy-forms.readthedocs.io/): Django-applikasjon som lar deg enkelt style skjemaene dine, ved hjelp av Bootstrap.

Detaljert informasjon om rammeverk på **[Dokumentasjon av kode](https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-35/wikis/Dokumentasjon-av-kode) på wiki**.
  
# Screenshots
<img src="screenshots/intro.PNG" width="400">
<img src="screenshots/forside.PNG" width="400">
<img src="screenshots/startups.PNG" width="400">
<img src="screenshots/adgogo.PNG" width="400">  
  

**Bilde 1**: Forside del 1  
**Bilde 2**: Forside del 2  
**Bilde 3**: Oversiktside over startups  
**Bilde 4**: Eksempel profilside for startup  

# Installasjon

**Installer prosjektet:**  
1. Klon prosjektet, last ned [git](https://git-scm.com/downloads) dersom du ikke har det allerede:  
cmd: `git clone https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-35.git`  
  
2. Last ned [Python 3.7](https://www.python.org/downloads) med en oppdatert versjon av [pip](https://pip.pypa.io/en/stable/installing/#upgrading-pip). Sørg for at python legges til i path under installasjonen.  
**NB:** Python 3.5 og senere kan brukes, men hvis ikke python 3.7 brukes, må en egen [mysqlclient.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient) lastes ned for din python-versjon.  

3. Bytt mappe til gruppe-35, og installer mysqlclient:  
cmd: `pip install ./mysqlclient-1.4.2-cp37-cp37m-win32.whl`  
  
4. Installer avhengigheter:   
cmd: `pip install -r requirements.txt`  
  
5. Installer VPN for å få tilgang til NTNU-databasen, dette steget kan hoppes over dersom man befinner seg på NTNU sine lokaler og nett.  
Detaljert installasjonsguide til VPN finner du [her](https://innsida.ntnu.no/wiki/-/wiki/Norsk/Installere+VPN)
  
6. Kjør serveren:  
cmd: `python djangoproject/manage.py runserver`  
  
7. Naviger til:  
http://localhost:8000/   
  
Dersom du ser at noe ikke fungerer som det skal etter denne installasjonen, kan du henvende deg til Magnus Ramm på magnram@stud.ntnu.no.  
  
**NB**: For å benytte deg av sidens fulle funksjonalitet, kan ikke AdBlock e.l. være aktivert i nettleseren din  

# Vedlikehold

**Nullstille database:**
1. cmd: `cd ./gruppe-35/djangoproject`
2. cmd: `python manage.py flush`
svar ‘yes’ hvis du er sikker på at du vil nullstille  
3. cmd: `python manage.py populate_db`
  
**Lage en ny superbruker:**
1. cmd: `cd <mappen du klonet prosjektet i>/djangoframe`
2. cmd: `python manage.py createsuperuser`
3. skriv inn brukernavn og passord når cmd spør om det
  
# Testing
Dette prosjektet har kun benyttet seg av unit-tester. Mer om test-coverage på **[Oversikt over kodekvalitet](https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-35/wikis/oversikt-over-kodekvalitet) på wiki**. Alle unit-testene kjøres ved:  
cmd: `python manage.py test app`
