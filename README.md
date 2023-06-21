## 🛠️ Como usar


### :waxing_crescent_moon: Projeto backend:
#### Requisitos:
* Instalação do PostgreSQL (a partir da versão 13.3)
> https://www.postgresql.org/
 
* Instalação do Python (a partir da versão 3.9)
> https://www.python.org/

* Instalação do Git
> https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git
 

#### Clonando projeto para máquina local:

* Criar repositório onde será mantido o projeto. 
> Ex.: C:\Users\seunome\desenv\sisarqimhc
* posicionar-se no diretório
* No terminal, executar o comando:
```
https://github.com/csdamo/sisarqimhc.git
```

#### Criando ambiente virtual de desenvolvimento:

* No prompt de comando, executar o comando
```
pip install virtualenv
```

* Pelo prompt, vá até o diretório do projeto e execute o comando a seguir. 
```
virtualenv venv
``` 
será criada uma pasta dentro do repositório com o nome "venv"


* Ative o ambiente virtual de desenvolvimento: ainda no prompt de comando (dentro do repositório do projeto) execute o comando
```
venv/Scripts/activate 
```
(Windows) 
```
source venv/bin/activate
```
(Linux) 

* Para você saber se o ambiente virtual foi ativado, perceba se antes do caminho do seu diretório, aparece o nome do ambiente entre parênteses. 
> Ex.: (venv) C:\Users\seunome\desenv\badmintonapi>


#### Iniciando a configuração do projeto 

* Dentro do ambiente virtual, para instalar as bibliotecas na versão correta para o projeto , rodar o comando
```
pip install -r requirements.txt
```

* Criar o arquivo .env na raiz do projeot e setar as seguintes variáveis:
SECRET_KEY = ###
DATABASE = sisarqimhc
USER = nome do usuario
PASSWORD = senha do banco de dados
HOST = localhost

#### Criar Data Base:
* Criar Banco de edados com o nome 'sisarqimhc'

* Denro do diretório do projeto, com o ambiente virtual ativado, rodar o comando 
```
python manage.py migrate
```
esse comando fará com que as tabelas do banco de dados sejam criadas

* Criar super usuário: rode o comando:

```
python manage.py createsuperuser
```
será necessário informar um login, e-mail e senha (você usará o e-mail para fazer login) 

#### Subindo Servidor:
* Rodar o comando:
```
python manage.py runserver
```
