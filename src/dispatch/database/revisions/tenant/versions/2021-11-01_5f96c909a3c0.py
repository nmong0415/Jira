"""Adds an activity counter.

Revision ID: 5f96c909a3c0
Revises: ecabe49272c8
Create Date: 2021-11-01 15:41:14.853706

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "5f96c909a3c0"
down_revision = "ecabe49272c8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("participant", sa.Column("activity", sa.Integer(), nullable=True))
    # add some activity for backwards compatibility
    op.execute("update participant set activity = 1 where activity isnull")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("participant", "activity")
    # ### end Alembic commands ###
