# LEGB

# Local
# Enclosing
# Global
# Built In

# Global
x = 'Global x'

def outer():
    print(x)
    
outer()

# Local
def outer(z):
    print(z)
    
outer('local z')
print(z)

# Local y Global
x = 'Global x'

def outer():
    x = 'Local x'
    print(x)
    
x = 'Global x2'
outer()


# Built In
def outer(z):
    print(min(z))
    
outer([1,2,3,4,5])
############
import builtins
print(dir(builtins))

def min(iterable):
    return None

def outer(z):
    print(min(z))
    
outer([1,2,3,4,5])

# Local, Enclosing
def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

# Local, Global
x = 'Global x'
def outer():
    x = 'outer x'

    def inner():
        global x
        print(x)

    inner()
    print(x)

outer()


# Local, Enclosing, Global
x = 'Global x'

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)