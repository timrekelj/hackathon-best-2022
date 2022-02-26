## Navodila za zagon aplikacije
1. Potrebna sta Python 3 in pip
2. Uporabi virtual environment za potrebne knjižnice
3. Ukaz ```flask run``` požene server, da lahko odpremo aplikacijo na http://localhost:3000

## Navodila za hackathon
### Opis problema in oblikovanje projektne naloge:
- Za ogrevanje poslovnih in industrijskih prostorov se uporablja energent kurilno olje (KO), ki se hrani v 20m3 rezervoarju, ki je nepravilne valjaste oblike (vodoravno postavljen »valj«, obe stranici sta elipsi). V rezervoarju se za spremljanje stanja izvaja meritev nivoja kurilnega olja (KO). Poraba KO se izračunava na podlagi formule volumna, ki izhaja iz oblike rezervoarja in razlike izmerjenega nivoja.


- Ob polnočni vsak dan se v bazo kreira txt datoteka z meritvami nivoja in izračunom volumna KO v rezervoarju. V analizi podatkov se uporablja dnevna poraba KO, ki se izračuna tako, da se povprečna vrednost volumna za tekoči dan odšteje od povprečne vrednosti volumna za prejšnji dan, tako dobimo porabo v tekočem dnevu. Povprečne vrednosti se uporabljajo zato, ker meritev sorazmerno precej niha.


- Primer izračuna za normalno dnevno porabo:
    - *30.11.2021 povprečna dnevna vrednost volumna KO 2,28 m3*
    - *1.12.2021 povprečna dnevna vrednost volumna KO 2,12 m3*
    - ***Dnevna poraba: 2,28 m3 – 2,12 m3 = 0,160 m3 oziroma 160 L***


- Pri določeni minimalni količini energenta v rezervoarju je potrebno le-tega napolniti in takrat se v tej dnevni periodi meritev in izračunov pojavi anomalija, saj je izračunan nivo oziroma volumen v rezervoarju nižji kot je pričakovati po dobavi, zato je razlika včeraj – danes prikazana kot negativna vrednost , torej pri polnjenju baze z dnevnimi podatki pride do napačnega podatka, ki ga je treba korigirati tako, da se izračuna razlika med volumnom od polnoči prejšnjega dneva do časa dobave in od časa dobave do polnoči dneva izvedene dobave. Dobave KO so najmanj 3000 do max 10000L. Na leto imamo približno 3 dobave.


- Primer izračuna porabe na dan dobave:
    - *1.12.2021 povprečna vrednost volumna 2,12 m3*
    - *2.12.2021 povprečna vrednost volumna do 10:15 2,08 m3 DELNA RAZLIKA 40 L*
    - *2.12.2021 povprečna vrednost volumna po 10:30 do polnoči 5,08 m3 (po dobavi 3000 l kurilnega olja)*
    - *3.12.2021 povprečna vrednost volumna 4,98 m3 DELNA RAZLIKA 100 L*
    - ***Skupna dnevna poraba 140 L.***

---

### Naloge

1. **Del naloge: ugotavljanje anomalij podatkov in s korekcijami zagotoviti verodostojnost podatkov o dnevnih porabah energenta¸**

V obstoječi Access bazi, kamor se avtomatsko zapisujejo izračunane vrednosti dnevnih porab energenta, naj se ugotovljene napačne/nelogične/neverodostojne vrednosti porabe obarvajo rdeče. Po korekcijskih izračunih pravilnih dnevnih porab na dneve dobav energenta, naj se v bazo podatkov, ki se uporablja za analizo porabe in napovedi dobav (Access), avtomatsko vnese popravljena vrednost porabe in se označi z npr. zeleno barvo.

---

2. **Del naloge: ugotavljanje/spremljanje trendov porabe naj bo podlaga za sprožanje alarmov o napakah v sistemu in za sprožanje naročil za nabave**

V bazi podatkov spremljamo dnevno porabo KO in ugotavljamo trend porabe. Minimalna količina energenta, ki mora ostati v rezervoarju je določena na 1000 L.
- Iz trenda porabe naj sistem obvešča, za koliko dni KO je na zalogi pri trenutnem trendu porabe. Sistem naj sporoči, ko je na zalogi še za 7 dni KO (+ minimalna količina 1000L), ker je potrebno sprožiti postopek naročila za nabavo. Zaželjeno je tudi da se generira e-mail opozorilo odgovornim osebam da spelje postopek nabave. 
- V analizi podatkov določimo še sprejemljivo maksimalno dnevno porabo, na primer, da določimo, da je to 400 L/dan. Če je ta poraba presežena, naj se sproži alarm (e-mail obvestilo) **o nesprejemljivih stanjih, (ki nakazujejo na napake meritev, nastavitev regulacije ogrevanja ali puščanja v sistemu) in/ali alarm e-mail sporočilo, da je potrebna nova dobava energenta.**

---

3. **Dodaten izziv**

Verodostojni podatki o porabi energenta (in drugih procesnih kemikalij) so izhodišče za bolj zanesljivo napovedovanje letne porabe energenta ob upoštevanju sezonskih vremenskih ciklov in trendov, ki izhajajo iz klimatskih sprememb, obratovalnih režimov, obrabe opreme, itd.

Za dodatne točke pri ocenjevanju vaših izdelkov lahko predlagate in demonstrirate izboljšavo ali nadgraditev našega sistema oziroma procesa uporabe podatkov, ki so na voljo (AI, deep-learning, data engineering,…).

---

4. **Vhodni podatki in izhodni podatki**

Za izvedbo zastavljene projektne naloge imate na voljo bazo podatkov v .txt formatu za leto 2021, vsak dan je ločena datoteka, podatki meritev pa so zabeleženi podatki vsakih 5 minut.

Za obdelavo teh podatkov lahko uporabite programsko opremo po vaši želji. Naša želja pa je, da bo rezultati vašega programiranja bilo možno importirati v Access podatkovno bazo.