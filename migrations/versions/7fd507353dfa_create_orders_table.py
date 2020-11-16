"""create orders table

Revision ID: 7fd507353dfa
Revises: e8f0ec232d0c
Create Date: 2020-11-16 13:54:19.543840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fd507353dfa'
down_revision = 'e8f0ec232d0c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('total_amount', sa.Integer, nullable=False),
        sa.Column('payment_status', sa.String(100), nullable=False),
        sa.Column('shipping_date', sa.DateTime, nullable=False),
        sa.Column('customer_id', sa.Integer, sa.ForeignKey('customers.id')),
        sa.Column('employee_id', sa.Integer, sa.ForeignKey('employees.id')),
        sa.Column('shop_id', sa.Integer, sa.ForeignKey('shops.id'))
    )


def downgrade():
    op.drop_table('orders')
