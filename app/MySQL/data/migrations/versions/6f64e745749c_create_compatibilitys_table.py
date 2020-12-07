"""create compatibilitys table

Revision ID: 6f64e745749c
Revises: f993a238b8ba
Create Date: 2020-11-16 14:30:05.974626

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '6f64e745749c'
down_revision = '25f698c417da'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "compatibilitys",
        sa.Column('ProductId', sa.Integer, sa.ForeignKey('products.id'), primary_key=True),
        sa.Column('ModelId', sa.Integer, sa.ForeignKey('cars.id'), primary_key=True)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'compatibilitys' in tables:
        op.drop_table('compatibilitys')
