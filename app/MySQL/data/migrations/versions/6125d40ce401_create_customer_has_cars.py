"""create customer_has_cars

Revision ID: 6125d40ce401
Revises: 20ca6b51f7e4
Create Date: 2020-11-16 14:25:48.271778

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '6125d40ce401'
down_revision = '20ca6b51f7e4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "customers_has_cars",
        sa.Column("CustomerId", sa.Integer, sa.ForeignKey("customers.id"), primary_key=True),
        sa.Column("CarId", sa.Integer, sa.ForeignKey("cars.id"), primary_key=True),
        sa.Column("license_number", sa.String(45)),
        sa.Column("color", sa.String(45))
    )


def downgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'customers_has_cars' in tables:
        op.drop_table('customers_has_cars')
