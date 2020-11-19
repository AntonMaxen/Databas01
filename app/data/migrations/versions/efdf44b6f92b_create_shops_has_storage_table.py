"""create shops_has_storage table

Revision ID: efdf44b6f92b
Revises: a4fa6af9ee0b
Create Date: 2020-11-16 14:27:36.028295

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'efdf44b6f92b'
down_revision = 'a4fa6af9ee0b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "shops_has_storages",
        sa.Column("ShopId", sa.Integer, sa.ForeignKey("shops.id"), primary_key=True),
        sa.Column("StorageId", sa.Integer, sa.ForeignKey("storages.id"), primary_key=True),
        sa.Column("ProductId", sa.Integer, sa.ForeignKey("products.id"))
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'shops_has_storages' in tables:
        op.drop_table('shops_has_storages')
