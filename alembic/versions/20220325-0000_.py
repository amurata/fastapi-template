"""empty message

Revision ID: e4b9622be822
Revises: 7083cebf60fd
Create Date: 2022-03-25 00:00:54.972996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4b9622be822'
down_revision = '7083cebf60fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('jobs', 'description')
    # ### end Alembic commands ###
