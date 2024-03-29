"""sixth Migration

Revision ID: e965453e9fd9
Revises: 5139a9de8035
Create Date: 2019-09-27 16:01:22.565058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e965453e9fd9'
down_revision = '5139a9de8035'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogposts', sa.Column('author', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogposts', 'author')
    # ### end Alembic commands ###
