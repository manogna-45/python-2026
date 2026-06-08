diary = input("write your diary entry: ")
with open("diary.txt" , "a") as file:
    file.write("\n" + diary)
