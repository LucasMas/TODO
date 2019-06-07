from flask import Flask, jsonify, request, abort


app = Flask(__name__)

tasks = [] #Declaration d'une liste vide

@app.route('/list', methods=['GET'])
def list_tasks():
    return jsonify({'tasks':tasks}) #Return les elements contenus dans la liste

@app.route('/add', methods=['POST'])
def add_task():
    if not request.json or not 'title' in request.json or not 'description' in request.json: #Gestion d'erreur dans le cas où le nom ou la description ne serait pas précisé
        abort(400)
    temp = 1 #Variable temporaire initialisée a 1, elle servira a affecté un ID a la tache ajouté
    if (len(tasks) > 0):            #  |Si le tableau contient deja au moins un élement alors on recupere l'ID du dernier et on ajoute 1 à la variable temp
        temp = tasks[-1]['id'] + 1  #  |
    task = {                                        #
        'id':temp,                                  #
        'title': request.json['title'],             # On crée et on affecte les valeurs recupérées à la nouvelle tache
        'description': request.json['description']  #
    }                                               #
    tasks.append(task) #On ajoute la tache a la liste
    return jsonify({'task': task}), 201

@app.route('/supp/<int:id>', methods=['DELETE'])
def supp_task(id): #On prend en argument l'ID precisé dans l'adresse
    task = [task for task in tasks if task['id'] ==id] #On cherche dans la liste la tache correspondante
    if len(task) == 0: #Si cette tache n'exite pas alors on renvoie une erreur et on arrête
        abort(400)
    tasks.remove(task[0]) #Sinon si la tache existe on la supprime de la liste
    return jsonify({'result':True})

if __name__ == '__main__':
    app.run(debug=True)
