"""initial

Revision ID: 137f0580b7c3
Revises: 
Create Date: 2015-04-12 18:03:42.916140

"""

# revision identifiers, used by Alembic.
revision = '137f0580b7c3'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
     op.create_table('users',
        sa.Column(
            'username',
            sa.String(length=255),
            nullable=False),
        sa.Column(
            'password',
            sa.String(length=255),
            nullable=False
        ),
        sa.PrimaryKeyConstraint('username')
    )


def downgrade():
    pass
