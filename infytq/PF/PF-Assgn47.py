#PF-Assgn-47
def encrypt_sentence(sentence):
    a_list = sentence.split(' ')
    b =[]
    for i in range(0,len(a_list)):
        if i %2!=0:
            v = '' #vowels
            c = '' #consonants
            for j in a_list[i]:
                if j in ['a','e','i','o','u']:
                    v+=j
                else:
                    c+=j
            cv = c+v
            a_list[i]=cv
        elif i %2==0:
            a_list[i]=a_list[i][::-1]
            
    sentence = ' '.join(a_list)
    return sentence       
                                  
            
sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
