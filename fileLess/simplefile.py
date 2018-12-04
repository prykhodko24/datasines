import os.path
import os

answer=os.path.exists("C:\\")
answer_1=os.path.exists("C:/")
print(answer)

print(" \" ")


answer=os.path.isfile("number.txt")

print(" \" ")

answer=os.path.isdir("data")

print(answer )
file=open("data/names.txt")


data_in_file=file.read()  #прочитати даний файл

lines=file.readlines()#буде список , считаєм по рядкам , якщо попередньо е считування то буде порожній список , бо вказівник внизу


print(data_in_file)


file.close()#обов'язково закрити