'''
students = ["Harry","Hermonie","Ron"]
N =[0,1,2] 
for i in N:
    print(students[i])
'''
'''
#example 2
students = ["Harry","Hermonie","Ron"]
for student in students:  #The for loop starts and takes the first element of the students list, which is "Harry."
                          #It assigns "Harry" to the variable student for the first iteration.execute what is whitin & then it moves to the 2nd assignement
    print(student)
'''
'''
#len(takes the length of a list), Like len(students)=
#exampe3
students = ["Harry","Hermonie","Ron"]
for i in range(len(students)):
    print(i+1, students[i])
'''
students = {"Hermione":"Gryffindor",
             "Harry":"Gryffindor",
             "Draco":"Slytherin"}
for student in students:#so for assigns to student the keys like the 1st ittiration student = "Harry"
                        #students[key]=the key's value,like students["Draco"]="Slytherin"

    print(student+" in "+students[student])

print(students["Harry"])