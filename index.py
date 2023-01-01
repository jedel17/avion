from flask import Flask, render_template, request, redirect, url_for

app = Flask (__name__)

passagers = []
liste=[]



@app.route('/')
def page_index ():
    return render_template('index.html')

@app.route('/cdbord')
def page_cdbord():
    poidtotal = 0
    for passager in passagers:  # on parcours la liste des passagers
        poidtotal = poidtotal + int(passager['poid']) # a partir du poids du bagage du passager je determine le poids total de bagage
    return render_template('cdbord.html',passagers=passagers,poid=poidtotal)

@app.route('/embarquement', methods=['GET', 'POST'])
def page_embarquement():
    if request.method == 'POST':  # si on recoit des données de formulaires html
        formulaire = request.form.to_dict()  # decode les donnees du formulaire html dans un dictionnaire
        passeport_found = False  # pour l'instant on a pas trouvé le passeport
        for passager in passagers:  # on parcours la liste des passagers
            if passager['passeportid'] == formulaire['passeportid']:  # si on trouve le passeport
                passager['embarque'] = True  # le passager a embarqué
                passeport_found = True  # on a trouvé le passeport

        if passeport_found == True:  # si on atrouvé le passeport
            return redirect(url_for('page_index'))  # on redirige vers la page d'acceuil
        else:
            return redirect(url_for('page_errpassport'))  # sinon on redirige vers l'erreur passeport

    return render_template('embarquement.html')

@app.route('/bagages', methods=['GET', 'POST'])
def page_bagages():
        global passagers
        if request.method == 'POST':  # si on recoit des données de formulaires html
            formulaire = request.form.to_dict()  # decode les donnees du formulaire html dans un dictionnaire
            # construit le dictionnaire passager
            passager = {'passeportid': formulaire['passeportid'], "name": formulaire['name'],
                        "firstname": formulaire['firstname'],
                        "poid": formulaire['poid'],"embarque":False}
            passagers.append(passager)
            print(passagers)
            print(formulaire['passeportid'])
        # redirige vers la page commandant de bord
            return redirect(url_for('page_cdbord'))
        return render_template('bagages.html')


@app.route('/passeportintrouvable', methods=['GET','POST'])
def page_passeportintrouvable():

    return render_template('passeportintrouvable.html')
