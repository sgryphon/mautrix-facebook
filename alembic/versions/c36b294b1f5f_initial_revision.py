"""Initial revision

Revision ID: c36b294b1f5f
Revises: 
Create Date: 2019-05-01 02:37:15.915613

"""
from alembic import op
import sqlalchemy as sa
from mautrix.client.state_store.sqlalchemy import SerializableType
from mautrix.types import PowerLevelStateEventContent

# revision identifiers, used by Alembic.
revision = 'c36b294b1f5f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('mxid', sa.String(length=255), nullable=True),
    sa.Column('mx_room', sa.String(length=255), nullable=True),
    sa.Column('fbid', sa.String(length=127), nullable=False),
    sa.Column('index', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('fbid', 'index'),
    sa.UniqueConstraint('mxid', 'mx_room', name='_mx_id_room')
    )
    op.create_table('mx_room_state',
    sa.Column('room_id', sa.String(length=255), nullable=False),
    sa.Column('power_levels', SerializableType(PowerLevelStateEventContent), nullable=True),
    sa.PrimaryKeyConstraint('room_id')
    )
    op.create_table('mx_user_profile',
    sa.Column('room_id', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.String(length=255), nullable=False),
    sa.Column('membership', sa.Enum('JOIN', 'LEAVE', 'INVITE', 'BAN', 'KNOCK', name='membership'), nullable=False),
    sa.Column('displayname', sa.String(), nullable=True),
    sa.Column('avatar_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('room_id', 'user_id')
    )
    op.create_table('portal',
    sa.Column('fbid', sa.String(length=127), nullable=False),
    sa.Column('fb_receiver', sa.String(length=127), nullable=False),
    sa.Column('fb_type', sa.Enum('USER', 'GROUP', 'ROOM', 'PAGE', name='threadtype'), nullable=False),
    sa.Column('mxid', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('photo_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('fbid', 'fb_receiver'),
    sa.UniqueConstraint('mxid')
    )
    op.create_table('puppet',
    sa.Column('fbid', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('photo_id', sa.String(), nullable=True),
    sa.Column('matrix_registered', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.PrimaryKeyConstraint('fbid')
    )
    op.create_table('user',
    sa.Column('mxid', sa.String(length=255), nullable=False),
    sa.Column('session', sa.PickleType(), nullable=True),
    sa.Column('fbid', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('mxid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('puppet')
    op.drop_table('portal')
    op.drop_table('mx_user_profile')
    op.drop_table('mx_room_state')
    op.drop_table('message')
    # ### end Alembic commands ###
