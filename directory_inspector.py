import os

def list_directory_contents(path):
    try:
        contents = os.listdir(path)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Invalid directory. Please check the path.")
    except PermissionError:
        print("Access denied. You don't have permission to view this directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

directory_path = input("Enter the directory path: ")

list_directory_contents(directory_path)
