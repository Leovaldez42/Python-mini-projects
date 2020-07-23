import os       # can be installed by pip install os if error is showed

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        
def move(folder_name, files):
    for file in files:
        os.replace(file, f"{folder_name}/{file}")

if __name__ == "__main__":
    
    files = os.listdir()
    files.remove("main.py")

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist("Others")

    imgExt = [".png", '.jpg', '.jpeg']
    images = [file for file in files if os.path.splitext(file)[1].lower in imgExt]

    docExts = [".txt", ".docs", ".doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1] in docExts]

    mediaExts = [".mp4", ".mp3", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1] in mediaExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExt) and os.path.isFile(file):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Others", others)
