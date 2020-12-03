"""create products table

Revision ID: f236881243c3
Revises: 6125d40ce401
Create Date: 2020-11-16 14:26:03.414234

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'f236881243c3'
down_revision = '6125d40ce401'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("product_name", sa.String(100), nullable=False),
        sa.Column("description", sa.String(2000), nullable=False),
        sa.Column("purchase_price", sa.String(45), nullable=False),
        sa.Column("retail_price", sa.String(100), nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'products' in tables:
        op.drop_table('products')
