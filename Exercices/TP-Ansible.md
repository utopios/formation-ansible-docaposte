## TP Ansible

On souhaite utiliser Ansible pour configurer et déployer une application composée de :

- Une partie front pour le vote port 80
- Une partie front pour l'affichage des résultats port = 4000.
- Une partie worker.
- Une base de données postgresql port 5432.
- Une base de cache redis port 6379.

Chaque partie est déployée dans un conteneur docker.

Les ressources ansible vont permettre :

- Vérifier l'installation des différents composants nécessaires.
- La construction des images docker.
- Le démarrage des conteneurs.

Lien du dépôt git de l'application: https://github.com/utopios/TP-Deploiement-Ansible   

### HELP

Module Ansible => install apt, yum,...
Module COPY pour copier le code source ou MODULE GIT pour cloner le dépôt.
Module docker_image pour construire les images ou MODULE SHELL.
Module docker_container pour démarrer les conteneurs ou MODULE SHELL



