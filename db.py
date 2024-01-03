import os

import mysql.connector
from dotenv import load_dotenv
from fastapi import HTTPException, status


def connect_db() -> mysql.connector.MySQLConnection:
    load_dotenv()
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    database = os.getenv("DB_NAME")

    if None in (host, user, password, database):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="err reading env vars",
        )

    try:
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            auth_plugin="mysql_native_password",
        )  # type: ignore
    except Exception as e:
        print(f"err connecting to db: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="err connecting to db",
        )
