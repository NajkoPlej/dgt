---- 1. DRUHY APLIKÁCIÍ ----
    a) Native aplikácie
Vytvorené priamo pre Android / iOS
Inštalácia cez Store (Google Play, App Store)
Plný prístup k hardvéru:
Bluetooth
senzory
kamera
GPS
beh na pozadí
Vysoký výkon
Používajú špecifické natívne API

Výhoda: maximálny výkon a plný HW prístup
Nevýhoda: vývoj zvlášť pre každú platformu

   b) Hybrid aplikácie
Webová aplikácia zabalená do WebView („web v krabičke“)
Obsahuje mostík medzi webom a natívnymi funkciami
Distribúcia cez Store
Potrebuje server a internet
Čiastočný prístup k HW
Charakteristika:
Webové UI
Pár natívnych schopností

Výhoda: jeden kód pre viac platforiem
Nevýhoda: závislosť na internete

   c) PWA (Progressive Web App)
PWA = web + manifest + service worker + HTTPS
Inštalácia z webu („Add to Home Screen“)
Spája výhody webu a natívnych aplikácií
Rýchly vývoj
Jednoduchá distribúcia
Offline režim pomocou cache
Nemá plný prístup k HW ako native
⚠ Service Worker nebeží ako klasická aplikácia na pozadí – funguje v rámci prehliadača.

---- ANDROID – ZÁKLADNÉ POJMY ----
Activity – jedna obrazovka aplikácie
Intent – presun medzi obrazovkami
Android Manifest – pravidlá aplikácie:
názov
povolenia
aktivity

-- PWA – ČO JE NUTNÉ --
    1. Web Manifest (manifest.webmanifest / .json)
„Vizitka aplikácie“
Najdôležitejšie:
name
short_name
start_url
icons (192x192, 512x512)
display: standalone
scope
id
background_color
theme_color

   2. Service Worker
Zabezpečuje offline režim a cache.
Lifecycle udalosti:
install → precache súborov
activate → čistenie starej cache
fetch → zachytáva požiadavky (sieť vs cache)
Cache stratégie:
Cache-first → statické súbory (HTML, CSS, JS, obrázky)
Network-first + fallback → dynamické dáta (JSON)
Stale-while-revalidate → rýchla odpoveď + aktualizácia na pozadí

   3. HTTPS
Povinné pre PWA (okrem localhost)
Bezpečnostné pravidlá podľa domény (origin)

  - BEZPEČNOSŤ -
Android
Sandbox → každá aplikácia má vlastný priestor
Permissions → aplikácia sa pýta na prístup (kamera, mikrofón…)
Web
Origin politika
HTTPS povinné pre offline a SW

  - ULOŽISKÁ -
localStorage
Malé textové údaje (key → value)
Jednoduché
Ukladá len text
(JSON umožňuje ukladať iné dátové typy ako text)
IndexedDB
Väčšie množstvo dát
Vyhľadávanie
Transakcie
Vhodné pre veľké zoznamy
 
  - OFFLINE STRATÉGIE - 
Cache-first → statické časti aplikácie
Network-first + fallback → dynamické dáta zo servera

   Na aké udalosti môže reagovať aplikácia
microphone
compass
bluetooth
GPS
camera
prístup k súborom / galérii
input prvky:
radio
textarea
checkbox
color
email
password
message
date

  -- ZÁKLADNÉ PROGRAMOVACIE POJMY --

.pop() → vymaže posledný prvok
.clear() → vymaže celé pole
.append() → pridá prvok do poľa
.strip() → odstráni medzery
.get() → získa hodnotu podľa kľúča (ak neexistuje, vráti None alebo default)
.value → vráti hodnotu inputu
return → ukončí funkciu a vráti hodnotu
pass → nič neurobí (len placeholder)

  -- SERVICE WORKER – DETAILNE --
Čo je Service Worker?
JavaScriptový súbor, ktorý:
beží na pozadí prehliadača
zachytáva sieťové požiadavky
umožňuje cache
umožňuje offline režim
podporuje push notifikácie

Hlavné výhody:
rýchlejšie načítanie
offline režim
správa ako natívna aplikácia

Obmedzenia:
funguje len na HTTPS alebo localhost
rovnaký pôvod ako stránka

-- APP SHELL MODEL --
Čo je App Shell?
Základná kostra aplikácie:
index.html
CSS
JS
ikony
Tieto súbory sa precachujú pri inštalácii SW.

Výhody:
rýchle načítanie
fungovanie offline
oddelenie statiky a dynamiky

  -- MINIMÁLNA ŠTRUKTÚRA PWA --
Povinné súbory:
index.html
style.css
sw.js
offline.html
manifest.webmanifest

Priečinok:
icons (192x192, 512x512)

  -- REGISTRÁCIA SERVICE WORKERA --
Vkladá sa do index.html
Pred koniec <body>
Funguje len na HTTPS / localhost
Stav možno sledovať v konzole

  -- SW.JS – PROFESIONÁLNY ZÁKLAD --
CACHE_VERSION → ručne meníme pri aktualizácii
PRECACHE_ASSETS → základné súbory
Fetch handler → sieť alebo cache
Runtime caching → dynamické ukladanie počas behu

  ---- ZHRNUTIE ----
Native = plný výkon + plný HW
Hybrid = web zabalený do aplikácie
PWA = webová aplikácia s offline podporou
localStorage = malé texty
IndexedDB = veľké dáta
Cache-first = statika
Network-first = dáta















