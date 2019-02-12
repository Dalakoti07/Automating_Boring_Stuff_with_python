import re
'''
#
8 characters length 10%
2 letters in Upper Case 10%
1 Special Character (!@#$&*) 50%
2 numerals (0-9) 10%
3 letters in Lower Case 20%
'''

password=input()

#this function takes list as input and maximum expected and weightage toward the password strength 
def get_score(list_custom,max_ac,weightage):
    a=1
    score=0.0
    if(len(list_custom)>=max_ac):
        score=(len(list_custom))/max_ac
    else:
        score=a*((len(list_custom))/max_ac)
    return min(weightage*100,score*weightage*100)

# calculate the score on the basis of the length of the password
score_1=get_score(list(password),8,.10)

list_all_caps=re.findall('[A-Z]+',password)
score_2=get_score(list_all_caps,2,.10)
list_special=re.findall('[!@#$&*]',password)
score_3=get_score(list_special,1,.50)

#calculate numerals in the password
list_numeral=re.findall('[0-9]',password)
score_4=get_score(list_numeral,2,.10)

list_lower_case=re.findall('[a-z]',password)
score_5=get_score(list_lower_case,3,.20)

score=score_1+score_2+score_3+score_4+score_5
print('strength is ',score)
if(score<20):
	print('Try again password is too weak ')
elif(score>=20 and score<40):
	print('It is weak ')
elif(score>=40 and score<60):
	print('It is Acceptable ')
elif(score>=60 and score<=90):
	print('It is Good ')
else:
	print('It is Great ')