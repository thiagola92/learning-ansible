# Playbook
Playbook é uma lista de "plays", cada "play" é uma lista de tarefas.  
O formato do arquivo com estas tarefas é `yaml`.  

Início de um playbook:  
```yaml
--
- name: Example name    # (optional) "play" name
  hosts: example_group  # choose a group or "all"
  become: yes           # you want to become root?
```

Criando variáveis para a "play" utilizar:  
```yaml
--
- name: Example name
  hosts: example_group
  become: yes

  vars: # (optional) all variables
    example_var:
      - thiago
      - matheus
      - leo
```

Por último as tarefas que essa **play** deve fazer:  
```yaml
--
- name: Example name
  hosts: example_group
  become: yes

  vars:
    example_var:
      - thiago
      - matheus
      - leo

  tasks:
    - name: task name
```

As tarefas utilizam módulos para serem finalizadas (os mesmo módulos utilizados com o comando `ansible -m ...`)  

É importante entender a sintaxe de um arquivo `yaml` para perceber que tudo até agora é apenas um item de uma possível lista de items.  

# Reference
Ansible modules: https://docs.ansible.com/ansible/latest/modules/modules_by_category.html  