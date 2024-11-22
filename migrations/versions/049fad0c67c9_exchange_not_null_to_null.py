"""exchange not null to null

Revision ID: 049fad0c67c9
Revises: 65fa1cd97a0e
Create Date: 2024-11-21 19:23:46.910784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '049fad0c67c9'
down_revision: Union[str, None] = '65fa1cd97a0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notes', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('notes', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notes', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('notes', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###