import os
import shutil
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

showname = simpledialog.askstring(title="Bot", prompt="Show Name:")
season = simpledialog.askstring(title="Bot", prompt="Season Number:")

def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.


dirname = os.path.dirname(__file__)
file_input = dirname.removesuffix('\\Common')+'\In'
filename = dirname+'\PyIn'
destination = dirname+'\Renamed'

shutil.copytree(file_input, filename, dirs_exist_ok=True)

full_file_paths = get_filepaths(filename)
print(full_file_paths)
length = len(full_file_paths)

destinations = []
start = 'HandBrakeCLI --preset-import-file preset.json -Z NVEnc -i '

for i in range(length):
    file = full_file_paths[i]
    temp, extension = os.path.splitext(file)
    episode = ''
    if i<10:
        episode = '0'+str(i+1)
    else:
        episode = ''+str(i+1)

    fulltitle = showname+' - s'+season+'e'+str(episode)+extension
    name = destination+'/'+fulltitle
    destinations.append(name)
    print(name)
    os.rename(file,name)

for c in range(length):
    current = destinations[c]

    new = current.replace('Renamed','Out')
    fname, ext = os.path.splitext(new)
    new = fname.replace('\\Common','')+'.m4v'

    full = start+'\"'+current+'\" -o \"'+new+'\"'
    full = full.replace('/','\\')
    print(full)
    os.system(full)
    os.remove(current)
