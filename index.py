from flask import Flask, render_template, request, redirect, url_for

app = Flask (__name__)

passagers = []
liste=[]
embarque=[]


@app.route('/')
def page_index ():
    return render_template('index.html')

@app.route('/cdbord')
def page_cdbord():
    return render_template('cdbord.html',personnes=liste,data2=passagers)

@app.route('/embarquement', methods=['GET', 'POST'])
def page_embarquement():
    if request.method == 'POST':
        global passagers
        data = request.form.to_dict()
        if 'btn1' in data:
            passagers.append(data)
            print(passagers)
            return redirect(url_for('page_cdbord'))
            return render_template('cdbord.html')
    return render_template('embarquement.html')


@app.route('/bagages', methods=['GET', 'POST'])
def page_bagages():
    if request.method == 'POST':  # si on recoit des données de formulaires html
        global liste
        data = request.form.to_dict()  # decode les donnees du formulaire html dans un dictionnaire
        if 'button_save' in data:
            liste.append(data)
            print(liste)
        # redirige vers la page commandant de bord
        return redirect(url_for('page_cdbord'))
    return render_template('bagages.html')


@app.route('/passeportintrouvable', methods=['GET','POST'])
def page_passeportintrouvable():
    return render_template('passeportintrouvable.html')
