"""create user table

Revision ID: 16f15c4abafa
Revises:
Create Date: 2015-11-02 17:15:26.497651

"""

# revision identifiers, used by Alembic.
revision = '16f15c4abafa'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key = True),
        sa.Column('email', sa.String(50), nullable = False),
        sa.Column('first_name', sa.String(50), nullable = False),
        sa.Column('last_name', sa.String(50), nullable = False)
    )

def downgrade():
    pass
