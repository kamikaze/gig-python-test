"""initial

Revision ID: f4eb64f96910
Revises: 
Create Date: 2020-10-27 22:01:11.634916+00:00

"""
import geoalchemy2
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4eb64f96910'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    schema_upgrades()
    data_upgrades()


def downgrade():
    data_downgrades()
    schema_downgrades()


def schema_upgrades():
    """schema upgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('img', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('DEAD', 'ALIVE', name='characterstatus'), nullable=True),
    sa.Column('nickname', sa.String(), nullable=True),
    sa.Column('occupation', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('appearance', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('portrayed', sa.String(), nullable=True),
    sa.Column('category', sa.ARRAY(sa.String()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('coordinates', geoalchemy2.types.Geography(geometry_type='POINT', srid=4326, from_text='ST_GeogFromText', name='geography'), nullable=True),
    sa.ForeignKeyConstraint(('character_id',), ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_index('uq_characters_name', 'characters', [sa.text('lower(name)')], unique=True,
                    postgresql_where=sa.text('deleted_at IS NULL'))
    op.create_index('uq_characters_nickname', 'characters', [sa.text('lower(nickname)')], unique=True,
                    postgresql_where=sa.text('deleted_at IS NULL'))
    # ### end Alembic commands ###


def schema_downgrades():
    """schema downgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('uq_characters_name', table_name='characters')
    op.drop_index('uq_characters_nickname', table_name='characters')
    op.drop_table('locations')
    op.drop_table('characters')
    # ### end Alembic commands ###


def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass


def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass

