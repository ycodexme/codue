from flask import Flask, render_template, request, redirect, url_for
import random
import requests

app = Flask(__name__)

# Définition des fonctions de récupération des données

def fetch_countries() -> dict:
    url = 'https://temp-numbers.xyz/admin/API/country_catagory.php'
    headers = {
        'Host': 'temp-numbers.xyz',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.0'
    }
    return requests.get(url, headers=headers).json()

def list_numbers(country:str) -> dict:
    url = 'https://temp-numbers.xyz/admin/API/get_lsit.php'
    params = {
        'no': country
    }
    headers = {
        'Host': 'temp-numbers.xyz',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.0'
    }
    return requests.post(url, params=params, headers=headers).json()

def fetch_sms(number:str) -> dict:
    url = 'https://temp-numbers.xyz/API/getAllMessages.php'
    params = {
        'no': number
    }
    headers = {
        'Host': 'temp-numbers.xyz',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.0'
    }
    return requests.post(url, params=params, headers=headers).json()

# Définir les routes
@app.route('/')
def index():
    # Afficher la page d'accueil
    return render_template('index.html')

@app.route('/countries')
def countries():
    # Obtenir la liste des pays
    countries = fetch_countries()
    return render_template('countries.html', countries=countries)

@app.route('/numbers/<country>')
def numbers(country):
    # Obtenir la liste des numéros pour un pays spécifique
    numbers = list_numbers(country)
    return render_template('numbers.html', numbers=numbers)

@app.route('/sms/<number>')
def sms(number):
    # Obtenir les messages SMS pour un numéro spécifique
    sms_list = fetch_sms(number)
    return render_template('sms.html', sms_list=sms_list)

@app.route('/inactive_numbers')
def inactive_numbers():
    # Votre logique ici
    return render_template('inactive_numbers.html')

@app.route('/faq')
def faq():
    # Votre logique ici
    return render_template('faq.html')

@app.route('/about')
def about():
    # Votre logique ici
    return render_template('about.html')

@app.route('/contact')
def contact():
    # Votre logique ici
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)
