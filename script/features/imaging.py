from datetime import datetime
import os
from time import sleep
from .backstrings import texter,syscall

#Images the file list in its current state
def imager(filelist,direct):
    print("----------\n")
    print("The purpose of this feature is to image a directory, so you don't have to go through all of it again at a later date\n")
    pathway = direct+"/Full_Image-"+str(datetime.date(datetime.now()))+".list"
    if os.path.exists(pathway):
        answer=input("It looks like you already created an image today, would you like to overwrite it? Y/N\n")
        if answer in ("Y", "y"): pass
        else: 
            print("Ok, not overwriting anything...\n")
            return
    with open(pathway, "w") as filehandle:
        for item in filelist:
            filehandle.write(item+"\n")
    print("We wrote an image into the file: "+pathway+"\n")
    return

#Reads an image
def reader(path,filelist,temp_stat):
    outlist=[]
    imglist=[]
    total=nuked=skipped=size_m=pointd=0
    umcheck=len(filelist)
    if not os.path.exists(path):
          print(texter("filemiss")+path+"\n")
          syscall("pause")
          if temp_stat: return(False,False,False,False,False)
          return(False)
    with open(path,"r") as filehandle:      #Read the selected file into list
        imglist=filehandle.read().splitlines()
        filehandle.close()
    for item in filelist:
        if item in imglist:                #Compare and create new list, preforms an integrity check
            umcheck-=1
            pass
        else: outlist.append(item)
    if temp_stat: #Read stat file
        path_stat=path[:-4]+"stat"
        if not os.path.exists(path_stat):
            print("We couldn't find a stat file, so we'll ignore it...")
            total=nuked=skipped=size_m=0
            temp_stat=False
        if temp_stat:
            with open(path_stat, "r") as filehandle:
                line=filehandle.read().splitlines()
                total=int(line[0])
                nuked=int(line[1])
                skipped=int(line[2])
                size_m=int(line[3])
                pointd=int(line[4])
                filehandle.close
        temp_stat=True
    print("Image read!\n\n")
    if umcheck==len(filelist):
        if path.endswith("temp.list"):
            print("----------\n")
            print("This is bad, the autosave image we made failed our integrity check\n")
            print("We'll clean up and restart\n")
            syscall("pause")
            os.remove(path)
            try:os.remove(path[:-4]+"stat")
            except:pass
            return(False,False,False,False,False)
        print("----------\n")
        print("This is bad...\n"+"The image you loaded failed our integrity check\n")
        print("It could be that the file you're using is unbelievably old, came from another directory or is corrupted\n")
        print("Are you sure you want to continue with this image file? If you do - you might have to go through some files again. Y/N\n")
        print("----------\n")
        answer=input()
        if answer in ("Y","y"): return(True)
        elif answer in ("N","n"):
            answer=input("Would you like us to delete this file and quit? Y/N\n")
            if answer in ("Y", "y"):
                print("Ok, nuking and quitting...")
                os.remove(path)
                sleep(1)
                quit()
            elif answer in ("N", "n"): return(False)
            else:
                print(texter("uns_no"))
                syscall("pause")
                return(False)
        else:
            print(texter("uns_no"))
            syscall("pause")
            return(False)
    sleep(1)
    if temp_stat: return(outlist,total,nuked,skipped,size_m,pointd)
    return(outlist)

#Finds images for use
def loader(filelist,direct):
    listlist={}
    lcheck=0
    syscall("cls")
    for item in os.listdir(direct):
        if item.endswith(".list"):
            listlist.update({lcheck:item})  #Look for image files and add them to dictionary
            lcheck+=1
    if lcheck==0:
        print("The directory doesn't appear to contain a '.list' image file, you might want to find or create one before running this\n")
        if input("Would you like to create one now? Y/N\n") in ("Y", "y"):
            imager(filelist,direct)
            syscall("pause")
            quit()
    print("Please choose an image file from the list bellow (or type 'Q' if you changed your mind):\n")
    print(listlist)
    select=input()
    if select in ("Q", "q"): quit()
    try:
        select=int(select)
        path=direct+"/"+listlist[select]   
    except: 
        print("It looks like you selected an invalid image, please try again after we trip a quick restart\n")
        syscall("pause")
        loader(filelist,direct)
    answer=input("What would you like to do with the image "+listlist[select]+"? (U)se or (D)elete\n")
    if answer in ("U", "u"):
        outlist=reader(path,filelist) #Calls to read the image
        return outlist
    elif answer in ("D", "d"):
        os.remove(path)
        print("Erased",listlist[select],"\n")
        syscall("pause")
        quit()
    else:
        print(texter("unkerr"))
        syscall("pause")
        loader(filelist,direct)
