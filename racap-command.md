**Commande playbook avec json var**
    ansible-playbook playbook.yml --extra-vars "@path_json_var.json"

**Commande playbook avec tag**
ansible-playbook -i config/inventory.yml playbooks/tag-playbook.yml --tags "install"
ansible-playbook -i config/inventory.yml playbooks/tag-playbook.yml --skip-tags "install"

**Commande ansible vault**

 pour crypter un fichier avec ansible-vault, on peut utiliser la commande 
 ansible-vault encrypt file_name.yml
 ansible-vault decrypt file_name.yml

utilisation des variables cryptées dans playbook est possible, en indiquant la phrase de cryptage en utiliasnt le flag  --ask-vault-pass

ansible-playbook -i config/inventory.yml playbooks-with-vault/playbook.yml --ask-vault-pass --private-key ./ansible-formation.pem

