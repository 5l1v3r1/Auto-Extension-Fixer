import magic
import sys
import os


try:
    file_magic = magic.Magic(magic_file=sys.argv[1])
    dic=sys.argv[2]
except:
    print("Usage: auto_extension_fixer.py [magic numbers file] [destination folder] ")
    exit()


def filetype(file):
    file_header=file_magic.from_file(dic+"//"+f)
    if file_header.find("JPEG") != -1:
        return ".jpg"
    if file_header.find("PNG") != -1:
        return ".png"
    if file_header.find("PDF") != -1:
        return ".pdf"
    if file_header.find("MP4") != -1:
        return ".mp4"
    if file_header.find("GIF") != -1:
        return ".gif"
    if file_header.find("MOV") != -1:
        return ".mov"
    print("Not Found tag:",file_header)
    return ""

files = os.listdir(dic)
for f in files:
    file_path=dic+"//"+f;file_name=f.split(".")[0] # index.html -> index
    try:
        os.rename(dic+"//"+f, dic + "//"+file_name+filetype(file_path))
    except:
        print("Cannot rename file:",file_path)