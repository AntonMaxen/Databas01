"""create associates table

Revision ID: 1654a908f3a0
Revises: d021d31441aa
Create Date: 2020-11-16 14:28:07.334976

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '1654a908f3a0'
down_revision = 'd021d31441aa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "associates",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('phone', sa.String(45), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('address_line_one', sa.String(100), nullable=False),
        sa.Column('address_line_two', sa.String(100), nullable=True),
        sa.Column('zip_code', sa.String(45), nullable=False),
        sa.Column('city', sa.String(100), nullable=False),
        sa.Column('country', sa.String(100), nullable=False),
        sa.Column('associates_category', sa.String(100), nullable=False),
        sa.Column('contact_person_id', sa.Integer, sa.ForeignKey('contact_persons.id'))
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'associates' in tables:
        op.drop_table('associates')