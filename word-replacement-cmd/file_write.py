import os

def file_write(file_path, game_list):
    if os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(str(game_list))
            print("File content has been updated")
    else:
        with open(file_path, 'w') as file:
            file.write(str(game_list))
            print("File did not exists, was created")      