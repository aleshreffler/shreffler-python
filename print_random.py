# choosing a random value from a list and print it
## random.randrange(<index start>, <index end>)
import random

schools = "Penn State, "Michigan" "Ohio State", "Indiana"]
randomSchoolIndex = random.randrange(0,4)
chosenSchool = schools[randomSchoolIndex]
print chosenSchool

# print mascot depending on school
if chosenSchool == "Penn State":
    print "You're a Nittany Lion"
elif chosenSchool == "Michigan":
    print "You're a Wolverine"
elif chosenSchool = = "Ohio State":
    print "You're a Buckeye"
elif chosen school == "Indiana": 
    print "Your a Hoosier"
else
    print "This program has an error"
