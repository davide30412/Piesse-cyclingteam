"""
Sito web per squadra ciclistica - Flask app
--------------------------------------------
Modifica i dati qui sotto (dizionario TEAM_DATA) per personalizzare
storia, vittorie, atleti, staff e contatti senza toccare l'HTML.
"""

import os
from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------
# DATI DELLA SQUADRA — modifica qui i contenuti del sito
# ---------------------------------------------------------------------
TEAM_DATA = {
    "nome_squadra": "Piesse Cycling Team",
    "motto": "Ogni salita ha una storia. Noi la scriviamo in sella.",

    "storia": {
        "anno_fondazione": 2010,
        "testo": (
            "Fondata nel 2010 da un gruppo di amici uniti dalla passione per il ciclismo, "
            "la Piesse Cycling Team è cresciuta negli anni fino a diventare una "
            "delle realtà più solide del ciclismo dilettantistico e giovanile della regione. "
            "Nata da una piccola officina di biciclette, la squadra ha saputo costruire un "
            "percorso fatto di sacrifici, allenamenti quotidiani e tanta strada macinata insieme. "
            "Oggi conta atleti di diverse categorie, un settore giovanile in espansione e uno "
            "staff tecnico che segue ogni corridore in ogni fase della stagione."
        ),
    },

    "vittorie": [
        {
            "anno": "2023",
            "titolo": "Campionato Regionale a cronometro",
            "descrizione": "Vittoria nella categoria Elite grazie a una prova cronometrata perfetta.",
        },
        {
            "anno": "2022",
            "titolo": "Giro delle Colline — Tappa Regina",
            "descrizione": "Successo in solitaria sull'ultima salita, con oltre un minuto di vantaggio.",
        },
        {
            "anno": "2021",
            "titolo": "Coppa Primavera",
            "descrizione": "Primo e terzo posto nella classifica generale a squadre.",
        },
        {
            "anno": "2019",
            "titolo": "Trofeo Città di Roma",
            "descrizione": "Vittoria di tappa e maglia di leader per tre giorni consecutivi.",
        },
    ],

    "atleti": [
        {
            "nome": "Ettore Scottoni",
            "categoria": "Allievo 2",
        },
        {
            "nome": "Davide Sellati",
            "categoria": "Allievo 1",
        },
        {
            "nome": "Giovanni Mancini",
            "categoria": "Allievo 2",
        },
        {
            "nome": "Mirko Troiani",
            "categoria": "Esordiente 2",
        },
    ],

    "staff": {
        "direttori_sportivi": ["Luca Petrolati", "Danilo Sellati"],
        "istruttori": ["Carlo Dullizia", "Marco Petrolati"],
    },

    "contatti": {
        "email": "info@piessecyclingteam.it",
        "telefono": "+39 06 1234567",
        "indirizzo": "Via dello Sport 10, 00100 Roma (RM)",
        "instagram": "https://instagram.com/piessecyclingteam",
        "facebook": "https://facebook.com/piessecyclingteam",
    },
}


@app.route("/")
def home():
    return render_template("index.html", team=TEAM_DATA)


if __name__ == "__main__":
    # In locale usa "python app.py". Su Render viene usato gunicorn (vedi Procfile).
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
