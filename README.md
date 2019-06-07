# TODO
Fonctionnalités :
     -Lister des taches
          route : '/list' | method : GET
          commande : curl -i http://localhost:5000/list
          (Initalement la liste est vide)
     -Ajouter une tache
          route : '/add' | method : POST
          commande : curl -i -H "Content-Type: application/json" -X POST -d '{"title":"NomDeLatache",                                              "description","DescriptionDeLaTache"}' http://localhost:5000/add
          (Si il manque title ou description n'est pas precisé une erreur serra renvoyé, code d'erreur 400,
          l'ID de la tache sera automatiquement ajouté)
     -Supprimer une tache
          route : '/supp/ID' | method : DELETE
          commande : curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/supp/ID
          (ID étant l'ID de la tache a supprimer, si aucunes tache n'a pour ID celle qui est donnée alors code d'erreur 400)
