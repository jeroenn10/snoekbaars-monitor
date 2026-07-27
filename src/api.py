"""
API Module - Technisch Ontwerp
===============================

VERANTWOORDELIJKHEID:
    Deze module abstraheert alle interactie met externe API's voor hydrologische data.
    Ze verzorgt:
    - Authenticatie en connectiviteit naar Rijkswaterstaat Waterinfo API
    - Verwerking van HTTP requests en responses
    - Error handling en rate limiting
    - Caching van metadata (catalogus) waar relevant
    
    De module is verantwoordelijk voor het ophalen van ruwe hydrologische gegevens
    uit externe bronnen, maar NIET voor data-analyse, opslag, of notificaties.

EXTERNE DATABRON:
    Rijkswaterstaat Waterinfo API (DDAPI20)
    - Endpoint: https://ddapi20-waterwebservices.rijkswaterstaat.nl
    - Services: METADATASERVICES (catalogus), WEBSERVICES (meetgegevens)
    - Gegevens: Waterhoogte, afvoer, temperatuur van gemonitorde locaties

PUBLIEKE FUNCTIES (TO IMPLEMENT):
    - discover_locations()
      Haalt lijst van beschikbare meetlocaties op uit Rijkswaterstaat catalogus
      
    - fetch_water_temperature()
      Haalt watertemperatuur op voor gegeven locatie(s) en tijdperiode
      
    - fetch_water_level()
      Haalt waterhoogte op voor gegeven locatie(s) en tijdperiode
      
    - fetch_discharge()
      Haalt afvoergegevens op voor gegeven locatie(s) en tijdperiode
"""
