#numbers=[]
#unique_numbers=[]
#for i in range(10):
  #  answer=int(input('enter a number:'))
 #   numbers.append(answer)
#for number in numbers:
  #  if number not in unique_numbers:
 #      unique_numbers.append(number) 
          
#print('original list:', numbers)
#print('list without duplicates:', unique_numbers)  


 
secret=30
answer=float(input('enter a number:')) 
while answer != secret:
      answer= float(input('wrong answer, try again:'))  
print('bingo! you found the secret number.')      
    