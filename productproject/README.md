# API de Produtos


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