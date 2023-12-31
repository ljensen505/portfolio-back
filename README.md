### Backend for lucasjensen.me

build with FastAPI and MySQL

### Setup

- create and activate virtual environment
- install requirements
- create database with mysql, note db name
- create .env file with db credentials (see `.env.example`)
- ensure mysql user has permissions to create tables
- run `create_tables.sql` to create tables

```bash
mysql -u [username] -p [database] < create_tables.sql
```

### Run

```bash
uvicorn main:app --reload
```

### Test

```bash
pytest -s
```
