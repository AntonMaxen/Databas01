"""create cars table

Revision ID: 20ca6b51f7e4
Revises: 7fd507353dfa
Create Date: 2020-11-16 14:25:37.268926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20ca6b51f7e4'
down_revision = '7fd507353dfa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cars',
        sa.Column('license_number', sa.Integer, primary_key=True),
        sa.Column('brand_name', sa.String(45), nullable=False),
        sa.Column('model_name'. sa.String(100), nullable=False),
        sa.Column('prod_year', sa.Integer, nullable=False),
        sa.Column('color', sa.String(45), nullable=False),
        sa.Column('date', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('cars')
