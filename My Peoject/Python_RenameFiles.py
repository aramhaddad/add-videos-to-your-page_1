
import os
def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"F:\ATT_WORK_Folder\Training\NanoDegree_IntroductionToProgramming\Stage_3_project\FUFU")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"F:\ATT_WORK_Folder\Training\NanoDegree_IntroductionToProgramming\Stage_3_project\FUFU")
    # (2) for each file, rename filename
    for file_name in file_list:
        print("old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
rename_files()
