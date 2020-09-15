f=open('kku.txt', encoding='utf-8')  
f1=open('kku2.txt','a', encoding='utf-8')

for x in f.read():
    f1.write(x)

f1.write("Motto: วิทยา จริยา ปัญญา\n")
f1.write("Motto in English: Knowledge, Virtues, Wisdom")

f.close()
f1.close()

with open('kku2.txt','r', encoding='utf-8') as file:
    print(file.read())
