# vid-reviewr.py

```text
       _     _                           _                                      
      (_)   | |                         (_)                                     
__   ___  __| |  ______   _ __ _____   ___  _____      ___ __       _ __  _   _ 
\ \ / / |/ _` | |______| | '__/ _ \ \ / / |/ _ \ \ /\ / / '__|     | '_ \| | | |
 \ V /| | (_| |          | | |  __/\ V /| |  __/\ V  V /| |     _  | |_) | |_| |
  \_/ |_|\__,_|          |_|  \___| \_/ |_|\___| \_/\_/ |_|    (_) | .__/ \__, |
                                                                   | |     __/ |
                                                                   |_|    |___/ 
```

__*The script lets you go through the directory and choose which videos to leave or delete.*__

**It might sound useful already, but wait - there are some extra features:**

* *Stats*, to know what you deleted and how much space that saved
* *Autosave*, so that progress isn't lost if the app quits, or you decide to take a break
* *Manual save*, so that you don't have to go through a directory all over again; Instead, just look at the new files
<!-- * *Somewhat useful script launcher*, for those who want to run it in Python and need a tip when setting up -->
* *Extra bits for code reviewers and regular users*, be on the lookout

We currently support ".mp4", ".mkv", ".mts" and ".avi" files

> This script is also designed to handle video files that have multiple audio tracks, like those produced by screen recording software.
>
> The script can handle dual-track, dual-file recordings like those produced by AMD Adrenalin. It currently searches for ".m4a" companion files.

This was my first python project, so the older commits look really *really* bad. I came back ~4 years later to improve it, because I still use this script regularly and thought it needed a tuneup.

**Original script built for Python 3.8, rewritten for Python 3.11**

## System requirements

This script relies on VLC being installed on your machine and being accessible from the command line

*(In Windows you have to set VLC's directory as an environmental path, so it's accessible from CMD)*

As for running it in Python, you'll ~~obviously~~ need Python installed and working from the command line as well as making sure Pip works too. The script uses the "send2trash" module, so getting that out of the way will also be necessary.
