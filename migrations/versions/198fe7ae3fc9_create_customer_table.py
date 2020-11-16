"""create customer table

Revision ID: 198fe7ae3fc9
Revises: 
Create Date: 2020-11-16 13:06:58.250956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '198fe7ae3fc9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(100), nullable=False),
        sa.Column('last_name', sa.String(100), nullable=False),
        sa.Column('phone', sa.String(45), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('company_name', sa.String(100), nullable=True),
        sa.Column('organisation_number', sa.String(100), nullable=True),
        sa.Column('address_line_one', sa.String(100), nullable=False),
        sa.Column('address_line_two', sa.String(100), nullable=True),
        sa.Column('zip_code', sa.String(45), nullable=False),
        sa.Column('city', sa.String(100), nullable=False),
        sa.Column('country', sa.String(100), nullable=True),
    )


def downgrade():
    op.drop_table('customers')
