string = input('Write your list of words: ')
string = string.split()
print(max(string, key=len))
