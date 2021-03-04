# vough_backend

## Pré-requisito

- Python 3.9
- pipenv

## Como subir o sistemano computador local

Primeiramente faça download dos arquivos do repositório sarahecomp/vough_backend. Depois navegue até a pasta **vough_backend/vough_backend**,  e então crie um ambiente vrtual python:

>>>
$ cd vough_backend/vough_backend

$ pipenv shell
>>>

Com base no arquivo Pipfile, instale as bibliotecas de depêndencia python

>>>
$ pipenv install --ignore-pipfile
>>>

É possível que a biblioteca psycopg2 tenha algum problema durante a instalação, nesse caso faça a atualização do PIP:

>>>
$ pip3 install --upgrade setuptools

$ pip3 install --upgrade pip
>>>

Atualize os dados do django e execute o serviço:

>>>
$ python manage.py migrate

$ python manage.py runserver
>>>

## A API Vough 

### Busca uma organização

GET URL_BASE/api/orgs/LOGIN_ORG

- URL_BASE -> deve ser substituida pela url onde foi feita o deploy da aplicação, ou pelo endereço padrão da máquina local que geralmente é http://127.0.0.1:8000/.
- LOGIN_ORG -> nome da organização deve ser substituido pelo login da organização que se quer consultar.


Ex:
http://127.0.0.1:8000/api/orgs/collectiveidea


Será retornado um json com o login, nome da organização e seu score. Sendo que o Score é a soma da quantidade de repositorios públicos da organização, mais o número de membros públicos.








 
