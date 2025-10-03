"""Import the requirement"""
from functools import wraps

def log_action(func):
    """MAKE A class"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper
