# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on tarjota käyttäjälle laskin, jolla pystyy laskemaan yksinkertaisia peruslaskutoimituksia. Laskutoimitukset tallentuvat tiedostoon. Rekisteröitynyt ja sisään kirjautunut käyttäjä voi nähdä oman laskimen käyttönsä historian.

## Käyttäjät

Kaikilla sovelluksen käyttäjillä on sama rooli. Admin-käyttäjiä ei tässä vaiheessa ole, mutta jos tarvetta myöhemmin ilmenee, voidaan sovellukseen lisätä mahdollisuus myös admin-käyttäjärooliin.

## Sovelluksen suunniteltu toiminnallisuus

### Sovelluksen aloitusnäkymä

- ✅ Käyttäjä voi kirjautua sisään; sisäänkirjautuminen siirtää käyttäjän Laskin-näkymään
- ✅ Käyttäjä voi siirtyä näkymään "Luo tunnus"

### Luo tunnus -näkymä

- ✅ Käyttäjä voi luoda uuden tunnuksen
- ✅ Käyttäjänimi ja salasana tallentuvat tiedostoon
    - ✅ Jos käyttäjänimi on jo jonkun toisen käytössä tai se on liian lyhyt (alle 3 merkkiä), käyttäjää ei luoda

### Laskin-näkymä

- ✅ Sovelluksessa on numeropainikkeet 0-9
- ✅Sovelluksessa on yhteen-, vähennys-, kerto- ja jakolaskupainikkeet sekä Clear-, Backspace- ja Tulos-painikkeet
- ✅ Käyttäjä voi syöttää laskutoimituksen
    - ✅ Laskutoimitus voi olla monimutkainen ja sisältää enemmän kuin kaksi operandia
- ✅ Tulos-painike ilmoittaa käyttäjälle laskutoimituksen lopputuloksen ja tallentaa tuloksen tiedostoon
- ✅ Käyttäjä näkee historian tekemistään laskutoimituksista
- ✅ Laskin piirtää kuvaajan käyttäjän syöttämästä funktiosta
    - ✅ Käyttäjä näkee halutessaan ohjeen funktion piirtämistä varten

## Sovelluksen jatkokehitys

-  Laskimessa on monimutkaisempia ominaisuuksia
    - Sulkulausekkeet, potenssit, pii, Neperin luku, laskun lopputuloksen ottaminen muistiin ja hyödyntäminen seuraavassa laskussa jne.
- Käyttäjä pystyy hakemaan laskutoimituksia omasta laskutoimitusten historiasta
- Käyttäjä pystyy tyhjentämään oman historiansa
- Laskin pystyy ratkaisemaan toisen asteen yhtälöitä
- Käyttäjä voi poistaa oman käyttäjätunnuksensa
- Sovelluksessa on admin-käyttäjä, joka pystyy hallinnoimaan ja poistamaan käyttäjätunnuksia
