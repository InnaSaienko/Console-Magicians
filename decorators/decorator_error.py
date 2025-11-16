from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Invalid input: {e}"
        except KeyError as e:
            return f"Contact or Note not found: {e}"
        except IndexError:
            return "Invalid command format. Please provide necessary arguments."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"        
    return inner