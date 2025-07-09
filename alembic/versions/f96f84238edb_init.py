"""init

Revision ID: f96f84238edb
Revises: 593ec47ecdc0
Create Date: 2025-07-09 16:06:38.433992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f96f84238edb'
down_revision: Union[str, Sequence[str], None] = '593ec47ecdc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
