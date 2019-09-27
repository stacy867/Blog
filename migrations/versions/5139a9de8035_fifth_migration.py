"""fifth Migration

Revision ID: 5139a9de8035
Revises: 2a12f966913e
Create Date: 2019-09-27 11:28:47.238679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5139a9de8035'
down_revision = '2a12f966913e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('writer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['writer_id'], ['writers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogposts')
    # ### end Alembic commands ###
