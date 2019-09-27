"""sixth Migration

Revision ID: 53a3fdef4392
Revises: e965453e9fd9
Create Date: 2019-09-27 17:00:41.989068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53a3fdef4392'
down_revision = 'e965453e9fd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feedback', sa.String(length=255), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('writer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blogposts.id'], ),
    sa.ForeignKeyConstraint(['writer_id'], ['writers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###