"""init

Revision ID: 41b4cb1173ed
Revises: b047c22300c8
Create Date: 2025-07-09 16:11:59.440287

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41b4cb1173ed'
down_revision: Union[str, Sequence[str], None] = 'b047c22300c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
