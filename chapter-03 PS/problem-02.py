#Question-02:Write a program to fill in a letter template given below with name and date.

letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|'''

print(letter.replace("<|Name|>","Nitin").replace("<|Date|","19 July 2024"))