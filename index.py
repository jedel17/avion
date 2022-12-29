from flask import Flask, render_template, request, redirect, url_for

app = Flask (__name__)

passagers = []
liste=[]


@app.route('/')
def page_index ():
    return render_template('index.html')

@app.route('/cdbord')
def page_cdbord():
    return render_template('cdbord.html',personnes=liste)

@app.route('/embarquement')
def page_embarquement():
    global passagers
    if request.method == 'POST':
        formulaire = request.form.to_dict()
        passeport_found = False

        for passager in passagers:  # on parcours la liste des passagers
            if passager['passeport'] == formulaire['passeportid']:  # si on trouve le passeport
                passager['boarding'] = True  # le passager a embarqué
                passeport_found = True  # on a trouvé le passeport

        if passeport_found == True:  # si on atrouvé le passeport
            return redirect(url_for('page_index'))  # on redirige vers la page d'acceuil
        else:
            return redirect(url_for('page_passeportintrouvable'))  # sinon on redirige vers l'erreur passeport
    return render_template('embarquement.html')

@app.route('/bagages', methods=['GET', 'POST'])
def page_bagages():
    if request.method == 'POST':  # si on recoit des données de formulaires html
        global liste
        data = request.form.to_dict()  # decode les donnees du formulaire html dans un dictionnaire
        if 'button_save' in data:
            liste.append(data)
            print(data)
        # redirige vers la page commandant de bord
        return redirect(url_for('page_cdbord'))
    return render_template('bagages.html')


@app.route('/passeportintrouvable', methods=['GET','POST'])
def page_passeportintrouvable():
    return render_template('passeportintrouvable.html')
