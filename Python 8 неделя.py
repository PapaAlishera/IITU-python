# 1.1

a = input()
a_list = list(a.lower())
print(a_list)


# 1.2

a_list = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]

vow = ('a', 'e', 'i', 'o', 'u', 'y')
cons = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')

list_vow = []
list_cons = []
list_symb = []
	 
for char, count in a_list:
    if char in vow:
        list_vow.append((char, count))
    elif char in cons:
        list_cons.append((char, count))
    else:
        list_symb.append((char, count))

print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_sym =", list_symb)



# 2.1

stud_name = input()  

assignments = []
labs = []
tests = []
nez = 0
for i in range(0, 4):
    a = int(input())
    assignments.append(a)

for i in range(0, 2):
    l = float(input())
    labs.append(l) 
    
for i in range(0, 2):
    t = int(input())
    tests.append(t)  

student = {
    'name': stud_name,
    'assignment': assignments, 
    'lab': labs,
    'test': tests
}

print("student =", student)


# 2.2

stud_name = input()  

assignments = []
labs = []
tests = []
nez = 0
for i in range(0, 4):
    a = int(input())
    assignments.append(a)
    if a==0:
        nez = nez + 1

for i in range(0, 2):
    l = float(input())
    labs.append(l) 
    if l==0:
        nez = nez + 1
    
for i in range(0, 2):
    t = int(input())
    tests.append(t)  
    if t==0:
        nez = nez + 1

student = {
    'name': stud_name,
    'assignment': assignments,
    'lab': labs,
    'test': tests
}

obsh_done = 8 - nez

lab_check = {
    student['name']: obsh_done
}

print(lab_check)


# 2.3

stud_name = input()  

assignments = []
labs = []
tests = []
nez = 0
for i in range(0, 4):
    a = int(input())
    assignments.append(a)
    if a==0:
        nez = nez + 1

for i in range(0, 2):
    l = float(input())
    labs.append(l) 
    if l==0:
        nez = nez + 1
    
for i in range(0, 2):
    t = int(input())
    tests.append(t)  
    if t==0:
        nez = nez + 1

student = {
    'name': stud_name,
    'assignment': assignments,
    'lab': labs,
    'test': tests
}

obsh_done = 8 - nez

lab_check = {
    student['name']: obsh_done
}

print(lab_check)

if obsh_done >= 4:
    sred_assignment = sum(student['assignment']) / len(student['assignment']) 
    sred_lab = sum(student['lab']) / len(student['lab'])  
    sred_test = sum(student['test']) / len(student['test'])  
    final = (0.3 * sred_assignment) + (0.5 * sred_lab) + (0.2 * sred_test)  
else:
    final = 0  


student['final_grade'] = final

print("student =", student)


# 2.4 длинный динозаврский метод, но рабочий

stud_name = input()  

assignments = []
labs = []
tests = []
nez = 0
for i in range(0, 4):
    a = int(input())
    assignments.append(a)
    if a==0:
        nez = nez + 1

for i in range(0, 2):
    l = float(input())
    labs.append(l) 
    if l==0:
        nez = nez + 1
    
for i in range(0, 2):
    t = int(input())
    tests.append(t)  
    if t==0:
        nez = nez + 1

student = {
    'name': stud_name,
    'assignment': assignments,
    'lab': labs,
    'test': tests
}

obsh_done = 8 - nez

lab_check = {
    student['name']: obsh_done
}

print(lab_check)

if obsh_done >= 4:
    sred_assignment = sum(student['assignment']) / len(student['assignment']) 
    sred_lab = sum(student['lab']) / len(student['lab'])  
    sred_test = sum(student['test']) / len(student['test'])  
    final = (0.3 * sred_assignment) + (0.5 * sred_lab) + (0.2 * sred_test)  
else:
    final = 0  


student['final_grade'] = final

stud_name = input()  

assignments = []
labs = []
tests = []
nez = 0
for i in range(0, 4):
    a = int(input())
    assignments.append(a)
    if a==0:
        nez = nez + 1

for i in range(0, 2):
    l = float(input())
    labs.append(l) 
    if l==0:
        nez = nez + 1
    
for i in range(0, 2):
    t = int(input())
    tests.append(t)  
    if t==0:
        nez = nez + 1

student2 = {
    'name': stud_name,
    'assignment': assignments,
    'lab': labs,
    'test': tests
}

obsh_done = 8 - nez

lab_check = {
    student2['name']: obsh_done
}

print(lab_check)

if obsh_done >= 4:
    sred_assignment = sum(student2['assignment']) / len(student2['assignment']) 
    sred_lab = sum(student2['lab']) / len(student2['lab'])  
    sred_test = sum(student2['test']) / len(student2['test'])  
    final = (0.3 * sred_assignment) + (0.5 * sred_lab) + (0.2 * sred_test)  
else:
    final = 0  


student2['final_grade'] = final

students = {}

students[student['name']] = {
    'assignment': student['assignment'],
    'lab': student['lab'],
    'test': student['test'],
    'final_grade': student['final_grade']
}

students[student2['name']] = {
    'assignment': student2['assignment'],
    'lab': student2['lab'],
    'test': student2['test'],
    'final_grade': student2['final_grade']
}

print("студенты =", students)
