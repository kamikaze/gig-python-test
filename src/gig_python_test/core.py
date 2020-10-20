from typing import List

import sqlalchemy as sa
from asyncpg import UniqueViolationError
from databases.backends.postgres import Record

from gig_python_test.db.models import Characters


async def get_character_list(database, order_by=None) -> List[Record]:
    return await database.fetch_all(sa.select([Characters]).order_by('id'))


async def create_character(database, fields: dict) -> int:
    query = sa.insert(Characters).values(**fields)

    try:
        return await database.execute(query)
    except UniqueViolationError as e:
        raise ValueError(e.message)
