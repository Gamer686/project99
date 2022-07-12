import os
import shutil

def main():
    deleted_folders_count = 0
    deleted_files_count = 0
    path = "Path_To_Delete"
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
     for root_folder, folders , files in os.walk(path):

        if seconds >= get_file_or_folder_age(root_folder):
            remove_folder(root_folder)
        deleted_folders_count += 1

        break

    else: 
        for folder in folders:
                folder_path = os.path.join(root_folder,folder)
                if seconds >= get_file_or_folder_age(file_path):
                    remove_file(file_path)
                deleted_files_count  += 1

        print(f"Total folders deleted: {deleted_folders_count}") 
        print(f"Total files deleted: {deleted_files_count}")

    def remove_folder(path): 
        if  not os.remove(path):
            print(f"(path) is removed succesfully") 

        else:
            print("Unable to delete the "+path)    

    def get_file_or_folder_age(path):
      ctime = os.stat(path).at_ctm
      return ctime

if __name__ == "__main__" :
    main() 