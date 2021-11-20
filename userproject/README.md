# API de Usuários

## Instalando Dependências:
    pip install -r requirements.txt
    
## Criando collection no banco:

- criando migração:
```
    python manage.py makemigrations userapi
```
- criando a collection:
```
    python manage.py migrate userapi
```

## Executando:

- Executando aplicativo:
```
    python manage.py runserver
```
O servidor será executando na url: **http://localhost:5852**

## Rotas:
 - Todos usuários **(método GET)**:
    ```
        /api/user
    ```

 - Retorna usuário pelo id **(método GET)**:
    ```
        /api/user/{id}
    ```
    
 - Cria usuário **(método POST)**:
    ```
        /api/user
    ```
    exemplo de json enviado no body:
    ```
    {
        "login":"login_user",
        "senha": "senha_user",
        "data_nascimento":"YYY-MM-DD"
    }
    ```
    **OBS**: login e data_nascimento são obrigatórios, já senha, caso não senha enviada, ou enviada vazia, a api cria uma nova senha aleatória.

 - Altera usuário **(método PUT)**:
    ```
        /api/user/{id}
    ```
    exemplo de json enviado no body:
    ```
    {
        "login":"login_user",
        "senha": "senha_user",
        "data_nascimento":"YYY-MM-DD"
    }
    ```
    **OBS**: login e data_nascimento são obrigatórios.

- Deleta usuário **(método DELETE)**:
    ```
        /api/user/{id}
    ```

### Foi criado um método que é disparado a cada 10 minutos, onde ele pega todos os dados cadastrados no banco e exporta para uma tabela em formato .xlsx no diretório **userapi/files**