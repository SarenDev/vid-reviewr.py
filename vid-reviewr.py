total=0
nuked=0
skipped=0
size_m=0
classic=False
import os
import subprocess
import platform
from time import sleep
from send2trash import send2trash
try: from features.backstrings import texter,syscall
except:
    print("I'm sorry, we can't continue...")
    print("'vid-reviewr.py' is designed to be somewhat modular, but this is a bit much")
    print("The '/features' directory needs to contain 'backstrings.py' for the script to run")
    print("Since without the script will crash, we have to quit right now")
    sleep(10)
    quit()
try: from features import imaging
except: classic=True

def classic_fault():
    syscall("cls")
    print("This feature isn't available in classic mode, sorry")
    sleep(5)
    main()

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
def player(origin,target,pointer,pointd):
    global total, nuked, skipped, size_m
    syscall("cls")
    if not os.path.exists(origin+"/"+target):
        print(texter("filemiss")+target)
        sleep(1)
        return
    print ("Playing: "+target+" ||",pointd,"/",total)
    command= 'vlc --quiet --sout-all --sout "#display"' + ' "' + origin + '/' + target + '"'
    subprocess.call(command, shell=True, stdout=open(os.devnull,"w"), stderr=subprocess.STDOUT)
    answer = input("What would you like to do with this file?\n (D)elete | (S)kip | (R)eplay | (Q)uit\n")
    if answer in ("D", "d"):
        print("Deleted: "+target)
        size_m+=round((os.stat(origin+"/"+target).st_size)/(1024 * 1024))
        if platform.system()=="Linux": send2trash(origin+"/"+target)
        else: send2trash(origin+"\\"+target)
        nuked+=1
        with open(origin+"/temp.stat", "w") as filehandle:
            filehandle.write(str(total)+"\n"+str(nuked)+"\n"+str(skipped)+"\n"+str(size_m)+"\n")
            filehandle.close()
        sleep(1)
        return
    elif answer in ("S", "s"):
        print("Skipped: "+target)
        with open(origin+"/temp.list", "a") as filehandle:
            filehandle.write(target+"\n")
            filehandle.close()
        skipped+=1
        with open(origin+"/temp.stat", "w") as filehandle:
            filehandle.write(str(total)+"\n"+str(nuked)+"\n"+str(skipped)+"\n"+str(size_m)+"\n")
            filehandle.close()
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
def player_call(files,direct,pointd):
    global total, nuked, skipped, size_m
    pointer=0
    mettype="MB"
    for item in files:
        pointer+=1
        pointd+=1
        player(direct, item, pointer, pointd)
        with open(direct+"/temp.stat", "a") as filehandle: #Calling player, while passing display values loaded from file (if it happened)
            filehandle.write(str(pointd))
            filehandle.close()
    syscall("cls")
    try:os.remove(direct+"/temp.list")
    except:pass
    try:os.remove(direct+"/temp.stat")
    except:pass
    if size_m>1024: 
        size_m=round(size_m/1024)
        mettype="GB"
        if size_m>1024:
            size_m=round(size_m/1024)
            mettype="TB"
    print("You have reached the end of the directory, good job!")
    print("Let's look at some numbers:")
    print("----------\n")
    print("You",texter("total"),total,"file(s)")
    print("----------\n")
    print("Out of those you",texter("nuked"),nuked,"file(s)")
    print("And",texter("skipped"),skipped,"file(s)")
    print("----------\n")
    print("That's",str(size_m)+mettype,"of storage savings!")
    print("----------\n")
    try:imaging.imager(files,direct)
    except:pass
    syscall("pause")
    quit()

#The executive part
def main():
    global total, classic, nuked, skipped, size_m
    image=0
    syscall("cls")
    print("Hi there and welcome to:")
    if not os.path.exists(os.getcwd()+"/features/boot.artwork"): print("\n[A logo-free]\nv i d - r e v i e w r . p y\n")
    else:
        with open("features/boot.artwork","r") as filehandle: 
            print(filehandle.read(), "\n")
            filehandle.close()
    if classic: 
        print("-"*27)
        print("Now running in CLASSIC MODE")
        print("-"*27)
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
    print("Let's look at "+direct)
    print("-"*(14+len(direct)))
    filelist=formatter(direct)
    total=len(filelist)
    if total==0:
        print("It doesn't have any videos I can work with")
        print("-"*43)
        print("Please pick another directory after this quick restart\n")
        syscall("pause")
        main()
    print("\nIt contains",total,"video(s)")
    for item in os.listdir(direct):
        if (item.endswith(".list") and not item.startswith("temp")): image+=1
    if image!=0:
        print("It also conatins",image,"image(s) that you can load\n")
        print("-"*(44+len(str(image))))
    else: print("-"*(21+len(str(image))))
    if os.path.exists(direct+"/temp.list"):
        if classic:
            print("I ran into problems with an Autosave image")
            os.remove(direct+"/temp.list")
            classic_fault()
        print("It looks like the program was quit before you got through the directory")
        answer=input("Would you like to resume that list? Y/N\n")
        if answer in ("Y","y"):
            filelistM,totalS,nuked,skipped,size_m,pointd=imaging.reader(direct+"/temp.list",filelist,True)
            if type(filelistM) is bool: main()     #Run recovery from temp.list
            if totalS==0: total=total-(total-len(filelistM))
            else: total=totalS
            player_call(filelistM,direct,pointd)
        elif answer in ("N", "n"):
            print("I cleaned up, sorry about the interruption\n")
            os.remove(direct+"/temp.list")
            print("-"*43)
        else:
            print(texter("unkerr"))
            sleep(3)
            main()
    print ("What would you like to do?\n")
    if classic: 
        print("-"*99)
        print("Since we're running in Classic Mode, because 'backstrings.py' isn't here, some feature are missing")
        print("-"*99)
        print("(S)tart | (Q)uit\n")
    elif image!=0: print("(O)pen an image | (S)tart | (C)reate an image of the directory | (Q)uit\n")
    else: print("(S)tart | (C)reate an image of the directory | (Q)uit\n")
    answer=input()
    if answer in ("C","c"):
        if classic: classic_fault()
        imaging.imager(filelist,direct)
        syscall("pause")
        quit()
    elif answer in ("O","o"):
        if classic: classic_fault()
        filelistM=imaging.loader(filelist,direct)
        if filelistM==False:
            player_call(filelist,direct,0)
        if len(filelistM)==0:
            syscall("cls")
            print("It looks like nothing was added since we imaged the directory. Let's call it a day\n\n")
            syscall("pause")
            quit()
        total=total-(total-len(filelistM))
        player_call(filelistM,direct,0)
    elif answer in ("S","s"):
        player_call(filelist,direct,0)
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