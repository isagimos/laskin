Ohjelmistotekniikan harjoitustyö: Laskin
================================

**Laskimen** käyttäjä pystyy *kirjautumaan sisään*, laskemaan yksinkertaisia *laskutoimituksia* ja näkemään oman laskimen käyttönsä *historian*. Lisäksi laskimella voi piirtää graafisen esityksen käyttäjän syöttämästä funktiosta.

## Dokumentaatio

- [Työaikakirjanpito](https://github.com/isagimos/laskin/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/isagimos/laskin/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/isagimos/laskin/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/isagimos/laskin/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/isagimos/laskin/blob/master/dokumentaatio/testaus.md)
- [Käyttöohje](https://github.com/isagimos/laskin/blob/master/dokumentaatio/kayttoohje.md)

## GitHub Releaset

- [Viikko 5](https://github.com/isagimos/laskin/releases/tag/viikko5)
- [Viikko 6](https://github.com/isagimos/laskin/releases/tag/viikko6)
- [Loppupalautus](https://github.com/isagimos/laskin/releases/tag/loppupalautus)

## Sovelluksen käyttöönotto

Avaa terminaali ja kloonaa repositorio:

```bash
git clone https://github.com/isagimos/laskin.git
```

Siirry repositorion hakemistoon ja asenna riippuvuudet:

```bash
poetry install
```
Käynnistä sovellus seuraavalla komennolla:

```bash
poetry run invoke start
```

## Testien suorittaminen

Suorita testit pytestin avulla:

```bash
poetry run invoke test
```
Luo testikattavuusraportti HTML-muodossa:
```bash
poetry run invoke coverage-report
```

## Pylint

Analysoi koodin laatu:
```bash
poetry run invoke lint
```
