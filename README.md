```
       _     _                           _                                      
      (_)   | |                         (_)                                     
__   ___  __| |  ______   _ __ _____   ___  _____      ___ __       _ __  _   _ 
\ \ / / |/ _` | |______| | '__/ _ \ \ / / |/ _ \ \ /\ / / '__|     | '_ \| | | |
 \ V /| | (_| |          | | |  __/\ V /| |  __/\ V  V /| |     _  | |_) | |_| |
  \_/ |_|\__,_|          |_|  \___| \_/ |_|\___| \_/\_/ |_|    (_) | .__/ \__, |
                                                                   | |     __/ |
                                                                   |_|    |___/ 
```
## vid-reviewr.py

__*The script lets you go through the directory and choose which videos to leave and which to delete.*__

**It might sound interesting already, but there are some extra features:**

* *Autosave*, to never lose progress if the app (or you) quits
* *Normal save*, so that you don't have to go through a directory all over again; Instead, just look at the new files
* *Somewhat useful launcher*, for those who want to run it as it was intended
* *That's basically it*... so far! Improvements to become available, maybe

This is a first project type of deal, so quality isn't a guarantee... but then again, when is it ever?

### Critical requirements:
This script relies on VLC being installed on your machine and bein accessible from the command line 

*(In Windows you have to set VLC's directory as an environmental path)*

As for running it in Python, you'll ~~obviously~~ need Python installed and working from the command line as well as making sure Pip works too. The script uses the "send2trash" module so getting that out of the way will also be important.
