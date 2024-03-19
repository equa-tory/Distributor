import os
import shutil
import time

source = os.path.join('/home/sasha/Downloads')
sort = os.path.join('/home/sasha/Pictures')

def main():
    while True:
        for f in os.listdir(source):
            if f.endswith((".png",".jpg",".jpeg")):
                print(f"Moving {os.path.join(source, f)} to {sort   }")
                shutil.move(os.path.join(source, f), sort)
        time.sleep(5)

if __name__ == '__main__':
    main()
