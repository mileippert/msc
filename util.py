# utility functions
import os

# warning and section lines
from termcolor import colored, cprint
print_warn = lambda x: cprint(" {} ".format(x), 'red', 'on_white', attrs=['bold'])
horline = lambda: cprint(("_" * 120), 'white', 'on_grey', attrs=['bold'])

# function collects all images from direct subfolders provides lists with paths, labels and a mapping 
# not really recursive :)
def recursive_collect(folder, model_labels=None):
    directories = [os.path.join(folder, child) for child in os.listdir(folder)]
    paths = []
    labels = []
    label_start_index = 0
    if model_labels is None:
        label_name = dict()
    else:
        label_name = model_labels.copy()
        label_start_index = int(len(label_name)/10) + 19
    
    # iterate over all subfolders
    for directory, label in zip(directories, range(label_start_index, label_start_index + len(directories))):
        dir_name = directory.split(os.sep)[-1]

        # collect images in directory
        children = os.listdir(directory)
        paths.extend([os.path.join(directory, child) for child in children])
        
        # if directory is not in label mapping create new entry for directory
        if model_labels is not None:
            # look for associated index for this directory name
            index = None
            for element in label_name:
                if label_name[element][1] == dir_name:
                    index = element
                    break

            if index is not None:
                # class is known to model, use existing mapping (but refresh stats)
                labels.extend([index] * len(children))
                label_name[index] = (len(children), dir_name)
            else:
                # class is likely not known to model, create new index
                #labels.extend([int(label) + int(len(label_name)/10) + 19] * len(children))
                #label_name[label + int(len(label_name)/10) + 19] = (len(children), dir_name)
                labels.extend([int(label)] * len(children))
                label_name[label] = (len(children), dir_name)
        else:
            labels.extend([int(label)] * len(children))
            label_name[label] = (len(children), dir_name)

    return paths, labels, label_name
    
# shuffle = sorted(shuffle, key = lambda x: int(x[0].split("\\")[-1].split(".")[0]))