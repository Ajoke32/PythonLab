"""empty message

Revision ID: 5d780272df1d
Revises: 
Create Date: 2022-12-11 01:45:14.390740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d780272df1d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('albumname', sa.String(length=25), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('img', sa.String(length=20), nullable=False),
    sa.Column('edit_data', sa.DateTime(), nullable=False),
    sa.Column('editor_name', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_name', sa.String(length=25), nullable=False),
    sa.Column('link', sa.String(length=150), nullable=True),
    sa.Column('audio', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=25), nullable=True),
    sa.Column('surname', sa.String(length=25), nullable=True),
    sa.Column('email', sa.String(length=35), nullable=False),
    sa.Column('login', sa.String(length=20), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('song')
    op.drop_table('albums')
    # ### end Alembic commands ###
