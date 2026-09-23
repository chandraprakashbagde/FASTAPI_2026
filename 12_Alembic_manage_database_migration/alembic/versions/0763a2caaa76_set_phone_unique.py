"""set phone unique

Revision ID: 0763a2caaa76
Revises: 071c5cd61c2b
Create Date: 2026-09-23 16:23:06.323978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0763a2caaa76'
down_revision: Union[str, Sequence[str], None] = '071c5cd61c2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch_alter_users:
        batch_alter_users.create_unique_constraint(constraint_name="unq_users_phone", columns=["phone"]);


def downgrade() -> None:
    with op.batch_alter_table("users") as batch_alert_users:
        batch_alert_users.drop_constraint(constraint_name="unq_users_phone", type="unique")
    # op.drop_constraint(constraint_name="unq_users_phone", table_name="users", type="unique");
