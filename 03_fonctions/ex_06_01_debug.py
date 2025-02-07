def debug(function, *args, **kwargs):
    print(f"Calling {function} with args {args} and kwargs {kwargs}")
    result = function(*args, **kwargs)
    print(f'The result is {result}')
    return result