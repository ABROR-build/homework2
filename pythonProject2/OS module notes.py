import os

a = os.getcwd()  # prints the current working directory
print(a)
# result = C:\Users\abror\OneDrive\Desktop\
#          Новая папка\Projects\3-oy 3-dars\pythonProject2


os.chdir("C:/Users/abror/OneDrive/Desktop/Новая папка/Projects/3-oy 3-dars/pythonProject2")  # changes working directory
print(os.getcwd())
# reult = C:\Users\abror\OneDrive\Desktop

files1 = os.listdir(os.getcwd())  # lists all files in current working directory
print(files1)
# result = ['.idea', '.venv', '2014_us_cities.csv',
#           'OS module notes.py', 'Task-1.py', 'Task-2.py',
#           'Task-3.py', 'text.txt', 'Tic-tac-toe.py'
#           ]

files2 = os.listdir("C:/Users")  # lists all files in specific directory
print(files2)
# result = ['abror', 'All Users',
#           'Default', 'Default User',
#           'desktop.ini', 'Public'
#           ]

# os.mkdir("Hello")  # creates a directory witin currentt working directory
b = os.listdir(os.getcwd())
os.makedirs("Hello")
print(b)
# result = ['.idea', '.venv', '2014_us_cities.csv',
#           'Hello', 'OS module notes.py', 'Task-1.py',
#           'Task-2.py', 'Task-3.py', 'text.txt', 'Tic-tac-toe.py'
#           ]
#           ------ we can see that 'Hello' directory is created where current python is working ------

os.makedirs("Hello_bro/Bye_bro", exist_ok=True)  # creates directory inside one after other
# exist_ok=True - stands for not raising error when creating same folders
# result = Hello_bro -> Bye bro

os.rmdir("Hello")  # stands for removing directory -> REMOVED FILE IS NOT SAVED IN RECYCLE BIN

Cwd = os.getcwd()
file = 'hi.txt'
combined = os.path.join(Cwd, file)  # joins created file or folder with specific folder
print(combined)

print(os.path.exists(combined))

os.path.exists(file)  # checks whether given folder or filename exists

print(os.path.isfile('Task-3.py'))   # check whether given argument or name is file

print(os.path.isdir('Task-3.py'))   # check whether given argument or name is directory(folder)

print(os.stat('Task-3.py'))     # gives statistics about specific folder or file

print(os.stat('Task-3.py').st_size)     # returns size of specific file, Also you can choose lots of arguments after .

v1 = os.environ.get('PATH')     # gets the environment
print(v1)

print(os.getlogin())      # gets the name of the sytem user