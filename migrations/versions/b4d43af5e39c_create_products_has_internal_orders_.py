"""create products_has_internal_orders table

Revision ID: b4d43af5e39c
Revises: bd1f222ded18
Create Date: 2020-11-16 14:31:01.799669

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'b4d43af5e39c'
down_revision = 'bd1f222ded18'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products_has_internal_orders',
        sa.Column('ProductId', sa.Integer, sa.ForeignKey('products.id'), primary_key=True),
        sa.Column('InternalOrderId', sa.Integer, sa.ForeignKey('internal_orders.id'), primary_key=True)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'products_has_internal_orders' in tables:
        op.drop_table('products_has_internal_orders')
