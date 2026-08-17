file_read = open('My_Shopping_List', 'r')
print("File in Read Mode :")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("File in Write Mode :")
file_write.write("This is my shopping list")
file_write.close()

file_append = open('My_Shopping_List', 'a')
file_append.write("\n File in append mode :")
file_append.write("This is my shopping list")
file_append.close()