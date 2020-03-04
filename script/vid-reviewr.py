import os
import subprocess
import platform
from time import sleep
from send2trash import send2trash
try:
    from features.texts import texter
    from features import imaging            #Attempt to import files from /features
    from features.syscall import syscall
except:
    print("I'm afaid this must end here\n\n")
    print("Since you are missing the /features directory, that contains critical files, we have to quit\n")
    print("It's not you, it's us. Since the script will crash if those files go away")
    sleep(10)
    quit()

total=0
nuked=0
skipped=0

#Deals with the directory path
def clipper(direct):
    rendirect=""
    delchar=["'",'"']
    if platform.system()=="Linux": delchar.append("\\")
    if direct.endswith(" "): direct=direct[:-1]       
    for symbl in direct:
        if not symbl in delchar: rendirect=rendirect+symbl
    return(rendirect)

#Converts the items of the directory into a list
def formatter(direct):
    filelist=[]
    for item in os.listdir(direct):
        if item.endswith(".mp4") or item.endswith(".mkv"):
            filelist.append(item)   #Only adding ".mp4" or ".mkv" files to the list
    return(filelist)



#Plays and act on the files
def player(origin,target,pointer):
    global total, nuked, skipped
    syscall("cls")
    if not os.path.exists(origin+"/"+target):
        print(texter("filemiss")+target)
        sleep(1)
        return
    print ("Playing: "+target+" ||",pointer,"/",total)
    command= 'vlc --quiet --sout-all --sout "#display"' + ' "' + origin + '/' + target + '"'
    subprocess.call(command, shell=True, stdout=open(os.devnull,"w"), stderr=subprocess.STDOUT)
    answer = input("What would you like to do with this file?\n (D)elete | (S)kip | (R)eplay | (Q)uit\n")
    if answer in ("D", "d"):
        print("Deleted: "+target)
        send2trash(origin+"/"+target)
        nuked+=1
        sleep(1)
        return
    elif answer in ("S", "s"):
        print("Skipped: "+target)
        with open(origin+"/temp.list", "a") as filehandle:
            filehandle.write(target+"\n")
            filehandle.close()
        skipped+=1
        sleep(1)
        return
    elif answer in ("R", "r"):
        print("Replaying: "+target)
        sleep(1)
        player(origin, target, pointer)
    elif answer in ("Q", "q"):
        print("Ok, quitting...")
        sleep(1)
        quit()
    else:
        print(texter("unkerr"))
        sleep(1)
        player(origin, target, pointer)

#Runs the player through all the files and deals with statistics as well as a graceful exit
def player_call(files,direct):
    global total, nuked, skipped
    pointer=0
    for item in files:
        pointer+=1
        player(direct, item, pointer)
    syscall("cls")
    os.remove(direct+"/temp.list")
    print("You have reached the end of the directory, good job!\n")
    print("Let's look at some numbers:\n")
    print("----------\n")
    print("You looked at",total,"file(s)\n")
    print("----------\n")
    print("Out of those you nuked",nuked,"file(s)\n")
    print("And spared",skipped,"file(s)\n")
    print("----------\n")
    print("We also imaged the directory for you convenience\n")
    imaging.imager(files,direct)
    syscall("pause")
    quit()

#The executive part
def main():
    global total
    image=0
    syscall("cls")
    print("Hi there and welcome to:\n")
    if not os.path.exists(os.getcwd()+"/features/boot.artwork"): print("[A logo-free]\nv i d - r e v i e w r . p y\n")
    else:
        with open("features/boot.artwork","r") as filehandle: 
            print(filehandle.read(), "\n")
            filehandle.close()
    direct=input("Punch up a directory for us to look at (or type 'Q' if you changed your mind):\n")
    if direct in ("Q","q"): quit()
    syscall("cls")
    if direct=="c": 
        texter("credits")
        syscall("pause")
        main()
    direct=clipper(direct)
    if not direct: main()
    if not os.path.exists(direct):
        print("The path you entered doesn't seem to be vaild, let's start over\n")
        syscall("pause")
        main()
    print("Let's look at "+direct+"\n")
    print("----------\n")
    filelist=formatter(direct)
    total=len(filelist)
    if total==0:
        print("It doesn't have any videos we can work with\n")
        print("----------\n")
        print("Please pick another directory after this quick restart\n")
        syscall("pause")
        main()
    print("It contains",total,"video(s)\n")
    for item in os.listdir(direct):
        if (item.endswith(".list") and not item.startswith("temp")): image+=1
    if image!=0:
        print("It also conatins",image,"image(s) that you can load\n")
    print("----------\n")
    if os.path.exists(direct+"/temp.list"):
        print("It looks like the program was quit before you got through the directory\n")
        answer=input("Would you like to resume that list? Y/N\n")
        if answer in ("Y","y"):
            filelistM=imaging.reader(direct+"/temp.list", filelist)
            if type(filelistM) is bool: main()
            total=total-(total-len(filelistM))      #Run recovery from temp.list
            player_call(filelistM,direct)
        elif answer in ("N", "n"):
            print("We cleaned up, sorry about the interruption\n")
            os.remove(direct+"/temp.list")
            print("----------\n")
        else:
            print(texter("unkerr"))
            sleep(3)
            main()
    print ("What would you like to do?\n")
    if image!=0: print("(O)pen an image | (S)tart | (C)reate an image of the directory | (Q)uit\n")
    else: print("(S)tart | (I)mage the directory | (Q)uit\n")
    answer=input()
    if answer in ("C","c"):
        imaging.imager(filelist,direct)
        syscall("pause")
        quit()
    elif answer in ("O","o"):
        filelistM=imaging.loader(filelist,direct)
        if filelistM==False:
            player_call(filelist,direct)
        if len(filelistM)==0:
            syscall("cls")
            print("It looks like nothing was added since we imaged the directory. Let's call it a day\n\n")
            syscall("pause")
            quit()
        total=total-(total-len(filelistM))
        player_call(filelistM,direct)
    elif answer in ("S","s"):
        player_call(filelist,direct)
    elif answer in ("Q","q"):
        print("Ok, quitting...")
        sleep(1)
    elif answer in ("W", "w"):
        texter("credits")
        syscall("pause")
        main()
    else:
        print(texter("unkerr"))
        sleep(3)
        main()

main()
