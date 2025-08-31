from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/animacao')
def animacao():
    return render_template('animacao.html')

@app.route('/arquivo')
def arquivo():
    return render_template('arquivo.html')

@app.route('/atendimento')
def atendimento():
    return render_template('atendimento.html')

@app.route('/conta')
def conta():
    return render_template('conta.html')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

@app.route('/escarlate')
def escarlate():
    return render_template('escarlate.html')

@app.route('/escolha')
def escolha():
    return render_template('escolha.html')

@app.route('/estampas')
def estampas():
    return render_template('estampas.html')

@app.route('/forums')
def forums():
    return render_template('forums.html')

@app.route('/guia')
def guia():
    return render_template('guia.html')

@app.route('/horizontes')
def horizontes():
    return render_template('horizontes.html')

@app.route('/imprensa')
def imprensa():
    return render_template('imprensa.html')

@app.route('/informacoes')
def informacoes():
    return render_template('informacoes.html')

@app.route('/jogos')
def jogos():
    return render_template('jogos.html')

@app.route('/legends')
def legends():
    return render_template('legends.html')

@app.route('/live')
def live():
    return render_template('live.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/pocket')
def pocket():
    return render_template('pocket.html')

@app.route('/pokedex')
def pokedex():
    return render_template('pokedex.html')

@app.route('/privacidade')
def privacidade():
    return render_template('privacidade.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/termo')
def termo():
    return render_template('termo.html')

if __name__ == '__main__':
    app.run(debug=True)
