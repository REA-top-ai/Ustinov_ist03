def identity_decorator(func):
    return func


@identity_decorator
def welcome_message():
    return 'greetings'


def lowercase_decorator(func):
    def wrapper():
        result = func()
        return result.lower()

    return wrapper


@lowercase_decorator
def send_signal():
    return 'ALERT'


def add_prefix(func):
    def wrapper():
        return '>> ' + func()

    return wrapper


def add_suffix(func):
    def wrapper():
        return func() + ' <<'

    return wrapper


@add_prefix
@add_suffix
def get_title():
    return 'Report'


def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f'Log: calling {func.__name__}()',
              f'with {args} and {kwargs}')

        result = func(*args, **kwargs)

        print(f'Log: {func.__name__}()',
              f'returned {result}')

        return result

    return wrapper


@log_execution
def handle_request(user_id, action):
    return f'User {user_id} did {action}'