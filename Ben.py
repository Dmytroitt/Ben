from random import choice
import os
print("==Ben 1.0==")
end = False
endquestion = ''
question = ''
say = ['yes','no','ho ho ho ho']
while end == False:
    question = str(input('Ask something for Ben: '))
    choice(say)
    endquestion = str(input('Continue?[Y/N]  ')).upper()
    if endquestion == 'N':
        end = True
    elif endquestion == 'Y':
        print('Ok!')
        os.system('clear') 
