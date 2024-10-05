# file handling operations such as
# opening a file
# reading from file
# adding or updating contents in a file
# closing the file after use to free system resources

my_cv = open("./cv.txt", "r")
full_content = my_cv.read()
single_line = my_cv.readline()
all_content_as_a_list = my_cv.readlines()
print(all_content_as_a_list)
my_cv.close()



