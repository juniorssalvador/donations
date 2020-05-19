"""empty message

Revision ID: 566de9eaa630
Revises: 66c490ed4336
Create Date: 2020-05-19 12:25:56.164509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '566de9eaa630'
down_revision = '66c490ed4336'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('my_donations', sa.Column('donations_objects_id', sa.Integer(), nullable=False))
    op.drop_constraint('my_donations_donations_objects.id_fkey', 'my_donations', type_='foreignkey')
    op.create_foreign_key(None, 'my_donations', 'donation_objects', ['donations_objects_id'], ['id'])
    op.drop_column('my_donations', 'donations_objects.id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('my_donations', sa.Column('donations_objects.id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'my_donations', type_='foreignkey')
    op.create_foreign_key('my_donations_donations_objects.id_fkey', 'my_donations', 'donation_objects', ['donations_objects.id'], ['id'])
    op.drop_column('my_donations', 'donations_objects_id')
    # ### end Alembic commands ###