"""init

Revision ID: f5e7ab8dcc7e
Revises: 7a1812ce6ead
Create Date: 2025-07-09 16:00:11.069504

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5e7ab8dcc7e'
down_revision: Union[str, Sequence[str], None] = '7a1812ce6ead'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
