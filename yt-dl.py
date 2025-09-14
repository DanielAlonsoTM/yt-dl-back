import sys
import os.path
import subprocess
import re

# Script for download many videos from youtube using the lib youtube-dl with a file input

# This receive one argument from the command line, with script execution
path_file = sys.argv[1]


def get_total_urls():
    result = str(subprocess.check_output("cat " + path_file + " | wc -l", shell=True))
    # Remove special characters and letters from result
    result = re.sub('[^a-zA-Z0-9 \n\.]', '', result)
    result = re.sub('[bn]', '', result)
    return result


def download_video(url_video):
    cmd_command = 'youtube-dl -f mp4 -o "~/Videos/%(title)s.%(ext)s" ' + url_video
    try:
        os.system(cmd_command)
    except OSError as error:
        print(error)


if os.path.exists(path_file):

    print("Total url's in file: " + get_total_urls())

    file = open(path_file, 'r')
    array_urls = file.readlines()

    for url in array_urls:
        download_video(url)

else:
    print("File don't exists")
