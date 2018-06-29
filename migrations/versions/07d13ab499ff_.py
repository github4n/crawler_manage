"""empty message

Revision ID: 07d13ab499ff
Revises: 47c5291f88d7
Create Date: 2018-06-14 21:04:24.897186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07d13ab499ff'
down_revision = '47c5291f88d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cm_users',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=225), nullable=False),
    sa.Column('nike_name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('u_id'),
    sa.UniqueConstraint('nike_name'),
    sa.UniqueConstraint('u_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('cm_website',
    sa.Column('w_id', sa.Integer(), nullable=False),
    sa.Column('web_site_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('w_id'),
    sa.UniqueConstraint('w_id')
    )
    op.create_table('cm_cookie',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('c_id', sa.Integer(), nullable=False),
    sa.Column('cookies_String', sa.Text(), nullable=True),
    sa.Column('w_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['w_id'], ['cm_website.w_id'], ),
    sa.PrimaryKeyConstraint('c_id')
    )
    op.create_index(op.f('ix_cm_cookie_c_id'), 'cm_cookie', ['c_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cm_cookie_c_id'), table_name='cm_cookie')
    op.drop_table('cm_cookie')
    op.drop_table('cm_website')
    op.drop_table('cm_users')
    # ### end Alembic commands ###