Ohjelmistotekniikan harjoitustyö: Laskin
================================

Tavoitteena on koodata **laskin**, jossa käyttäjä pystyy *kirjautumaan sisään*, laskemaan yksinkertaisia *laskutoimituksia* ja näkemään oman laskimen käyttönsä *historian*.

## Dokumentaatio

- [Työaikakirjanpito](https://github.com/isagimos/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/isagimos/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/isagimos/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/isagimos/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [GitHub release](https://github.com/isagimos/ot-harjoitustyo/releases/tag/viikko5)

## Sovelluksen käyttöönotto

Avaa terminaali ja kloonaa repositorio:

```bash
git clone https://github.com/isagimos/ot-harjoitustyo.git
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
