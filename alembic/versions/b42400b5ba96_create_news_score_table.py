"""create news score table

Revision ID: b42400b5ba96
Revises: 08f394104395
Create Date: 2025-08-10 22:49:08.419839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b42400b5ba96'
down_revision: Union[str, Sequence[str], None] = '08f394104395'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
