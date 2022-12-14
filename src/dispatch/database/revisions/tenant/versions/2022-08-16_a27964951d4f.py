"""Adds a relationship between case types and oncall services

Revision ID: a27964951d4f
Revises: 33f35da7013b
Create Date: 2022-08-16 10:56:09.852403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a27964951d4f"
down_revision = "33f35da7013b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("case_type", sa.Column("oncall_service_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "case_type", "service", ["oncall_service_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "case_type", type_="foreignkey")
    op.drop_column("case_type", "oncall_service_id")
    # ### end Alembic commands ###
