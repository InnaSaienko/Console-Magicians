from functools import wraps


def validate_args(required: int, optional: int, error_msg: str):
    """Ensures expected numbers of arguments for parametrised handlers."""
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            cmd_args = args[0] if len(args) > 0 else kwargs.get("args")
            if cmd_args is not None:
                cmd_args_count = len(cmd_args)
                if cmd_args_count < required or cmd_args_count > required + optional:
                    raise ValueError(error_msg)
            return func(*args, **kwargs)

        return inner

    return decorator
