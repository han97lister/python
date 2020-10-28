class Student :

    def __init__( self, name, age ) :
        self.name = name
        self.age = age
        
    class_ = "student"
    
    #method containing 3 test scores and prints avg

    def test_score( self, score1, score2, score3 ) :
        
        total = score1 + score2 + score3
        avg = total / 3

        return avg

Hannah = Student( "Hannah", 23 )
print( Hannah.class_ )
print( Hannah.test_score( 87, 52, 60 ) )


