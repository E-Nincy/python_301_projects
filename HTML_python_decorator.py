def tagify(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # call the original function
            result = func(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator

@tagify("p")
def greet(name):
    return f"Hello, {name}"

@tagify("div")
def lorem():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

@tagify("h1")
def shout(text):
    return text.upper()

# Outputs
print(greet("Nincy"))       # Output: <p>Hello, Nincy</p>
print(lorem())              # Output: <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
print(shout("hi there"))    # Output: <h1>HI THERE</h1>