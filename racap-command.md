**Commande playbook avec json var**
    ansible-playbook playbook.yml --extra-vars "@path_json_var.json"

**Commande playboo avec tag**
ansible-playbook -i config/inventory.yml playbooks/tag-playbook.yml --tags "install"
ansible-playbook -i config/inventory.yml playbooks/tag-playbook.yml --skip-tags "install"
