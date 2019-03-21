**Installer prosjektet:**  
1. cmd: git clone git@gitlab.stud.idi.ntnu.no:programvareutvikling-v19/gruppe-35.git
2. Last ned nyeste versjon av python på www.python.org  
3. Installer nyeste versjon av python med pip i en terminal  
4. cmd: pip install Django  
5. cmd: pip install Pillow
6. cmd: pip install django-crispy-forms
7. Gå til: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient.Then. Sjekk hvilken versjon du kjører av Python og merk deg om det er 32-bits eller 64-bits. Søk etter “mysqlclient” på siden og last ned riktig versjon av mysqlclient.
8. Last ned Microsoft Visual Studio https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15
9. Velg Visual C++ build tools fra workloads
10. Velg Windows 10 SDK og fjern avkrysning på de andre alternativene
11. Last ned wheel hvis nødvendig med pip install.
12. Finn lokasjonen til mysqlfilen og installer den med pip/wheel. Hvis du får problemer her kan du først forsøke å oppdatere pip og sjekke om du faktisk har installert wheel. Får du en feilmelding som sier at filen ikke støttes på denne plattformen, har du valgt feil mysqlclient-fil. Gå tilbake til steg 6 for å løse dette.
13. cmd: lokaliser mappen du klonet prosjektet til og gå inn i djangoframe
14. cmd: python manage.py runserver
Serveren kjører på localhost:8000
  
**Nullstille database:**
1. cmd: cd <mappen du klonet prosjektet i>/djangoframe
2. cmd: python manage.py flush
svar ‘yes’ hvis du er sikker på at du vil nullstille  
*Når man nullstiller databasen må man på nytt legge til brukergruppene “Startup” og “Investor” osv  i databasen for å kunne gi disse rettighetene. Se neste steg.*

**Hvordan legge til brukergrupper på nytt:**
1. cmd: python manage.py runserver
2. Gå til localhost:8000/admin
3. Trykk på “Groups”
4. Trykk på “Add group”  
5. Lag nye grupper: “Startup”, “Investor”, “Person” (stor forbokstav)

**Lage en ny superbruker:**
1. cmd: cd <mappen du klonet prosjektet i>/djangoframe
2. cmd: python manage.py createsuperuser
3. skriv inn brukernavn og passord når cmd spør om det


