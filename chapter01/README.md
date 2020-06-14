# Install
Existem diversas manerias de instalar ansible, eu utilizei **pip**:  
`pip install ansible`  

## Configuration
As configurações do ansible são controladas pelo arquivo **ansible.cfg**. Ao executar comandos com o ansible, ele procura primeiro no diretório atual por este arquivo, então crie ele no diretório onde vai executa-lo.  

Arquivo com todas as configurações possíveis: https://github.com/ansible/ansible/blob/devel/examples/ansible.cfg  

A princípio meu arquivo **ansible.cfg** vai possuir apenas:  
```ini
[defaults]
inventory = hosts
```

O paramêtro *inventory* armazena o caminho para a lista de máquinas a quais você quer acessar  
(no caso eu aponto para o arquivo **hosts** que vai estar na mesma pasta do **ansible.cfg**)  

Crie o arquivo **hosts**, por exemplo:  
```ini
[example_group]
example-machine ansible_host=192.168.0.20

[example_group:vars]
ansible_password=xxxxxx
```

Lembre de utilizar o IP da máquina correto.  
Utilizei o usuário root apenas como exemplo, utilize geralmente um com menos permissão.  
Tenha certeza que os computadores alvos podem ser acessados por ssh, ou seja, que eles possuam openssh-server instalado e o serviço esteja executando.  

Após isso tente executar `ansible -m ping all` e verifique se a resposta é sucesso, por exemplo:  
```json
example-machine | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

# Referências
ansible.cfg: https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html  
hosts: https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#inventory-basics-formats-hosts-and-groups  
video: https://www.youtube.com/watch?v=icR-df2Olm8  