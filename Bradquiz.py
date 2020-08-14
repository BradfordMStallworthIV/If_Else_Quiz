#By Bradford Stallworth

print('Hello, welcome to Brad trivia!')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1. Who is my favorite current Boxer? ')
    if ans.lower() == 'charlo':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')


    
    ans = input('2. What is my favorite color? ')
    if ans.lower() == 'blue':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')


   
    ans = input('3. Go to meal when I am hungry? ')
    if ans.lower() == 'chipotle':
        score += 1
        print('Correct!')
    else:
         print('Incorrect')
    

  
    ans = input ('4. Favorite Rapper?')
    if ans.lower() == 'jay z':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

print('Thank you for playing, You got' , score, 'questions correct.')
mark = (score/total_q) *100

print('Mark', str(mark)+ '%')
print('Goodbye')

