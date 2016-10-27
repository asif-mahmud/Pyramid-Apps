"""DateTime Fix 2

Revision ID: fbe20baa174a
Revises: 
Create Date: 2016-10-27 06:24:25.223637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbe20baa174a'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('_password_hash', sa.Text(), nullable=False),
    sa.Column('roles', sa.ARRAY(sa.Text()), nullable=False),
    sa.Column('joined_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=True)
    op.create_table('galleries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_on', sa.DateTime(), server_default=sa.text('now()'), server_onupdate=sa.text('now()'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_galleries_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_galleries'))
    )
    op.create_index(op.f('ix_galleries_title'), 'galleries', ['title'], unique=False)
    op.create_table('profile_pictures',
    sa.Column('basename', sa.Text(), nullable=False),
    sa.Column('_available_sizes', sa.ARRAY(sa.Text()), nullable=False),
    sa.Column('image_type', sa.Text(), nullable=False),
    sa.Column('extension', sa.Text(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_profile_pictures_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_profile_pictures')),
    sa.UniqueConstraint('basename', name=op.f('uq_profile_pictures_basename'))
    )
    op.create_table('gallery_images',
    sa.Column('basename', sa.Text(), nullable=False),
    sa.Column('_available_sizes', sa.ARRAY(sa.Text()), nullable=False),
    sa.Column('image_type', sa.Text(), nullable=False),
    sa.Column('extension', sa.Text(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gallery_id', sa.Integer(), nullable=False),
    sa.Column('uploaded_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['gallery_id'], ['galleries.id'], name=op.f('fk_gallery_images_gallery_id_galleries')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_gallery_images')),
    sa.UniqueConstraint('basename', name=op.f('uq_gallery_images_basename'))
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gallery_images')
    op.drop_table('profile_pictures')
    op.drop_index(op.f('ix_galleries_title'), table_name='galleries')
    op.drop_table('galleries')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_table('users')
    ### end Alembic commands ###