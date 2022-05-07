# def navttc(a,b='available'):
#     print(a,b)
# navttc(10,'laptop')

# def students(*entry_test):
#     print(entry_test)
#     sum=0
#     for n in entry_test:
#         sum=sum+n
#     print('Sum = ',sum)
# students(2,6,10,45,1,20)


# def students(**entry_test):
#     print(entry_test)
# students(name='munir',age=20,course='software')
# students(name=['munir','imran'], age=40, course=['sw','cs'])

# Task 1
# print('Task 1')
# def NTS (*entry_test):
#     print(entry_test)
# NTS('Munir','Ali','Karan','Sagar')
# print('')

#Task 2
# Make a function with unknown number of arguments pass in functions
# print('Task 2')
# def unknown(*a):
#     print(a)
#     sum=0
#     for n in a:
#         sum=sum+n
#     print('No of students admitted: ',sum)
# unknown(4,7,3,9)
# print('')

#Task 3
# Make a student management system which manages all the data of students like their 
# name,age,department and progress report
# print('Task 3')
# print('Student Management System')
# def student_management(**student):
#     print(student)
# student_management(name=['Munir','Imran','Karan','Sagar','Sahil'], age=[20,21,20,23,19], department=['SW','CS','ES','EL','CS'], progress=['good','very good','satisfactory','not satisfactory','Excellent'])
# print('')



def div(numb):
    print('Execution started: ')
    p = 0
    while numb >= 1000:
        p = int(numb/2)
        if numb<=1000:
            print(p)
    print('Execution stopped')

div(226991098841700000000000)
