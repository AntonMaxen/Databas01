"""create order_has_products table

Revision ID: 5b1b22fb5d73
Revises: f236881243c3
Create Date: 2020-11-16 14:26:17.915190

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '5b1b22fb5d73'
down_revision = 'f236881243c3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "orders_has_products",
        sa.Column("OrderId", sa.Integer, sa.ForeignKey('orders.id'), primary_key=True),
        sa.Column("ProductId", sa.Integer, sa.ForeignKey('products.id'), primary_key=True),
        sa.Column("Amount", sa.Integer, nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'orders_has_products' in tables:
        op.drop_table('orders_has_products')
