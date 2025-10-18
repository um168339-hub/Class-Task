sentence = input("Enter you sentence :")
print(sentence)
print(sentence.__len__())
print(sentence.upper())
print(sentence[0])
print(sentence[-1])

# Part No.2
name = input("Enter any name :\n")
place = input("Enter any place :\n")
object = input("Enter any object :\n")
feeling = input("Enter any feeling:\n")
print("The student name is ", name,"he is from " ,place," ,object,and his is fav subject ",object,"he is so ",feeling,)

#  Part No.3
def Vowels_Word(text):
    return text
word = input("Enter your word:")
reversed = word [::-1]
print(word.title())
print(reversed)
print(word.replace("a","*"))
print(word.replace("e","*"))
print(word.replace("i","*"))
print(word.replace("o","*"))
print(word.replace("u","*"))