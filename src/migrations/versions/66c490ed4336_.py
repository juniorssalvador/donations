"""empty message

Revision ID: 66c490ed4336
Revises: 24f2bbf707e8
Create Date: 2020-05-16 18:16:13.277552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66c490ed4336'
down_revision = '24f2bbf707e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('donation_sate', sa.Column('date_change', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('donation_sate', 'date_change')
    # ### end Alembic commands ###
