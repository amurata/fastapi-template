"""empty message

Revision ID: 7083cebf60fd
Revises: 6d4151b10c3e
Create Date: 2022-03-23 21:55:10.092971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7083cebf60fd'
down_revision = '6d4151b10c3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('scopes', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'scopes')
    # ### end Alembic commands ###
