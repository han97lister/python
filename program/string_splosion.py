def string_splosion( str ) :
    result = ""
    for char in range( len( str ) ) :
        result = result + str[: char + 1]
    return result