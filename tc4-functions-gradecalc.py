############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: 

# main() FUNCTION
def main():

    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

def courseInput (course):


        #Gather user inputs
        letterGrade = input(f"Please enter a letter grade for {course} : ").upper()
        modifier = input("Please enter a modifier (+, - or nothing) : ")
        
        # Determine base numeric value of the grade
        if letterGrade == "A":
             numericGrade = 4.0
        elif letterGrade == "B":
            numericGrade = 3.0
        elif letterGrade == "C":
            numericGrade = 2.0
        elif letterGrade == "D":
            numericGrade = 1.0
        elif letterGrade == "F":
            numericGrade = 0.0
        else:
                #If an invalid entry is made
            print("You entered an invalid letter grade.")
            
            # Determine whether to apply a modifier
        if modifier == "+":
            if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
                    numericGrade += 0.3
        elif modifier == "-":
            if letterGrade != "F":     # Minus is not valid on F
                    numericGrade -= 0.3
            return numericGrade
    # Output final message and result, with formatting
def classValue(course):
     numericGrade= courseInput
     print("The numeric value for {1} is : {0:.1f}".format (numericGrade,course))
     
       
#PROGRAM EXECUTION STARTS HERE
main()
courseInput("PROG1700")
print("")
courseInput("NETW1700")
print("")
courseInput("OSYS1200")
print("")
courseInput("WEBD1000")
print("")
courseInput("COMM1700")
print("")
courseInput("DBAS1007")
print("")

print("********************************************************")
print("")
print("")
classValue("PROG1700")
classValue("NETW1700")
classValue("OSYS1200")
classValue("WEBD1000")
classValue("COMM1700")
classValue("DBAS1007")