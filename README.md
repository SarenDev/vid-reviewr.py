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

**It might sound useful already, but wait - there are some extra features:**

* *Progress autosave*, to never lose progress if the you or app quits
* *Manual save*, so that you don't have to go through a directory all over again; Instead, just look at the new files
* *Somewhat useful script launcher*, for those who want to run it as it was intended, in good old Python
* *Review-and-edit-friendly code structure*, while not a feature per say it is just good organization

This is my first project in Python, so some things aren't as straight forward as they could be. Sorry if that's somehow dissapointing

### Critical requirements:
This script relies on VLC being installed on your machine and being accessible from the command line 

*(In Windows you have to set VLC's directory as an environmental path)*

As for running it in Python, you'll ~~obviously~~ need Python installed and working from the command line as well as making sure Pip works too. The script uses the "send2trash" module so getting that out of the way will also be important.

### For potential contributors or those who want to live on the edge:
Simply clone, fork or warily observe the "beta-bekr" branch. If it gets too unstable for you, fall back to the safety of "master"
*If "beta-bekr is missing, nothing new is brewin' so just use good-ole "master"*
