## Exercice 5 condition
Gestion conditionnelle des packages sur différentes distributions Linux

Dans cet exercice, vous devez créer un playbook Ansible qui installe un package spécifique en fonction de la distribution Linux et de la version du système de l'hôte.

    Si l'hôte est une machine tournant sur CentOS 7, votre playbook doit installer le package httpd.
    Si l'hôte est une machine tournant sur Ubuntu 20.04, votre playbook doit installer le package apache2.

Votre playbook doit recueillir les facts de l'hôte pour déterminer la distribution et la version du système d'exploitation, et utiliser ces informations pour décider quel package installer.