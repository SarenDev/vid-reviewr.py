import os
import sys
from datetime import datetime
from time import sleep

import features.backstrings as backs


def imager(video_list: list[str], target_dir: str):
    """
    Create an image of all video files in a directory

    Args:
        video_list (list[str]): List of all video file names
        target_dir (str): Directory path in which to save the image
    """
    print("----------\n")
    target_image = (
        target_dir + "/Full_Image-" + str(datetime.date(datetime.now())) + ".list"
    )
    if os.path.exists(target_image):
        print("It looks like you already created an image today.")
        if input("Would you like to overwrite it? y/N\n").lower() != "y":
            print("Ok, not overwriting anything...\n")
            return
    with open(target_image, "w", encoding="utf-8") as filehandle:
        for item in video_list:
            filehandle.write(item + "\n")
    print(
        "We wrote an image (directory snapshot) into the file: " + target_image + "\n"
    )


# Reads an image
def reader(
    target_dir: str, video_files: list[str], temp_stat: bool
) -> tuple[list[str], list[str], int, int, int, int, int]:
    """
    _summary_

    Args:
        target_dir (str): Video directory path
        video_files (list[str]): List of video files in the dir
        temp_stat (bool): Load temporary stats

    Returns:
        tuple[list[str], list[str], int, int, int, int, int]: new_files, old_files, total, nuked, skipped, size_k, starting_file_idx
    """
    new_files = []
    old_files = []
    total = nuked = skipped = size_k = starting_file_idx = 0
    target_dir_len = len(video_files)

    if not os.path.exists(target_dir):
        print(backs.texter("filemiss") + target_dir + "\n")
        backs.syscall(backs.TerminalCalls.PAUSE)
        if temp_stat:
            return (None, None, 0, 0, 0, 0, 0)
        return (None, None, 0, 0, 0, 0, 0)

    with open(
        target_dir, "r", encoding="utf-8"
    ) as filehandle:  # Read the selected file into list
        old_files = filehandle.read().splitlines()

    # Compare and create new list of files not in the image
    # Also used to perform an integrity check using the number of matches
    for item in video_files:
        if item in old_files:
            target_dir_len -= 1
        else:
            new_files.append(item)

    if temp_stat:  # Read stat file
        path_stat = target_dir[:-4] + "stat"
        if not os.path.exists(path_stat):
            print("We couldn't find a stat file, so we'll ignore it...")
            total = nuked = skipped = size_k = 0
            temp_stat = False
        else:
            with open(path_stat, "r", encoding="utf-8") as filehandle:
                line = filehandle.read().splitlines()
                total = int(line[0])
                nuked = int(line[1])
                skipped = int(line[2])
                size_k = float(line[3])
                starting_file_idx = int(line[4])

    print("Image read!\n\n")

    # Image integrity check by seeing if any files matched the image
    if target_dir_len == len(video_files):
        if target_dir.endswith("temp.list"):
            print("----------\n")
            print(
                "This is bad, the autosave image we made failed our integrity check\n"
            )
            print("We'll clean up and restart\n")
            backs.syscall(backs.TerminalCalls.PAUSE)
            os.remove(target_dir)
            try:
                os.remove(target_dir[:-4] + "stat")
            except FileNotFoundError:
                pass
            return (None, None, 0, 0, 0, 0, 0)

        print("----------\n")
        print("This is bad... The image you loaded failed our integrity check")
        print(
            "It could be the file you're using is unbelievably old, came from another directory, or is corrupted"
        )
        print("Are you sure you want to continue with this image file? y/N")
        print("If you do - you might have to go through some files again. \n")
        print("----------\n")
        answer = input().lower()
        if answer == "y":
            return (new_files, [], 0, 0, 0, 0, 0)
        if answer == "n":
            answer = input(
                "Would you like us to delete this file and quit? y/N\n"
            ).lower()
            if answer == "y":
                print("Ok, nuking and quitting...")
                os.remove(target_dir)
                sleep(1)
                sys.exit()
            else:
                return (None, None, 0, 0, 0, 0, 0)
        else:
            return (None, None, 0, 0, 0, 0, 0)
    sleep(1)
    if temp_stat:
        return (new_files, old_files, total, nuked, skipped, size_k, starting_file_idx)
    return (new_files, old_files, 0, 0, 0, 0, 0)


def loader(file_list: list[str], target_dir: str) -> list[str]:
    """
    Finds, lists, and loads a full image file from a directory

    Args:
        file_list (list[str]): List of all files in the directory
        target_dir (str): Target directory, used to complete a full image path

    Returns:
        list[str]: List of new files after image loading
    """
    images = []
    backs.syscall(backs.TerminalCalls.CLEAR)

    for item in os.listdir(target_dir):
        if item.endswith(".list"):
            images.append(item)  # Look for image files and add them to dictionary

    if len(images) == 0:
        print("The directory doesn't appear to contain a '.list' image file.")
        print("you might want to find or create one before running this.")
        if input("Would you like to create one now? Y/N\n").lower() == "y":
            imager(file_list, target_dir)
            backs.syscall(backs.TerminalCalls.PAUSE)
            sys.exit()

    target_image = ""
    while target_image == "":
        print(
            "Please choose an image file from the list bellow (or type 'Q' if you changed your mind):"
        )
        for image in images:
            print(images.index(image), ":", image)
        print("\n")

        select = input().lower()
        if select == "q":
            return None
        try:
            target_image = target_dir + "/" + images[int(select)]
        except (IndexError, ValueError):
            print("It looks like you selected an invalid image, please try again\n")
            backs.syscall(backs.TerminalCalls.PAUSE)
    while True:
        answer = input(
            "What would you like to do with the image "
            + target_image
            + "? (U)se or (D)elete\n"
        ).lower()

        if answer == "u":
            new_files, old_files, _, _, _, _, _ = reader(
                target_image, file_list, False
            )  # Calls to read the image
            if old_files != []:
                with open(
                    target_dir + "/temp.list", "w", encoding="utf-8"
                ) as filehandle:
                    for item in old_files:
                        filehandle.write(item + "\n")
            return new_files
        if answer == "d":
            os.remove(target_image)
            print("Erased", target_image, "\n")
            backs.syscall(backs.TerminalCalls.PAUSE)
            sys.exit()
        else:
            print(backs.texter("unkerr"))


def read_temp_image(
    target_dir: str, file_list: list[str]
) -> tuple[list[str], int, int, int, int, int]:
    """
    Read a temp image file

    Args:
        target_dir (str): Path of the video dir
        file_list (list[str]): List of video files in the dir

    Returns:
        tuple[list[str], int, int, int, int, int]: new_files, total, nuked, skipped, size_k, starting_file_idx
    """
    print("It looks like the program was quit before you got through the directory")
    if input("Would you like to resume that list? Y/n\n").lower() == "n":
        print("I cleaned up, sorry about the interruption\n")
        os.remove(target_dir + "/temp.list")
        print("-" * 43)
        return (None, None, None, None, None, None)
    total = len(file_list)
    remaining_videos, _, totalS, nuked, skipped, size_k, starting_file_idx = reader(
        target_dir + "/temp.list", file_list, True
    )
    if remaining_videos is None:
        return (None, None, None, None, None, None)
    if totalS == 0:
        total = total - (total - len(remaining_videos))
    else:
        total = totalS
    return (remaining_videos, total, nuked, skipped, size_k, starting_file_idx)
