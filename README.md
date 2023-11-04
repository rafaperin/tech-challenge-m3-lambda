# Serviço de Autenticação com JWT e PostgreSQL

Este código representa um serviço básico de autenticação que utiliza Tokens Web JSON (JWT) e PostgreSQL para autenticação de usuários. O serviço é projetado para autenticar usuários usando seu CPF (Cadastro de Pessoa Física). Se o CPF fornecido existir no banco de dados PostgreSQL, o serviço gera um token JWT para o usuário.

## Pré-requisitos

Para executar este código, certifique-se de ter os seguintes pré-requisitos configurados:

- Python 3.x
- Banco de dados PostgreSQL
- Bibliotecas Python necessárias: `jwt`, `psycopg`, `psycopg-binary`

## Uso

A função principal authenticate_with_cpf(event, context) é responsável por autenticar usuários com base no CPF fornecido. Se o CPF existir no banco de dados, a função gera um token JWT para o usuário. Caso o usuário queira entrar apenas como visitante, basta não passar nenhum parâmetro no corpo da requisição. A função pode ser acionada passando um evento apropriado para ela.

## Estrutura

- `authenticate_with_cpf(event, context)`: A função principal para autenticação de usuário com base no CPF fornecido no evento. Ela utiliza o PostgreSQL para interação com o banco de dados e o JWT para geração de token.
- Variáveis de Ambiente:
    - `POSTGRES_USER`: Nome de usuário do PostgreSQL.
    - `POSTGRES_PASS`: Senha do PostgreSQL.
    - `POSTGRES_HOST`: Endereço do host do PostgreSQL.
    - `POSTGRES_DB`: Nome do banco de dados PostgreSQL.
    - `JWT_SECRET`: Chave secreta para codificação JWT.
    - `JWT_ALGORITHM`: Algoritmo para codificação JWT.