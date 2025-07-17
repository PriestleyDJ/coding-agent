from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

# File info
print("Results for current directory:")
print(get_files_info("calculator", "."))

print("Results for 'pkg' directory:")
print(get_files_info("calculator", "pkg"))

print("Results for '/bin' directory:")
print(get_files_info("calculator", "/bin"))

print("Results for '../' directory:")
print(get_files_info("calculator", "../"))

# File content
print("Results for 'lorem.txt' file:")
print(get_file_content("calculator", "lorem.txt"))

print("Results for 'main.py' file:")
print(get_file_content("calculator", "main.py"))

print("Results for 'pkg/calculator.py' file:")
print(get_file_content("calculator", "pkg/calculator.py"))

print("Results for '/bin/cat' file:")
print(get_file_content("calculator", "/bin/cat"))

print("Results for 'pkg/does_not_exist.py' file:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))

# Write files
print("Results for writing to 'lorem.txt'")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("Results for writing to 'pkg/morelorem.txt'")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print("Results for writing to '/tmp/temp.txt'")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

# Run python files
print("Results for running 'main.py'")
print(run_python_file("calculator", "main.py"))

print("Results for running 'main.py' with 3 + 5")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("Results for running 'tests.py'")
print(run_python_file("calculator", "tests.py"))

print("Results for running '../main.py'")
print(run_python_file("calculator", "../main.py"))

print("Results for running 'nonexistent.py'")
print(run_python_file("calculator", "nonexistent.py"))
