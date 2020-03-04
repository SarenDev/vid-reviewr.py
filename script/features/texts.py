import random, sys, getpass
from time import sleep

def credts():
    lines = ["That one script that let's you review videos",
         "Written, concepted, tested by:",
         "Saren Dev - https://github.com/SarenDev",
         "---AND---",
         'Proudly optimized by the "one and only":',
         "TrackLab - https://github.com/TrackLab",
         "---FINALLY---",
         "Checked out and maybe improved by...",
         getpass.getuser()]
    with open("features/boot.artwork","r") as filehandle: 
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

    incomp="\n\n\nSomething seem to have gone awry in the world of compatibility, but fret not, for we will fix it soon\nFor now, we'll have to close down, it'll happen in a few seconds. Sorry about this...\n\n\n"

    unkerr=["Something didn't go quite right, let's start over\n", "Something went sideways, we should go back to square 1\n", "What just happened? Wha- huh? Ok, this is too much, give me a sec\n"]

    filemiss=["That's odd, we couldn't find the file:", "I swear, the file was right here. Someone, help me find:", "Did I just get bamboozled by:", "Seriously?! That's not cool! Why'd they have to nick:"]

    uns_yes=["I didn't understand that, but I'll take it as a YES\n", "I might need a bit to decode that, but for now let's say it's a YES\n"]

    uns_no=["I didn't understand that, but I'll take it as a NO\n", "I might need a bit to decode that, but for now let's say it's a NO\n"]

    if text=="credits": return(credts())
    if text=="incomp": return(incomp)
    if text=="unkerr": active=unkerr
    if text=="filemiss": active=filemiss
    if text=="uns_yes": active=uns_yes
    if text=="uns_no": active=uns_no
    return(active[random.randint(0,(len(active)-1))])
