"""create reviews table

Revision ID: 0001
Revises: 
Create Date: 2025-05-25

"""
from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('imdb_id', sa.String(length=20), nullable=False),
        sa.Column('user_opinion', sa.Text, nullable=False),
        sa.Column('user_rating', sa.Integer, nullable=False),
    )

def downgrade():
    op.drop_table('reviews')
