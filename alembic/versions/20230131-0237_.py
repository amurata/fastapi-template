"""empty message.

Revision ID: 6c689d530cbe
Revises:
Create Date: 2023-01-31 02:37:07.077007

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "6c689d530cbe"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tags",
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_tags_name"), "tags", ["name"], unique=True)
    op.create_table(
        "todos",
        sa.Column("title", sa.String(length=100), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_todos_title"), "todos", ["title"], unique=False)
    op.create_table(
        "users",
        sa.Column("full_name", sa.String(length=64), nullable=True),
        sa.Column("email", sa.String(length=200), nullable=False),
        sa.Column("email_verified", sa.Boolean(), server_default="0", nullable=False),
        sa.Column("hashed_password", sa.Text(), nullable=False),
        sa.Column("scopes", sa.Text(), nullable=True),
        sa.Column("id", sa.String(length=32), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_index(op.f("ix_users_full_name"), "users", ["full_name"], unique=False)
    op.create_table(
        "todos_tags",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("todo_id", sa.String(length=32), nullable=True),
        sa.Column("tag_id", sa.String(length=32), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
        ),
        sa.ForeignKeyConstraint(
            ["todo_id"],
            ["todos.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("todo_id", "tag_id", name="ix_todos_tags_todo_id_tag_id"),
    )
    op.create_index(
        op.f("ix_todos_tags_tag_id"), "todos_tags", ["tag_id"], unique=False,
    )
    op.create_index(
        op.f("ix_todos_tags_todo_id"), "todos_tags", ["todo_id"], unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_todos_tags_todo_id"), table_name="todos_tags")
    op.drop_index(op.f("ix_todos_tags_tag_id"), table_name="todos_tags")
    op.drop_table("todos_tags")
    op.drop_index(op.f("ix_users_full_name"), table_name="users")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("ix_todos_title"), table_name="todos")
    op.drop_table("todos")
    op.drop_index(op.f("ix_tags_name"), table_name="tags")
    op.drop_table("tags")
    # ### end Alembic commands ###
