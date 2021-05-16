__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
from zipfile import ZipFile

cache_dir = './cache'
zip_file_path = './data.zip'
search_string = 'password: ' 

def main():
    clean_cache()
    cache_zip(zip_file_path, cache_dir)
    files = cached_files()
    password = find_password(files)
    print(password)

def clean_cache():
    if os.path.exists(cache_dir):
        for filename in os.listdir(cache_dir):
            filepath = os.path.join(cache_dir, filename)
            os.unlink(filepath)
    else :
        os.mkdir(cache_dir)
    

def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, 'r') as zipObj:
        zipObj.extractall(cache_dir_path)

def cached_files():
    if os.path.exists(cache_dir):
        filelist = []
        for filename in os.listdir(cache_dir):
            filepath = os.path.join(cache_dir, filename)
            filelist.append(os.path.abspath(filepath))
        return filelist

def find_password(filelist):
    for filepath in filelist:
        file = open(filepath, 'r')
        text = file.read()
        lines = text.splitlines()
        for line in lines:
            if (line.find(search_string) > -1):
                return line.replace(search_string, "")
    return "'" + search_string + "' not found..."



if __name__ == '__main__':
    main()
