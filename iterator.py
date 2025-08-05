def my_generator():
    for i in range(5):
        yield i

for i in my_generator():
    print(i)


def outer():
    message = "Hello from Shorya"

    def inner():
        print(message)
    return inner

my_function = outer()
my_function()   