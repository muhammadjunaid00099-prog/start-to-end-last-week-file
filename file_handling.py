...
f= open("demo",'w')
text= f.write("this is write file")
print(text)
f.close()
...

f= open("dumy.txt",'w')
for i in range(100):
    f.write(f"This is line2{i+1}")
    #print(text)
f.close()

f= open("dumy",'r')
text= f.read()
f.close()
