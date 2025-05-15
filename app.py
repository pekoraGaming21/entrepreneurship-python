from flask import Flask, render_template, request
from flask_caching import Cache

from Character import Character
from Substat import Substat
from Artifact import Artifact
from BetterArtifacts import BetterArtifacts

app = Flask(__name__)

characters = []

characterID = 0
with open("files\characters.txt", "r") as c:
    best = 0
    for x in c:
        characters.append({
            "name":x.split(';')[1],
            "id":x.split(';')[0]
        })
        if x.split(';')[0] > best:
            best = x.split(';')[0]
    characterID = best

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/character")
def character():
    return render_template("character.html")

def daytonify(value):
    if value == "":
        return 0.0
    else:
        try:
            return float(value)
        except:
            return "AAAAAAAAAAAAAAAAAAAAAA"

@app.route("/calculator")
def calculator():
    return render_template("calculator.html")

@app.route("/calculator/submit")
def calculatorSubmit():
    jim = BetterArtifacts(request.form['character'])


@app.route("/character/submit", methods=['POST'])
def characterSubmit():
    a1 = Artifact("HP",daytonify(request.form['flowerMain']), Substat(request.form['flowerSub1'], daytonify(request.form['flowerSub1V'])), Substat(request.form['flowerSub2'], daytonify(request.form['flowerSub2V'])), Substat(request.form['flowerSub3'], daytonify(request.form['flowerSub3V'])), Substat(request.form['flowerSub4'], daytonify(request.form['flowerSub4V'])))
    a2 = Artifact("ATK",daytonify(request.form['featherMain']), Substat(request.form['featherSub1'], daytonify(request.form['featherSub1V'])), Substat(request.form['featherSub2'], daytonify(request.form['featherSub2V'])), Substat(request.form['featherSub3'], daytonify(request.form['featherSub3V'])), Substat(request.form['featherSub4'], daytonify(request.form['featherSub4V'])))
    a3 = Artifact(request.form['sandsMain'],daytonify(request.form['sandsMainV']), Substat(request.form['sandsSub1'], daytonify(request.form['sandsSub1V'])), Substat(request.form['sandsSub2'], daytonify(request.form['sandsSub2V'])), Substat(request.form['sandsSub3'], daytonify(request.form['sandsSub3V'])), Substat(request.form['sandsSub4'], daytonify(request.form['sandsSub4V'])))
    a4 = Artifact(request.form['gobletMain'],daytonify(request.form['gobletMainV']), Substat(request.form['gobletSub1'], daytonify(request.form['gobletSub1V'])), Substat(request.form['gobletSub2'], daytonify(request.form['gobletSub2V'])), Substat(request.form['gobletSub3'], daytonify(request.form['gobletSub3V'])), Substat(request.form['gobletSub4'], daytonify(request.form['gobletSub4V'])))
    a5 = Artifact(request.form['circletMain'],daytonify(request.form['circletMainV']), Substat(request.form['circletSub1'], daytonify(request.form['circletSub1V'])), Substat(request.form['circletSub2'], daytonify(request.form['circletSub2V'])), Substat(request.form['circletSub3'], daytonify(request.form['circletSub3V'])), Substat(request.form['circletSub4'], daytonify(request.form['circletSub4V'])))

    list = [
    a1,
    a2,
    a3,
    a4,
    a5]
    # characters["Ganyu"] = Character("Cryo", 90, 9796.73, 334.85, 630.21, request.form['weapon'], 541.83, list, "CD", 38.4)
    with open("files\characters.txt", "a") as c:
        c.write(f"{characterID};{request.form['character']};{a1};{a2};{a3};{a4};{a5}")
    characterID += 1
    return render_template('characterStats.html', characterName=request.form['character'], ATK=characters["Ganyu"].getTotalATK(),DEF=characters["Ganyu"].getTotalDEF(),HP=characters["Ganyu"].getTotalHP())


