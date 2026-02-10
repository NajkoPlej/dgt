--- SERVICE WORKER ---
- JavaScriptový skript bežiaci na pozadí prehliadača
- Beží nezávisle od otvorenej stránky
- Interceptuje sieťové požiadavky
- Používa sa na:
    - cachovanie zdrojov
    - zlepšenie rýchlosti
    - offline režim
      
--- PREČO POUŽIŤ ---
- Rýchlejšie načítanie (cache statických assetov)
- Offline podpora a degradované správanie pri strate siete
- Push notifikácie
- Pozadí synchronizácia

--- HLAVNÉ LIFECYCLE UDALOSTI ---
1. install
  - precache dôležitých statických súborov
  - spúšta sa pri registrácii alebo novej verzii SW (Service Worker)
2. activate
  - čistenie starých cache verzií
  - zabezpečenie aktuálnosti a konzistencie dát
3. fetch
  - rozhoduje medzi sieťou a cache
  - používa cache stratégie
4. waiting stav
  - nový SW čaká, kým sa nezavrú staré karty
  - skipWaiting urýchľuje aktiváciu

--- BEŽNÉ CACHE STRATÉGIE ---
- Cache-first
  - statické assety (CSS, JS, obrázky)
  - rýchle
  - vhodné pre offline
- Network-first
  - dynamické a autentifikačné dáta
  - fallback na cache pri výpadku siete
- Stale-while-revalidate
  - rýchla odpoveď z cache
  - aktualizácia cache na pozadí

--- DEFINÍCIA A VÝZNAM ---
-Beží na pozadí
-Spravuje sieťové požiadavky

--- VÝHODY CACHE A OFFLINE REŽIMU ---
-Rýchlejšie načítavanie
-Funkčnosť aplikácie bez internetu

--- PODPORA PWA FUNKCIÍ ---
-Správanie ako natívna aplikácia
-Inštalácia
-Ikona na zariadení

--- OBMEDZENIA A BEZPEČNOSŤ ---
-Funguje iba na HTTPS alebo localhost
-Vyžaduje rovnaký pôvod ako webová stránka

_____________________________________________________

--- APP SHELL MODEL ---
-Základná kostra aplikácie

--- ZÁKLADNÁ KOSTRA APLIKÁCIE ---
precache:
-index.html
-CSS
-skripty

--- RÝCHLEJŠIE NAČÍTAVANIE OFFLINE ---
-okamžité načítanie aplikácie
-funguje pri slabom alebo žiadnom internete

--- DYNAMICKÉ NAČÍTANIE DÁT ---
-dáta sa načítavajú počas behu aplikácie
-oddelené od statickej kostry

--- VÝHODY PRE ŠKOLSKÉ PROJEKTY ---
-lepšie pochopenie offline režimu
-rozdelenie projektu:
-statická časť
-dynamická časť

--- MINIMÁLNA ŠTRUKTÚRA PWA PROJEKTU ---
POVINNÉ SÚBORY PWA
-index.html
-style.css
-sw.js
-offline.html
-manifest.webmanifest

--- ŠTRUKTÚRA PRIEČINKOV ---
-icons/
-192x192px
-512x512px
-zabezpečenie vizuálnej identity aplikácie

--- BRYTHON ŠPECIFIKÁCIA ---
-app.py
-bryhton.min.js
-brython_stdlib.js
-zabezpečenie lokálnej funkčnosti bez internetu

--- ODDELENIE STATICKÝCH A DYNAMICKÝCH SÚBOROV ---
-lepšie cache
-jednoduchšia údržba aplikácie

--- REGISTRÁCIA SERVICE WORKERA V INDEX.HTML ---
ZÁKLADNÝ KROK PWA
-nevyhnutné pre PWA funkcionalitu

--- UMIESTNENIE V INDEX.HTML ---
-pred koniec <body>
-nezdržuje načítanie stránky

--- BEZPEČNOSTNÉ OBMEDZENIA ---
-iba HTTPS alebo localhost

--- PROFESIONALITA A LADENIE ---
-sledovanie stavu v konzole
-profesionálna webová prax

--- SW.JS – PROFESIONÁLNY ZÁKLAD ---
CACHE VERZOVANIE A AKTUALIZÁCIE
CACHE_VERSION sa mení manuálne
-zabraňuje používaniu starých súborov

--- PRECACHE A APP SHELL ---
PRECACHE_ASSETS:
-index.html
-štýly
-skripty
-ikony

- - - FETCH A OFFLINE CALLBACK - - -
navigačné požiadavky:
-sieť
-fallback na offline.html

--- RUNTIME CACHING A SELEKTÍVNA OBSLUHA ---
-dynamické dopĺňanie cache
-selektívna obsluha podľa typu požiadavky






































