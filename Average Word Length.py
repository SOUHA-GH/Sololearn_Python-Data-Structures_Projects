#Given a sentence as input,the program calculates and outputs the average word length of that sentence.
text = input()
n=text.split()
nw=len(n)
l=len(text)-text.count(" ")
print(l/nw)
