"""create car_models table

Revision ID: f993a238b8ba
Revises: 25f698c417da
Create Date: 2020-11-16 14:29:26.085998

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'f993a238b8ba'
down_revision = '25f698c417da'
branch_labels = None
depends_on = None


def upgrade():
    sa.Column('id', sa.Integer, primary_key=True)
    sa.Column('car_brand', sa.String(100), nullable=False)
    sa.Column('model_name', sa.String(100), nullable=False)
    sa.Column('production_year', sa.String(100), nullable=False)
    sa.Column('colour', sa.String(45), nullable=True)


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'car_models' in tables:
        op.drop_table('car_models')
