from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='/Users/an-yunhoe/Desktop/dev/calbockio/be/.env', override=True)

DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
print("os.environ:", os.environ)

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"