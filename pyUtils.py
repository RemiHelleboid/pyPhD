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


def animate_3d_camera_rotation(X, Y, Z):
    import matplotlib.pyplot as plt
    from matplotlib import animation
    from mpl_toolkits.mplot3d import Axes3D


    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.grid(False)

    scat = ax.scatter(X, Y, Z,  s=2, marker='.', alpha=0.65, edgecolors='k', linewidths=0.1)
    fig.tight_layout()

    def init():
        ax.view_init(elev=10., azim=0)
        return [scat]

    def animate(i):
        print(f"\rFrame {i} / {360}", end='', flush=True)
        angle = i 
        ax.view_init(elev=10., azim=i)
        return [scat]

    # Animate
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                frames=int(360), interval=20, blit=True)

    # Save
    anim.save('rotation_basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'], dpi=300)


