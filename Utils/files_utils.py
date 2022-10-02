import os
import shutil


def eval_directory(path,name_dir):
    try:
        p=os.path.join(path,name_dir)
        if not os.path.exists(p):
            os.mkdir(p)
            print("Directory " , p ,  " Created ")
        return p
    except FileExistsError:
        print("Directory " , p ,  " already exists")

def get_path_file_recient(path):
    files=os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    epath=[]
    for file in paths:
        if(file.endswith(".xlsx") or file.endswith(".xls")):
            epath.append(file)
    if len(epath)>0:
            return max(epath, key=os.path.getmtime)
    else:
        return None

def get_path_img_recient(path):
    files=os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    epath=[]
    for file in paths:
        if(file.endswith(".png") or file.endswith(".jpg")):
            epath.append(file)
    if len(epath)>0:
            return max(epath, key=os.path.getmtime)
    else:
        return None

def move_file(path_from,path_to,name_file):
    to=os.path.join(path_to,name_file)
    print(to)
    shutil.move(path_from,to)
    return to

def delete_directory(directory):
    print("delete ... ",directory)
    try:
        shutil.rmtree(directory)
        print("Success delete directory")
    except Exception as e:
        print("Directory " , directory ,  " not deleted ", e)
    return
