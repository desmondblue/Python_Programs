#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    s=''
    for i in patient_medical_speciality_list:
        if type(i) ==str:
            s+=i            
    
    #s = '-'.join(patient_medical_speciality_list)
    count_p = s.count('P')
    count_o = s.count('O')
    count_e = s.count('E')
    del(s)
    max_p = max(count_p,count_o,count_e)
    if count_o >count_p:
        if count_o>count_e:
            speciality =medical_speciality['O']
        else:
            speciality= medical_speciality['E']
    elif count_p>count_e:
        speciality =medical_speciality['P']
    else:
        speciality =medical_speciality['E']


    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
