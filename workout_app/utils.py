from django.utils import timezone


def workout_update(request, day, WorkoutLog, ExerciseLog, WorkoutExercise):
    today = timezone.now().date()
    existing_log = WorkoutLog.objects.filter(
        user=request.user,
        workout_plan=day.plan,
        workout_day=day,
        date=today
    ).first()
    
    if existing_log:
        workout_log = existing_log
    else:
        # Create new workout log
        workout_log = WorkoutLog.objects.create(
            user=request.user,
            workout_plan=day.plan,
            workout_day=day,
            date=today
        )
        
        # Create exercise logs for each exercise in the workout day
        for exercise_item in WorkoutExercise.objects.filter(workout_day=day).order_by('order'):
            ExerciseLog.objects.create(
                workout_log=workout_log,
                exercise=exercise_item.exercise
            )
    return workout_log