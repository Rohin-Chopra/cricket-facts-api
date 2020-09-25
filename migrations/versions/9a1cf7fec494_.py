"""empty message

Revision ID: 9a1cf7fec494
Revises: 
Create Date: 2020-09-25 15:50:23.338904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a1cf7fec494'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cricket_fact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fact', sa.String(), nullable=False),
    sa.Column('source', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fact')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cricket_fact')
    # ### end Alembic commands ###
