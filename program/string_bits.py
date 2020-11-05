#return even characters of a string

def string_bits( str ) :
    result = ""
    for char in range( len(str) ) :
        if char % 2 == 0 :
            return result + str[ char ]
        return result