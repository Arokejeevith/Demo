"""In a betting game involving the roll of a dice, Sandeep gains Rs.X if an odd number turns up
and he loses Rs.Y is an even number turns up. The numbers shown on the face of the dice in a 
certain number of games is passed as input. The values of X and Y are also passed as input. 
The program must print the net gain or loss as the output. 

Input Format: 
First line will contain the numbers shown on the face of the dice separated by one or more spaces. 
Second line will contain the value of X 
Third line will contain the value of Y 

Output Format: The net gain or loss (loss will be a negative value) 

Sample Input/Output: 
Example 1: 
Input: 1 4 3 10 30 
Output: -10 
Explanation: He gains 20 rupees for 1 and 3 and loses 30 rupees for 4. Hence there is a net loss of 20-30 = -10 
Example 2: 
Input: 4 6 1 2 1 50 25 
Output: 25 He gains 100 rupees for 1,1 and loses 75 rupees for 4,6,2. 
Hence there is a net gain of 100-75 = 25"""

string=input() 
x=int(input()) 
y=int(input()) 
lis=string.strip().split() 
cash=0 
for i in range(len(lis)): 
  if int(lis[i])%2==0: cash-=y 
  else: cash+=x
print(cash)
