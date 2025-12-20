import time

def workout_logger(func):
    def wrapper(*args, **kwargs):
        print("Workout starting...")
        start_time = time.time()
        
        result = func(*args, **kwargs)
        
        end_time = time.time()
        duration = end_time - start_time
        print(f"Workout finished in {duration:.2f} seconds!")
        print("Great job! Keep pushing your limits")
        return result
    return wrapper


@workout_logger
def perform_workout(exercise, reps):
    for i in range(1, reps + 1):
        print(f"{exercise} rep {i}")
        time.sleep(0.2)
    return f"{reps} {exercise} reps completed!"


result = perform_workout("Push-up", 5)
print(result)
