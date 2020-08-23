import random
print("Welcome to Hangman\n ------------------")
words=['australia','canada','america','Mexico']
print('GUESS the word HINT!:a word about country')
randword=random.choice(words)
flag,cnt,count=[],0,0
cnt=len(randword)
print('_ '*len(randword))
for i in range(len(randword)):
    flag.append(0)
while (cnt!=count):
    letter=input('Enter the guess word:')
    if(len(letter)>1):
        print("Enter only a character")
        continue
    if(letter.isdigit()==1):
        print("digits are restricted\n enter only a charcter")
        continue
    for i in range(len(randword)):
        if(letter==randword[i]):
            flag[i]=1
            count=count+1
    for i in range(len(randword)):
        if(flag[i]==1):
            print(randword[i],end=' ')
        else:
            print('_',end=' ')    
    print()