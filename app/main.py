from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

app = FastAPI(
    title="SECE API",
    description="Sistema de Expediente Clínico Electrónico",
    version="0.1.0",
)

@app.get("/health", tags=["Health"])
async def health(db: AsyncSession = Depends(get_db)):
    await db.execute(text("SELECT 1"))
    return {"status": "ok", "db": "ok"}
