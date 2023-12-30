import os
import subprocess
import platform
import sys
from time import sleep
from send2trash import send2trash

import features.backstrings as backs
from features import imaging


# Plays and act on the files
def player(target_dir: str, target_file: str, total: int, current_file_num: int) -> int:
    """
    Play a file and act on it

    Args:
        target_dir (str): Directory in which the file is contained. Used to build full path
        target_file (str): Filename of the file. Used to build full path
        total (int): The total number of files to review. Used to display the header
        current_file_num (int): The index of the current file. Used to display the header

    Returns:
        int: The size of the file in KB. If the file is skipped, returns -1
    """
    while True:
        backs.syscall(backs.TerminalCalls.CLEAR)
        if not os.path.exists(target_dir + "/" + target_file):
            print(backs.texter("filemiss") + target_file)
            sleep(1)
            return -1
        print("Playing: " + target_file + " ||", current_file_num, "/", total)
        program = "vlc"
        if platform.system() == "Darwin":
            program = "/Applications/VLC.app/Contents/MacOS/VLC"
        command = (
            program
            + " --quiet"
            + " --sout-all"
            + " --sout"
            + ' "#display"'
            + ' "'
            + target_dir
            + "/"
            + target_file
            + '"'
        )  # Running VLC with the file and all audio channels
        subprocess.run(command, shell=True, check=True)
        print("What would you like to do with this file?")
        match (input("(D)elete | (S)kip | (R)eplay | (Q)uit\n").lower()):
            case "d":
                print("Deleted: " + target_file)
                size_k = (os.stat(target_dir + "/" + target_file).st_size) / 1024
                if platform.system() in ("Linux", "Darwin"):
                    send2trash(target_dir + "/" + target_file)
                else:
                    send2trash(target_dir + "\\" + target_file)
                sleep(1)
                return size_k
            case "s":
                print("Skipped: " + target_file)
                sleep(1)
                return -1
            case "r":
                print("Replaying: " + target_file)
                sleep(1)
            case "q":
                print("Ok, sys.exitting...")
                sleep(1)
                sys.exit()
            case _:
                print(backs.texter("unkerr"))
                sleep(1)


def player_call(
    video_files: list[str],
    target_dir: str,
    total: int,
    starting_file_idx: int,
    nuked: int,
    skipped: int,
    total_k_deleted: int,
):
    """
    Runs the player through all the files and deals with statistics

    Args:
        video_files (list[str]): List of video file names
        target_dir (str): Video directory path
        total (int): Total number of files in the dir
        starting_file_idx (int): The index of the first video file from the total count
        nuked (int): Number of files deleted
        skipped (int): Number of files skipped
        total_k_deleted (int): Total number of KBs deleted
    """
    # Calling player, while passing display values loaded from file (if they exist)
    for item in video_files:
        starting_file_idx += 1
        del_file_size = player(target_dir, item, total, starting_file_idx)
        if del_file_size == -1:
            skipped += 1
            with open(target_dir + "/temp.list", "a", encoding="utf-8") as filehandle:
                filehandle.write(item + "\n")
        else:
            nuked += 1
            total_k_deleted += del_file_size

        with open(target_dir + "/temp.stat", "w", encoding="utf-8") as filehandle:
            filehandle.write(
                str(total)
                + "\n"
                + str(nuked)
                + "\n"
                + str(skipped)
                + "\n"
                + str(total_k_deleted)
                + "\n"
                + str(starting_file_idx)
            )

    backs.syscall(backs.TerminalCalls.CLEAR)
    # Cleaning up temps and converting data values
    try:
        os.remove(target_dir + "/temp.list")
    except FileNotFoundError:
        pass
    try:
        os.remove(target_dir + "/temp.stat")
    except FileNotFoundError:
        pass

    imaging.imager(backs.search_dir(target_dir), target_dir)
    backs.display_stats(total_k_deleted, total, nuked, skipped)

    backs.syscall(backs.TerminalCalls.PAUSE)
