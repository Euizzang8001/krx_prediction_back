"""delete not nullable in  news score table

Revision ID: c83262b5af5c
Revises: b42400b5ba96
Create Date: 2025-08-10 22:58:38.063713

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c83262b5af5c'
down_revision: Union[str, Sequence[str], None] = 'b42400b5ba96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
