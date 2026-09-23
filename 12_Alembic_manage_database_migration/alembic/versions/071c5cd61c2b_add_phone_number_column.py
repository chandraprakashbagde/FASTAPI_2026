"""Add phone number column

Revision ID: 071c5cd61c2b
Revises: ed5b094c34a3
Create Date: 2026-09-23 16:03:01.962848

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '071c5cd61c2b'
down_revision: Union[str, Sequence[str], None] = 'ed5b094c34a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone", sa.Integer))


def downgrade() -> None:
    op.drop_column("users","phone")
    pass
