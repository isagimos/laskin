## Toiminnallisuudet sekvenssikaavioina

### Käyttäjätunnuksen luominen:

```mermaid
sequenceDiagram
   actor User
   participant UI
   participant SignUp
   participant UsersRepository
   User->>UI: click "Luo tunnus" button
   UI->>SignUp: _create_account("username", "password", "password")
   SignUp->>UsersRepository: check_username("username")
   UsersRepository-->>SignUp: True
   SignUp->>UsersRepository: add_username_and_password("username", "password")
   UsersRepository-->>SignUp: True
   SignUp-->>UI: user
   UI->>UI: _login.start()
```
Sekvenssikaavion selitys:

Käyttäjä on sisäänkirjautumisnäkymässä, kirjoittaa käyttäjätunnuksen ja salasanan (kahdesti) ja klikkaa "Luo tunnus" -painiketta. Kutsutaan käyttöliittymän luokassa CreateAccount olevaa metodia _create_account. Tämä metodi taas kutsuu sovelluslogiikan SignUp-luokassa olevaa metodia _create_account, jolle annetaan parametrina käyttäjän syöttämä tunnus ja salasanat. Käyttätunnusten ja salasanojen tallentamisesta vastaava luokka UsersRepository sisältää metodin check_username("username"), jolla tarkistetaan, onko käyttäjätunnus uniikki. Mikäli näin on, metodi palauttaa True. Tämän jälkeen käyttäjätunnus ja salasana lisätään tietokantaan käyttämällä UsersRepository-luokan metodia add_username_and_password("username", "password"). Sovellus siirtyy sisäänkirjautumisnäkymään.
