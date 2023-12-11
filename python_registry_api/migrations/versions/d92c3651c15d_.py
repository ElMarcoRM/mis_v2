"""empty message

Revision ID: d92c3651c15d
Revises: 2ec5fa7141ed
Create Date: 2023-02-21 14:50:39.543105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d92c3651c15d"
down_revision = "2ec5fa7141ed"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "shareholder",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("parent_reg_code", sa.String(length=7), nullable=True),
        sa.Column("reg_code", sa.String(length=11), nullable=True),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("share_amount", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent_reg_code"],
            ["company.reg_code"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("shareholder")
    # ### end Alembic commands ###
