"""Initial migration

Revision ID: 0b255c4b6915
Revises: 
Create Date: 2020-03-27 01:34:43.567341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b255c4b6915'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ct_ranges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('min_value', sa.Integer(), nullable=True),
    sa.Column('max_value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('languages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('has_articles', sa.Boolean(), nullable=True),
    sa.Column('mrph_alignment', sa.String(length=50), nullable=True),
    sa.Column('dominant_order', sa.String(length=50), nullable=True),
    sa.Column('writing_system', sa.String(length=50), nullable=True),
    sa.Column('genders', sa.Integer(), nullable=True),
    sa.Column('cases', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('language_categories',
    sa.Column('language_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['ct_ranges.id'], ),
    sa.ForeignKeyConstraint(['language_id'], ['languages.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('language_categories')
    op.drop_table('languages')
    op.drop_table('ct_ranges')
    # ### end Alembic commands ###