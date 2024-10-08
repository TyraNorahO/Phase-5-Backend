"""updates models

Revision ID: 40e152bd0c4a
Revises: c5176c0f5e49
Create Date: 2024-07-30 12:58:05.958542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40e152bd0c4a'
down_revision = 'c5176c0f5e49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workout_plans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('coach_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('workout_days', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['coach_id'], ['coaches.id'], name=op.f('fk_workout_plans_coach_id_coaches')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('target_date', sa.Date(), nullable=False),
    sa.Column('achieved', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_goals_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nutrition_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('meal_type', sa.Enum('BREAKFAST', 'LUNCH', 'DINNER', 'SNACK', name='mealtype'), nullable=False),
    sa.Column('calory_intake', sa.Integer(), nullable=False),
    sa.Column('carbs', sa.Integer(), nullable=False),
    sa.Column('notes', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_nutrition_logs_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('progress_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('body_fat_percentage', sa.Integer(), nullable=False),
    sa.Column('muscle_mass', sa.Integer(), nullable=False),
    sa.Column('notes', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_progress_logs_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('workout_plan_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('day_of_week', sa.String(length=20), nullable=False),
    sa.Column('exercises', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_workouts_user_id_users')),
    sa.ForeignKeyConstraint(['workout_plan_id'], ['workout_plans.id'], name=op.f('fk_workouts_workout_plan_id_workout_plans')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('workout_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('sets', sa.Integer(), nullable=False),
    sa.Column('reps', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['workout_id'], ['workouts.id'], name=op.f('fk_exercises_workout_id_workouts')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exercises')
    op.drop_table('workouts')
    op.drop_table('progress_logs')
    op.drop_table('nutrition_logs')
    op.drop_table('goals')
    op.drop_table('workout_plans')
    # ### end Alembic commands ###
