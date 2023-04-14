"""empty message

Revision ID: 393731516c13
Revises: 14d399d3b026
Create Date: 2023-04-11 17:37:57.032482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '393731516c13'
down_revision = '14d399d3b026'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
