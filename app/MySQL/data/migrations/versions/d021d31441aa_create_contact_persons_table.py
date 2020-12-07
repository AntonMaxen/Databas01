"""create contact_persons table

Revision ID: d021d31441aa
Revises: efdf44b6f92b
Create Date: 2020-11-16 14:27:52.156003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy.engine.reflection import Inspector

revision = 'd021d31441aa'
down_revision = 'efdf44b6f92b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'contact_persons',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(45), nullable=False),
        sa.Column('last_name', sa.String(45), nullable=False),
        sa.Column('phone', sa.String(45), nullable=False),
        sa.Column('email', sa.String(45), nullable=False),
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'contact_persons' in tables:
        op.drop_table('contact_persons')