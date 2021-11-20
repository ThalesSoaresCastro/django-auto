# Iniciando projetos

- userapi depende de um banco mongodb e productapi de um banco mysql

- Os dois bancos de dados necessários estão configurados no docker-compose nas portas
    - mongodb na porta 5850
    - mysql na porta 5851

- Para iniciar os containers:
    ```
    docker-compose up -d
    ```
- Para parar os containers:
    ```
    docker-compose down -d
    ```

# API de Usuários

- Arquivos no diretório **userproject**

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


# API de Produtos

- Arquivos no diretório **productproject**

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
O servidor será executando na url: **http://localhost:5853**



## Rotas:
 - Todos produtos **(método GET)**:
    ```
        /api/product/all
    ```

 - Retorna produto pelo id **(método GET)**:
    ```
        /api/product/{id}
    ```
    
 - Cria produto **(método POST)**:
    ```
        /api/product/create
    ```
    exemplo de json enviado no body:
    ```
    {
        "nome": "nome_produto",
        "descricao": "descricao_produto",
        "quantidade": 1,
        "preco": 12.2
    }
    ```
    **OBS**: todos os parâmetros são necessários.

 - Altera produto **(método PUT)**:
    ```
        /api/product/{id}/change
    ```
    exemplo de json enviado no body:
    ```
    {
        "nome": "nome_produto",
        "descricao": "descricao_produto",
        "quantidade": 1,
        "preco": 12.2
    }
    ```
    **OBS**: todos os parâmetros são obrigatórios.

- Deleta produto **(método DELETE)**:
    ```
        /api/product/{id}/delete
    ```

### Foi criado um método que é disparado a cada 10 minutos, onde ele pega todos os dados cadastrados no banco e exporta para uma tabela em formato .xlsx no diretório **productapi/files**


# APP para baixar os dados

- arquivos no diretório **apiscrapping**

## Instalando e executando:
- Fazer a instalação das dependências necessárias:
    ```
    pip install -r requirements.txt
    ```

- Executando:
    ```    
    python scrapping.py
    ```

### Será criada uma pasta com o nome *files* com os arquivos das duas api's em .xlsx.