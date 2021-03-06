"""empty message

Revision ID: abe42cc715f5
Revises: ee869b997c4c
Create Date: 2018-06-27 00:41:14.409718

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'abe42cc715f5'
down_revision = 'ee869b997c4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cm_website', sa.Column('web_site_host', sa.String(length=64), nullable=True))
    op.drop_column('cm_website', 'web_site_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cm_website', sa.Column('web_site_name', mysql.VARCHAR(collation='utf8_bin', length=64), nullable=True))
    op.drop_column('cm_website', 'web_site_host')
    # ### end Alembic commands ###
