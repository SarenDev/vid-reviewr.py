import sys
import os
from time import sleep

import features.backstrings as backs
from features import video

CLASSIC = False

try:
    from features import imaging
except ImportError:
    CLASSIC = True


def classic_error():
    """
    Display an error when accessing non-Classic functions
    """
    print("This feature isn't available in Classic Mode, sorry")
    backs.syscall(backs.TerminalCalls.PAUSE)
    backs.syscall(backs.TerminalCalls.CLEAR)


def main():
    image = nuked = skipped = total_k_deleted = starting_file_idx = 0
    target_dir = ""

    backs.syscall(backs.TerminalCalls.CLEAR)
    print("Hi there and welcome to:")
    if not os.path.exists(os.getcwd() + "/features/boot.artwork"):
        print("\n[A logo-free]\nv i d - r e v i e w r . p y\n")
    else:
        with open("features/boot.artwork", "r", encoding="utf-8") as filehandle:
            print(filehandle.read(), "\n")
    print("-----A FULLY RE-WRITTEN V3-----\n\n")
    if CLASSIC:
        print("-" * 27)
        print("Now running in CLASSIC MODE")
        print("-" * 27)

    while not os.path.exists(target_dir):
        target_dir = input(
            "Punch up a directory for us to look at (or type 'Q' if you changed your mind): "
        )
        if target_dir in ("Q", "q"):
            sys.exit()

        backs.syscall(backs.TerminalCalls.CLEAR)
        if target_dir in ("C", "c"):
            backs.texter("credits")
            backs.syscall(backs.TerminalCalls.PAUSE)
            sys.exit()

        target_dir = backs.dir_char_clipper(target_dir)
        if not target_dir:
            sys.exit()
        if not os.path.exists(target_dir):
            print("The path you entered doesn't seem to be valid, let's start over")

    print("Let's look at " + target_dir)
    print("-" * (14 + len(target_dir)))
    full_video_list = backs.search_dir(
        target_dir
    )  # Preparing the file list and informing user
    total = len(full_video_list)

    if total == 0:
        print("It doesn't have any videos I can work with")
        print("-" * 43)
        print("Please pick another directory after this quick restart\n")
        backs.syscall(backs.TerminalCalls.PAUSE)
        sys.exit()

    print("\nIt contains", total, "video(s)")

    for item in os.listdir(target_dir):
        if item.endswith(".list") and not item.startswith("temp"):
            image += 1
    if image != 0:
        print("It also contains", image, "image(s) that you can load\n")
        print("-" * (44 + len(str(image))))  # Count images
    else:
        print("-" * (21 + len(str(image))))

    if os.path.exists(target_dir + "/temp.list"):
        if CLASSIC:
            print(
                "The directory contains a temporary image, but it can't be loaded in Classic Mode"
            )
        else:
            (
                remaining_video_list,
                total,
                nuked,
                skipped,
                total_k_deleted,
                starting_file_idx,
            ) = imaging.read_temp_image(target_dir, full_video_list)
            if remaining_video_list is None:
                sys.exit()
            video.player_call(
                remaining_video_list,
                target_dir,
                total,
                starting_file_idx,
                nuked,
                skipped,
                total_k_deleted,
            )
            sys.exit()

    while True:
        print("What would you like to do?\n")
        if CLASSIC:
            print("-" * 99)
            print("Since we're running in Classic Mode, some feature are disabled")
            print("-" * 99)
            print("(S)tart | (Q)uit\n")
        elif image != 0:
            print(
                "(O)pen an image | (S)tart | (C)reate an image of the directory | (Q)uit\n"
            )
        else:
            print("(S)tart | (C)reate an image of the directory | (Q)uit\n")
        match (input().lower()):
            case "c":
                if CLASSIC:
                    classic_error()
                    continue
                imaging.imager(full_video_list, target_dir)
                backs.syscall(backs.TerminalCalls.PAUSE)
                sys.exit()
            case "o":
                if CLASSIC:
                    classic_error()
                    continue
                remaining_video_list = imaging.loader(full_video_list, target_dir)
                if remaining_video_list is None:
                    continue
                if len(remaining_video_list) == 0:
                    print(
                        "It looks like nothing was added since we imaged the directory"
                    )
                    backs.syscall(backs.TerminalCalls.PAUSE)
                    continue
                total = total - (total - len(remaining_video_list))
                video.player_call(
                    remaining_video_list,
                    target_dir,
                    total,
                    starting_file_idx,
                    nuked,
                    skipped,
                    total_k_deleted,
                )
                sys.exit()
            case "s":
                video.player_call(
                    full_video_list,
                    target_dir,
                    total,
                    starting_file_idx,
                    nuked,
                    skipped,
                    total_k_deleted,
                )
                sys.exit()
            case "q":
                sys.exit()
            case "w":
                backs.texter("credits")
                backs.syscall(backs.TerminalCalls.PAUSE)
            case _:
                print(backs.texter("unkerr"))
                sleep(3)


if __name__ == "__main__":
    main()
