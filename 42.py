def outer():
    def inner():
        return "Hello from inner function"
    return inner
result=outer()
print(result())