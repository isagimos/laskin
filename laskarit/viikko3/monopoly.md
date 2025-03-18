
```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Erottaja
    Erottaja "1" -- "1" Aloitusruutu
    Aloitusruutu "1" -- "1" Korkeavuorenkatu
    Korkeavuorenkatu "1" -- "1" Ruutu
    Ruutu "1" -- "1" Esplanadi
    Esplanadi "1" -- "1" Vankila
    Vankila "1" -- "1" Hämeentie
    Hämeentie "1" -- "1" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
```
