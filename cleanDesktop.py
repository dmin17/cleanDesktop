import os, shutil




def main():
    
    os.mkdir("Desktop/screenshots/")
    for file in os.listdir("Desktop"):
        if file.startswith("Screen"):
            shutil.move("Desktop/" + file, "Desktop/screenshots/")

       



if __name__ == "__main__":
    main()