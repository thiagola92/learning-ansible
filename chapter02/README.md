# Playbook
Playbook é uma lista de "plays", cada "play" é uma lista de tarefas.  
O formato do arquivo com estas tarefas é `yaml`.  

Início de um playbook:  
```yaml
---
- name: Example name    # (optional) "play" name
  hosts: example_group  # choose a group or "all"
  become: yes           # you want to become root?
```

Criando variáveis para a "play" utilizar:  
```yaml
---
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
---
- name: Example name
  hosts: example_group
  become: yes

  vars:
    example_var:
      - thiago
      - matheus
      - leo

  tasks:
    - name: install piper # (optional)
      apt: # module name
        name:
          - piper
          - muon
          - unrar
```

As tarefas utilizam módulos para serem executadas (os mesmo módulos utilizados com o comando `ansible -m ...`), você pode ver mais sobre os módulos existentes em https://docs.ansible.com/ansible/latest/modules/modules_by_category.html.  

Essa tarefa deve tentar instalar utilizando **apt** os aplicativos **piper**, **muon** e **unrar**. Porém, como botei para virar root, é preciso inserir a senha no arquivos **hosts**.  
```ini
[example_group]
example-machine ansible_host=192.168.0.20

[example_group:vars]
ansible_password=xxxxxxxxx
ansible_become_password=xxxxxxxxx
```

Para executar a tarefa utilize o comando `ansible-playbook` e o nome do arquivo playbook (`ansible-playbook example.yaml`):  
```shell
PLAY [Example name] *******************************************

TASK [Gathering Facts] ****************************************
ok: [example-machine]

TASK [install piper] ******************************************
ok: [example-machine]

PLAY RECAP ****************************************************
example-machine            : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

Eu já possuia esses pacotes instalados por isso no final o relatório não mostrou nenhuma mudança.  
É importante entender a sintaxe de um arquivo `yaml` para perceber que tudo até agora é apenas um item de uma possível lista de plays.  

# Reference
Ansible modules: https://docs.ansible.com/ansible/latest/modules/modules_by_category.html  