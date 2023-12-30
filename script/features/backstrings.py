import getpass
import platform
import random
import subprocess
import os
import sys
from time import sleep

from enum import Enum


class TerminalCalls(Enum):
    """
    An enum for terminal commands
    """

    PAUSE = 1
    CLEAR = 2


# Deals with the directory path
def dir_char_clipper(target_dir: str) -> str:
    """
    Strips special characters from a directory path depending on platform

    Args:
        target_dir (str): Directory path to strip

    Returns:
        str: Stripped directory path
    """
    stripped_dir = ""
    delchar = ["'", '"']
    if platform.system() in ("Linux", "Darwin"):
        delchar.append("\\")
    if target_dir.endswith(" "):
        target_dir = target_dir[:-1]
    for symbol in target_dir:
        if not symbol in delchar:
            stripped_dir = stripped_dir + symbol
    return stripped_dir


def search_dir(target_dir: str) -> list[str]:
    """
    Searches a directory for compatible files

    Args:
        target_dir (str): Directory to search

    Returns:
        list[str]: Compatible files in directory
    """
    filelist: list[str] = []
    for item in os.listdir(target_dir):
        if item.endswith((".mp4", ".mkv", ".mts", ".avi")):
            filelist.append(item)  # Only adding supported files to the list
    return filelist


def syscall(call: TerminalCalls):
    """
    Calls local system commands. Currently only terminal commands

    Args:
        call (TerminalCalls): An enum for terminal commands
    """
    if platform.system() in ("Linux", "Darwin"):
        match call:
            case TerminalCalls.PAUSE:
                subprocess.run(
                    "read -n 1 -r -s -p 'Press any key to continue...'",
                    shell=True,
                    executable="/bin/bash",
                    check=False,
                )
            case TerminalCalls.CLEAR:
                subprocess.run("clear", shell=True, executable="/bin/bash", check=False)
    elif platform.system() == "Windows":
        match call:
            case TerminalCalls.PAUSE:
                subprocess.run("pause", shell=True, check=False)

            case TerminalCalls.CLEAR:
                subprocess.run("cls", shell=True, check=False)
    else:
        print(texter("incomp"))
        sleep(10)
        sys.exit()


def display_stats(total_k_deleted: int, total: int, nuked: int, skipped: int):
    """
    Show the stats for a full directory run

    Args:
        total_k_deleted (int): Total number of KBs deleted
        total (int): Total number of files in the dir
        nuked (int): Number of files deleted
        skipped (int): Number of files skipped
    """
    size_k = total_k_deleted
    mettype = "KB"
    if size_k > 1024:
        size_k = size_k / 1024
        mettype = "MB"
        if size_k > 1024:
            size_k = size_k / 1024
            mettype = "GB"
    print("You have reached the end of the directory, good job!")
    print("Let's look at some numbers:")
    print("----------\n")
    print("You", texter("total"), total, "file(s)")
    print("----------\n")
    print("Out of those you", texter("nuked"), nuked, "file(s)")
    print("And", texter("skipped"), skipped, "file(s)")
    print("----------\n")
    print("That's", str(round(size_k, 2)) + mettype, "of storage savings!")
    print("----------\n")


def dev_credits():
    lines = [
        "That one script that let's you review videos",
        "Concepted, written and tested by:",
        "Saren Dev - https://github.com/SarenDev",
        "---AND---",
        'Proudly optimized by "the one and only":',
        "TrackLab - https://github.com/TrackLab",
        "---FINALLY---",
        "Checked out and maybe improved by...",
        getpass.getuser(),
    ]
    with open("features/boot.artwork", "r", encoding="utf-8") as filehandle:
        print(filehandle.read(), "\n")
        filehandle.close()
    for line in lines:
        print("\n")
        for letter in line:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(0.05)
    print("\n")
    return


def texter(text):
    # FIXME: This entire function is pretty garbage
    compat = "\n\n\nSomething seem to have gone awry in the world of compatibility, but fret not, for we will fix it soon\nFor now, we'll have to close down, it'll happen in a few seconds. Sorry about this...\n\n\n"

    unk_err = [
        "Something didn't go quite right, let's start over\n",
        "Something went sideways, we should go back to square 1\n",
        "What just happened? Wha- huh? Ok, this is too much, give me a sec\n",
    ]

    file_miss = [
        "That's odd, we couldn't find the file:",
        "I swear, the file was right here. Someone, help me find:",
        "Did I just get bamboozled by:",
        "Seriously?! That's not cool! Why'd they have to nick:",
    ]

    uns_yes = [
        "I didn't understand that, but I'll take it as a YES\n",
        "I might need a bit to decode that, but for now let's say it's a YES\n",
    ]

    uns_no = [
        "I didn't understand that, but I'll take it as a NO\n",
        "I might need a bit to decode that, but for now let's say it's a NO\n",
    ]

    total = [
        "looked at",
        "observed",
        "studied",
        "interrogated",
        "went through",
        "indexed",
        "checked",
        "noted down",
        "viewed",
    ]

    nuked = [
        "nuked",
        "obliterated",
        "decimated",
        "locked up",
        "snipped",
        "shredded",
        "totaled",
        "disintegrated",
        "zeroed",
    ]

    skipped = [
        "spared",
        "left be",
        "skipped",
        "saved",
        "archived",
        "kept",
        "salvaged",
        "left out",
        "greenlit",
    ]

    if text == "credits":
        return dev_credits()
    if text == "incomp":
        return compat
    if text == "unkerr":
        active = unk_err
    if text == "filemiss":
        active = file_miss
    if text == "uns_yes":
        active = uns_yes
    if text == "uns_no":
        active = uns_no
    if text == "total":
        active = total
    if text == "nuked":
        active = nuked
    if text == "skipped":
        active = skipped
    return active[random.randint(0, (len(active) - 1))]
