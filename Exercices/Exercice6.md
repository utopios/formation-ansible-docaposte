## Exercice 6 Loop

On souhaite créer un playbook qui permet de copier une liste de fichier de configuration avec la possiblité d'injecter des variables dans ces fichiers.

#### Exemple du fichier de config

```ini

variable1 = val1
variable2 = val2

```

Liste de fichier de config

f1.ini {variable1= f1_val1, variable2= f1_val2}
f2.ini {variable1= f2_val1, variable2= f2_val2}
