import sys, os
import glob, pathlib
import subprocess
import shutil
import time
import re


def get_latest_subfolder(root_dir: str) -> str:
    """Get the latest subfolder in a directory.

    Args:
        root_dir (str): The root directory to search.

    Returns:
        str: The latest subfolder.

    Example:
        get_latest_subfolder('/home/username/Documents')
    """
    list_dirs = glob.glob(root_dir + '/*/')
    if not list_dirs:
        return None
    latest_dir = max(list_dirs, key=os.path.getmtime)
    return latest_dir

def get_latest_file(dir: str, regex='*') -> str:
    """Get the latest file in a directory.

    Args:
        dir (str): The directory to search.
        regex (str, optional): The regex to use. Defaults to '*' (all files).

    Returns:
        str: The latest file.

    Example:s
        get_latest_file('C:/Users/username/Desktop', '*.txt')
    """
    list_of_files = glob.glob(dir + '/' + regex)
    if not list_of_files:
        return None
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file



