```mermaid
sequenceDiagram
  participant main
  participant laitehallinto
  participant rautatietori
  participant ratikka6
  participant bussi244
  main->>laitehallinto: lisaa_lataaja(rautatietori)
  main->>laitehallinto: lisaa_lukija(ratikka6)
  main->laitehallinto: lisaa_lukija(bussi244)
  
```
