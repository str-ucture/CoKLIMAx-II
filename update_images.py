import os
import shutil

def copy_images(source_root_dir, target_root_dir):
    for dirpath, dirnames, filenames in os.walk(source_root_dir):
        if "images" in dirnames:
            # Read source dir
            source_images_dirpath = os.path.join(dirpath, "images")
            print(source_images_dirpath)

            # Define target dir
            dir_seq = source_images_dirpath.split(os.sep)
            target_image_dirpath = os.path.join(target_root_dir, dir_seq[1], dir_seq[2], dir_seq[3])
            
            # Copy entire dir it target doesnt exist
            try:
                print("Copying the images folder...")
                shutil.copytree(source_images_dirpath, target_image_dirpath)
            except FileExistsError:
                print(f"The directory {target_image_dirpath} already exists")
            except Exception as e:
                print(f"An error occurred: {e}")
            print()

copy_images(source_root_dir = "./source_en", target_root_dir="./docs")
copy_images(source_root_dir = "./source_en",target_root_dir="./docs/en")
copy_images(source_root_dir = "./source_de",target_root_dir="./docs/de")