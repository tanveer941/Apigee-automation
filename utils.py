import zipfile
import os
import shutil

def extract_zipfile(path_to_zip_file):
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        directory_to_extract_to = os.path.dirname(path_to_zip_file)
        fl_name = os.path.basename(path_to_zip_file)
        folder_to_extract = os.path.splitext(fl_name)[0]
        directory_to_extract_to = os.path.join(directory_to_extract_to, folder_to_extract)
        if os.path.exists(directory_to_extract_to):
            print("Overwriting an existing proxy data: ", directory_to_extract_to)
            shutil.rmtree(directory_to_extract_to)
        zip_ref.extractall(directory_to_extract_to)

def zip_folder(path_to_zip_folder):
    # delete the zip file for this folder if it already exists

    zip_file_name = '{}.zip'.format(path_to_zip_folder)
    if os.path.isfile(zip_file_name):
        os.remove(zip_file_name)
    zipf = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
    zipdir(path_to_zip_folder, zipf)
    zipf.close()

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), arcname=os.path.join(root[len(path):], file))