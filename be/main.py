from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from dependencies import get_db
from db_config import DATABASE_URL

# FastAPI 앱 초기화
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from your isolated FastAPI project!"}

@app.get("/env")
async def show_env():
    return {
        "DB_URL": DATABASE_URL,
    }
    
    
@app.get("/check-db")
async def check_db(db: AsyncSession = Depends(get_db)):
    # 단순히 DB 연결 여부 확인 
    try:
        result = await db.execute(text("SELECT 1"))
        one = result.scalar()
        return {"db_check": one}
    except Exception as e:
        print("🔴 DB Error:", e)
        return {"error": str(e)}
