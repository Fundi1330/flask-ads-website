"""empty message

Revision ID: 58e74244cc22
Revises: 
Create Date: 2023-02-28 15:03:04.598270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58e74244cc22'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Ads', schema=None) as batch_op:
        batch_op.drop_index('ix_Ads_path_to_image')
        batch_op.drop_column('path_to_image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Ads', schema=None) as batch_op:
        batch_op.add_column(sa.Column('path_to_image', sa.VARCHAR(), nullable=True))
        batch_op.create_index('ix_Ads_path_to_image', ['path_to_image'], unique=False)

    # ### end Alembic commands ###