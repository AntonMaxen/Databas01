"""create storage table

Revision ID: a4fa6af9ee0b
Revises: 5b1b22fb5d73
Create Date: 2020-11-16 14:26:50.324351

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'a4fa6af9ee0b'
down_revision = '5b1b22fb5d73'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "storages",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("product_amount", sa.String(45), nullable=False),
        sa.Column("min_amount", sa.String(100), nullable=False),
        sa.Column("reorder_amount", sa.Integer, nullable=False),
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'storages' in tables:
        op.drop_table('storages')
