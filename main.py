import shutil
import sys
import os


download_folder = os.path.expanduser("~/downloads")
zipped_files = os.path.expanduser("~/desktop/zipped")


if not os.path.exists(zipped_files):
    os.makedirs(zipped_files)

for file_name in os.listdir(download_folder):
    if file_name.endswith(".zip"):
        file_path = os.path.join(download_folder, file_name)
        # print(file_path)
        shutil.move(file_path,zipped_files)

print(f'finished, the file has been moved sucessfully to {zipped_files}')


# print(os.listdir(zipped_files))

# print(download_folder)
# print(zipped_files)
