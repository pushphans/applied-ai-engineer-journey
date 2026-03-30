from psycopg_pool import AsyncConnectionPool
from app.core.config import settings
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

connection_pool = AsyncConnectionPool(
    conninfo=settings.DATABASE_URL,
    max_size=10,
    kwargs={"autocommit": True, "prepare_threshold": 0},
    open=False
)

checkpointer = AsyncPostgresSaver(connection_pool)
