# Sito web squadra ciclistica (Flask)

Sito semplice per una squadra ciclistica con: storia, vittorie più importanti,
elenco atleti, staff tecnico e contatti. Pensato per essere hostato gratuitamente
su **Render**.

## Struttura del progetto

```
team-ciclistico/
├── app.py                 # App Flask + dati della squadra (modifica qui i contenuti)
├── requirements.txt        # Dipendenze Python
├── Procfile                 # Comando di avvio per Render
├── templates/
│   ├── base.html
│   └── index.html
└── static/
    ├── css/style.css
    └── img/logo.jpg
```

## 1. Personalizzare i contenuti

Apri `app.py` e modifica il dizionario `TEAM_DATA` in cima al file:
- `nome_squadra`, `motto` (frase/slogan)
- `storia` → anno di fondazione e testo
- `vittorie` → lista di vittorie (anno, titolo, descrizione)
- `atleti` → lista di corridori (nome, categoria)
- `staff` → direttori sportivi e istruttori
- `contatti` → email, telefono, indirizzo, social

Non serve toccare l'HTML per cambiare i testi.

## 2. Provarlo in locale

```bash
python -m venv venv
source venv/bin/activate      # su Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Il sito sarà disponibile su http://localhost:5000

## 3. Pubblicarlo su Render (piano gratuito)

1. Crea un repository su GitHub e carica tutti i file di questa cartella
   (compreso `Procfile` e `requirements.txt`).
2. Vai su https://render.com e crea un account (puoi accedere anche con GitHub).
3. Clicca **New +** → **Web Service**.
4. Collega il repository GitHub appena creato.
5. Nelle impostazioni del servizio:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: `Free`
6. Clicca **Create Web Service**. Render farà build e deploy automaticamente.
7. Dopo qualche minuto il sito sarà online su un indirizzo tipo
   `https://tuo-nome-progetto.onrender.com`

Nota: con il piano gratuito di Render, il servizio "si addormenta" dopo un
periodo di inattività e il primo caricamento dopo una pausa può richiedere
qualche secondo in più: è normale.

## 4. Prossimi passi (facoltativi)

- Aggiungere foto reali degli atleti e della squadra (cartella `static/img/`)
- Aggiungere una pagina calendario gare
- Collegare un dominio personalizzato da Render (impostazioni → Custom Domain)
