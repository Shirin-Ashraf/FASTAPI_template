"""added age column to users

Revision ID: 2172a3e0237c
Revises: 58271ef7ea5e
Create Date: 2025-05-06 12:06:15.623547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2172a3e0237c'
down_revision: Union[str, None] = '58271ef7ea5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'age')
    # ### end Alembic commands ###
