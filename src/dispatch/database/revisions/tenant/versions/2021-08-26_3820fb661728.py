"""Adding evergreen to other resources.

Revision ID: 3820fb661728
Revises: b73416df5744
Create Date: 2021-08-26 15:43:21.019477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3820fb661728"
down_revision = "b73416df5744"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("notification", sa.Column("evergreen", sa.Boolean(), nullable=True))
    op.add_column("notification", sa.Column("evergreen_owner", sa.String(), nullable=True))
    op.add_column(
        "notification", sa.Column("evergreen_reminder_interval", sa.Integer(), nullable=True)
    )
    op.add_column(
        "notification", sa.Column("evergreen_last_reminder_at", sa.DateTime(), nullable=True)
    )
    op.add_column("service", sa.Column("evergreen", sa.Boolean(), nullable=True))
    op.add_column("service", sa.Column("evergreen_owner", sa.String(), nullable=True))
    op.add_column("service", sa.Column("evergreen_reminder_interval", sa.Integer(), nullable=True))
    op.add_column("service", sa.Column("evergreen_last_reminder_at", sa.DateTime(), nullable=True))
    op.add_column("team_contact", sa.Column("evergreen", sa.Boolean(), nullable=True))
    op.add_column("team_contact", sa.Column("evergreen_owner", sa.String(), nullable=True))
    op.add_column(
        "team_contact", sa.Column("evergreen_reminder_interval", sa.Integer(), nullable=True)
    )
    op.add_column(
        "team_contact", sa.Column("evergreen_last_reminder_at", sa.DateTime(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("team_contact", "evergreen_last_reminder_at")
    op.drop_column("team_contact", "evergreen_reminder_interval")
    op.drop_column("team_contact", "evergreen_owner")
    op.drop_column("team_contact", "evergreen")
    op.drop_column("service", "evergreen_last_reminder_at")
    op.drop_column("service", "evergreen_reminder_interval")
    op.drop_column("service", "evergreen_owner")
    op.drop_column("service", "evergreen")
    op.drop_column("notification", "evergreen_last_reminder_at")
    op.drop_column("notification", "evergreen_reminder_interval")
    op.drop_column("notification", "evergreen_owner")
    op.drop_column("notification", "evergreen")
    # ### end Alembic commands ###
