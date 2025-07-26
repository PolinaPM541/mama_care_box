from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from core.config import settings
from models.base import Base
from models.user import User
from models.product import Product, Category, Subcategory
from models.basket import Basket
from models.order import Order
from sqlalchemy import engine_from_config, pool
import asyncio

from alembic import context

# this is the Alembic Config object
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Исправлено: устанавливаем target_metadata
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    # Получаем URL из настроек, а не из alembic.ini
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_async_engine(settings.DATABASE_URL, echo=True)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())