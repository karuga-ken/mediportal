"""empty message

Revision ID: 621ad2ff4730
Revises: 
Create Date: 2024-04-14 20:31:40.022689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '621ad2ff4730'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('patientrecords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nationalno', sa.Integer(), nullable=True),
    sa.Column('hospital', sa.String(), nullable=True),
    sa.Column('DoctorName', sa.String(), nullable=True),
    sa.Column('date', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('nationalno', sa.Integer(), nullable=True),
    sa.Column('password', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nationalno')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients')
    op.drop_table('patientrecords')
    op.drop_table('doctors')
    # ### end Alembic commands ###