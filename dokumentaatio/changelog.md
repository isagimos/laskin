# Changelog

## Viikko 1

- Sovelluksessa on nyt kaksi näkymää:
  - Aloitusnäkymä, jossa voi kirjautua sisään
  - Laskin-näkymä, jossa voi laskea laskuja ja kirjautua ulos; uloskirjautuminen vie takaisin aloitusnäkymään
- Luokka Login huolehtii aloitusnäkymästä
- Luokka Calculator näyttää Laskin-näkymän
- Luokka CalculatorLogic vastaa sovelluslogiikasta
  - Tarkistaa näppäinten painallukset
  - Laskee laskun ja palauttaa tuloksen käyttöliittymään (Calculator-luokka)
- Muun muassa seuraavat testit tehty:
  - Laskimen käynnistyessä operaattorit ja operandi ovat None
  - Väärää muotoa olevia laskutoimituksia ei hyväksytä (esim. 1++2 tai 1-=)
  - Nollalla ei voi jakaa
- Testattu, että sovellus toimii Cubbli Linuxilla
