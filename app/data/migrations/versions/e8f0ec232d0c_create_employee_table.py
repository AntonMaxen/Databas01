"""create employee table

Revision ID: e8f0ec232d0c
Revises: 0bdb435c7e19
Create Date: 2020-11-16 13:45:42.552103

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'e8f0ec232d0c'
down_revision = '0bdb435c7e19'
branch_labels = None
depends_on = None
conn = op.get_bind()
inspector = Inspector.from_engine(conn)
tables = inspector.get_table_names()


def upgrade():
    if 'employees' not in tables:
        op.create_table(
            'employees',

            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('first_name', sa.String(100), nullable=False),
            sa.Column('last_name', sa.String(100), nullable=False),
            sa.Column('job_title', sa.String(45), nullable=False),
            sa.Column('email', sa.String(45), nullable=False),
            sa.Column('reports_to', sa.Integer, nullable=False),
            sa.Column('shop_id', sa.Integer, sa.ForeignKey('shops.id'))
        )


def downgrade():
    if 'employees' in tables:
        op.drop_table('employees')
