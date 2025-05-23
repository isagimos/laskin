# Changelog

## Viikko 1

- Sovelluksessa on nyt kaksi näkymää:
  - Aloitusnäkymä, jossa voi kirjautua sisään
  - Laskin-näkymä, jossa voi laskea laskuja ja kirjautua ulos; uloskirjautuminen vie takaisin aloitusnäkymään
- Luokka **UI** vastaa sovelluksen käynnistämisestä
- Luokka **Login** huolehtii aloitusnäkymästä
- Luokka **Calculator** näyttää Laskin-näkymän
- Luokka **CalculatorLogic** vastaa sovelluslogiikasta
  - Tarkistaa näppäinten painallukset
  - Laskee laskun ja palauttaa tuloksen käyttöliittymään (Calculator-luokka)
- Muun muassa seuraavat testit tehty:
  - Laskimen käynnistyessä operaattorit ja operandi ovat None
  - Väärää muotoa olevia laskutoimituksia ei hyväksytä (esim. 1++2 tai 1-=)
  - Nollalla ei voi jakaa
- Testattu, että sovellus toimii Cubbli Linuxilla

## Viikko 2
- Sovelluksessa nyt myös Luo tunnus -näkymä; käyttäjä voi luoda tunnuksen ja kirjautua sisään
- Käyttöliittymän luokka **CreateAccount** vastaa tunnuksen luomisesta
  - Vastaavasti sovelluslogiikan luokka **SignUp** tallentaa tunnuksen .csv-tiedostoon
- Sisäänkirjautumista varten luotu myös sovelluslogiikkaan **LoginCheck**-luokka
  - Käsittelee sisäänkirjautumispyynnöt
- Lasketut laskut tallentuvat .csv-tiedostoon
  - Kunkin käyttäjän laskujen historia näkyy Laskin-näkymässä; tästä huolehtii **FetchHistory**-luokka
- **CalculatorLogic**-luokkaa muokattu olennaisesti
  - Nyt käyttäjän syötteet käsitellään ja lasketaan sympy-kirjaston avulla
- Lisää testejä: luokka **TestSignup** tarkistaa, että sovelluslogiikan luokka **SignUp** toimii kuten pitää

## Viikko 3
- Testattu, että viime viikolla käyttöönotettu sympy-kirjasto **CalculatorLogic**-luokassa toimii
- Laskimeen lisätty backspace- ja clear all -näppäimet
- Lisätty käyttäjätunnuksen ja salasanan vähimmäispituuden tarkistus tunnusta luotaessa

## Viikko 4
- Käyttäjä pystyy piirtämään funktion kuvaajan
  - Kuvaajan piirtäminen toteutettu matplotlibillä **CalculatorLogic**-luokkaan
- Testattu mm., että laskin jatkaa toimintaansa, jos edellinen laskenta päättynyt ilmoitukseen "Virhe"

## Viikko 5
- Laskimessa painike "Näytä ohje", jota klikkaamalla käyttäjä näkee ohjeet funktion kuvaajan piirtämiseen

## Viikko 6
- Tietokannan lukeminen ja kirjoittaminen toteutui aiemmin sovelluslogiikassa. Nyt tehty repository-mallin mukainen toteutus. Luotu hakemisto repositories, jonne tehty luokat **CalculationsRepostiory** ja **UsersRepository**.
- Muita muutoksia sovelluslogiikkaan tai käyttöliittymään ei tämän viikon palautukselle ole; sovellus on jo tullut valmiiksi.
