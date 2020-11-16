"""create products_has_associates table

Revision ID: 25f698c417da
Revises: 1654a908f3a0
Create Date: 2020-11-16 14:28:22.565946

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '25f698c417da'
down_revision = '1654a908f3a0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products_has_associates',
        sa.Column("ProductId", sa.Integer, sa.ForeignKey('products.id'), primary_key=True),
        sa.Column("AssociateId", sa.Integer, sa.ForeignKey('associates.id'), primary_key=True)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'products_has_associates' in tables:
        op.drop_table('products_has_associates')
