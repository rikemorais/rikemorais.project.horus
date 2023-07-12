import os

import pytest
from pymongo import MongoClient


def test_mongodb_connection():
    uri_mongodb = os.environ.get("URI_MONGODB")
    if uri_mongodb is None:
        pytest.skip("Variável de ambiente URI_MONGODB não configurada.")

    try:
        client = MongoClient(uri_mongodb)
        db = client["admin"]
        db.command("ping")
        client.close()
    except Exception as e:
        pytest.fail(f"Falha ao Conectar ao MongoDB: {str(e)}")
