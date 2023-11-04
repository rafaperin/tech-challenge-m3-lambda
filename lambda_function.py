import jwt
import psycopg
import os
import random
import json

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASS = os.environ.get("POSTGRES_PASS")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_DB = os.environ.get("POSTGRES_DB")

JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")

def authenticate_with_cpf(event, context) -> dict:
    if 'body' in event:
        json_body = json.loads(event['body'])
        if 'cpf' in json_body:
            pg_uri = f"postgres://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"
            conn_dict = psycopg.conninfo.conninfo_to_dict(pg_uri)
            with psycopg.connect(**conn_dict) as conn:
                with conn.cursor() as cur:
                    cur.execute(f"SELECT first_name FROM customers WHERE cpf = '{json_body['cpf']}';")
                    result = cur.fetchone()
            if result is None:
                message = f"User with cpf {json_body['cpf']} not found"
                jwt_token = None
            else:
                message = f"User {result[0]} authenticated successfully"
                jwt_token = jwt.encode({"user_name": result[0]}, JWT_SECRET, algorithm=JWT_ALGORITHM)            
    else:
        message = "Authenticated as guest"
        jwt_token = jwt.encode({"user_name": "Visitante " + str(random.randint(100000, 999999))}, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"message": message , "jwt_token": jwt_token}
