## TP Ansible

On souhaite utiliser Ansible pour configurer et déployer une application composée de :

- Une partie front pour le vote
- Une partie front pour l'affichage des résultats.
- Une partie worker.
- Une base de données postgresql.
- Une base de cache redis.

Chaque partie est déployée dans un conteneur docker.

Les ressources ansible vont permettre :

- Vérifier l'installation des différents composants nécessaires.
- La construction des images docker.
- Le démarrage des conteneurs.

Lien du dépôt git de l'application: https://github.com/utopios/TP-Deploiement-Ansible   

