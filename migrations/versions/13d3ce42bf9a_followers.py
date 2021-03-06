"""followers

Revision ID: 13d3ce42bf9a
Revises: 230e3411fe7f
Create Date: 2020-05-14 22:38:31.477321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13d3ce42bf9a'
down_revision = '230e3411fe7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
