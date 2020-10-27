#my attempt at this

name = str( input( "Please enter your name: "))
hw = int( input( "score / 25 : "))
assess = int( input( "score / 50 : "))
final = int( input( "score / 100 : "))

percentage = (( hw + assess + final ) / 175 ) * 100

def grade_calc( percentage ) :

    if percentage >= 80 :
        return "A"
    elif percentage >= 70 :
        return "B"
    elif percentage >= 60 :
        return "C"
    else :
        return "Fail"

ICT_grade = grade_calc( percentage )

print( name, percentage, ICT_grade )

#ben's workshop attempt

name = str( input( "Please enter your name: "))
hw = int( input( "score / 25 : "))
assess = int( input( "score / 50 : "))
final = int( input( "score / 100 : "))

def grade_calculator( hw, assess, final ) :
    
    if hw > 25 or assess > 50 or final > 100 :
        return "Invalid score entered"
    
    total = hw + assess + final
    grade = ( total / 175 ) * 100

    return grade

def grade_boundaries( percent_score ) :
    
    if percentage >= 80 :
        return "A"
    elif percentage >= 70 :
        return "B"
    elif percentage >= 60 :
        return "C"
    else :
        return "Fail"

grade = grade_calculator( hw, assess, final )
letter_grade = grade_boundaries( grade )

print( f"{ name } got { grade }% which is {letter_grade}") 