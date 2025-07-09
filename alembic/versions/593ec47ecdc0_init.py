"""init

Revision ID: 593ec47ecdc0
Revises: f5e7ab8dcc7e
Create Date: 2025-07-09 16:04:26.076900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '593ec47ecdc0'
down_revision: Union[str, Sequence[str], None] = 'f5e7ab8dcc7e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
