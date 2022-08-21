#This is a program to analyze text.
#outputs the frequency of a letter in a text in percentage
txt=str(input())
l=str(input())
print((txt.count(l)*100)//len(txt))
