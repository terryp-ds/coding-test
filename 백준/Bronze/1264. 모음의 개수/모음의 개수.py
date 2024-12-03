while 1:
 s=input()
 if s=='#':break
 print(len([x for x in list(s.lower()) if x in 'aeiou']))