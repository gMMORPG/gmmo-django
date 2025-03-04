# Começando  

Primeiro, clone o repositório do GitHub e acesse o diretório do projeto:  

```bash
$ git clone git@github.com:gMMORPG/gmmo-django.git
$ cd gmmo-django
```  

Ative o ambiente virtual do seu projeto.

Instale as dependências do projeto:  

```bash
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

Em seguida, crie e aplique as migrações:  

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

Caso o retorno seja que não foram encontradas alterações execute o seguinte comando:

```bash
$ python manage.py makemigrations mmo
$ python manage.py migrate
```

Agora você pode criar um super user e executar o servidor de desenvolvimento:  
Ao criar executar o ```createsuperuser```, será pedido usuário, email, senha, confirmação de senha.

```bash
$ python manage.py createsuperuser
$ python manage.py runserver 0.0.0.0:8000
```
