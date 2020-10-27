with open( "teams.txt" , "r" ) as file :
    outfile = ""

    for index in range( 5 ) :
        if index == 0 :
            outfile += "This is a new line \n "
            file.readline()
        else :
            outfile += file.readline()

with open( 'teams.txt', 'w' ) as file :
    file.write( outfile )

with open( "teams.txt" , "r" ) as reading_file :
    for index in range( 5 ) :
        print( reading_file.readline() )