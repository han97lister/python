def upper_decorator( func ) :

    def function_wrapper( string_1 ) :
        return string_1.upper()
    return function_wrapper

@upper_decorator
def hello( string_1 ) :
    return string_1

print( hello( "decorator is here" ))