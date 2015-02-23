# indexgoriva
A django app showing Croatian motor fuel price indexes.

indexgoriva je django web app koji prikazuje indekse cijene goriva u Hrvatskoj. Cilj je prikazivanje ponderirane prosječne cijene pojedine vrste goriva za svaku tvrtku i hrvatsku u cijelini, te prikazivanje povijesnih promjena ovih indeksa.
  Izvor podataka o cijenama je portal min-go.hr, podaci sa tog portala se obrađuju koristeći [mingoparser](https://github.com/dijxtra/mingoparser).
  
  Projekt je započet na [Code for Croatia](http://codeforcroatia.org/) hackatronu 21.2.2015.

### Status projekta

indexgoriva je u pre-alpha fazi

### Roadmap

1. implementacija jednostavnog bootstrap dizajna
1. praćenje razvoja [mingoparsera](https://github.com/dijxtra/mingoparser) i prikaz podataka kako budu dostupni
1. zapisivanje svih vrijednosti jednom dnevno i grafičko prikazivanje promjene svakog indeksa kroz vrijeme
1. normaliziranje vremenske promjene indeksa i grafička usporedba trendova indeksa i cijene barela nafte na svjetskom tržištu
1. pronalaženje front-end developera da predizajnira sajt :-)

### Licenca

Kod je licenciran sa GPLv3.
