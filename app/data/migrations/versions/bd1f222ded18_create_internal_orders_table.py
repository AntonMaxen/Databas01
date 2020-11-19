"""create internal_orders table

Revision ID: bd1f222ded18
Revises: 6f64e745749c
Create Date: 2020-11-16 14:30:21.980861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.engine.reflection import Inspector

revision = 'bd1f222ded18'
down_revision = '6f64e745749c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'internal_orders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('lead_time', sa.DateTime, nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'internal_orders' in tables:
        op.drop_table('internal_orders')
