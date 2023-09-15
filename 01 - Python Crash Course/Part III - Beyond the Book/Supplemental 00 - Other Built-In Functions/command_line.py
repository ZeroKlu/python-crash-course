import sys

script_name = sys.argv[0].split("\\")[-1].split("/")[-1]
print(f"I am running {script_name}")

print("My command line arguments are")

for i in range(1, len(sys.argv)):
    print(f" - {sys.argv[i]}")

# Execute using this command:
#   python <<path_to_script>> arg_1 arg_2 ... arg_n
