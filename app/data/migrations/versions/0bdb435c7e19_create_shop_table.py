"""create shop table

Revision ID: 0bdb435c7e19
Revises: 198fe7ae3fc9
Create Date: 2020-11-16 13:41:26.654698

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '0bdb435c7e19'
down_revision = '198fe7ae3fc9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'shops',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('phone', sa.String(25), nullable=False),
        sa.Column('email', sa.String(45), nullable=False),
        sa.Column('address_line_one', sa.String(100), nullable=False),
        sa.Column('address_line_two', sa.String(100), nullable=False),
        sa.Column('city', sa.String(192), nullable=False),
        sa.Column('country', sa.String(60), nullable=False)
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'shops' in tables:
        op.drop_table('shops')
