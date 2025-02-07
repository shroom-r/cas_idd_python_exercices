def debug2(function):
    def returnFun(*args, **kwargs):
        print(f"Calling {function} with args {args} and kwargs {kwargs}")
        result = function(*args, **kwargs)
        print(f'The result is {result}')
        return result
    return returnFun