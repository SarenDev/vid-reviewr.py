#-----------------------------------------------------------------------------------------------------------------------------
# Proudly optimized by the one and only TrackLab - https://www.youtube.com/channel/UCxeUx7kNlG5iq-pJrDNKKKg
#-----------------------------------------------------------------------------------------------------------------------------
import os
from time import sleep
from send2trash import send2trash
from datetime import datetime

total=0
nuked=0
skipped=0

#Deals with the directory path
def clipper(direct):       
    if direct.startswith('"') and direct.endswith('"'):
        direct=direct[1:-1] #Clip the quotes off of the directory listing
    if direct.startswith('"') or direct.endswith('"'):
        print('The path seems to have broken quotes, let\'s start over') #If the quotes are incomplete we should reset
        return(False)
    else:
        pass #The user has already removed the quotes, all good to go
    return(direct)

#Converts the items of the directory into a list
def formatter(direct):
    filelist=[]
    for item in os.listdir(direct):
        if item.endswith(".mp4") or item.endswith(".mkv"):
            filelist.append(item)   #Only adding ".mp4" or ".mkv" files to the list
    return(filelist)

#Images the file list in its current state
def imager(filelist,direct):
    print('----------\n')
    print('The purpose of this feature is to image a directory, so you don\'t have to go through all of it again at a later date\n')
    pathway = direct+'\\Full_Image-'+str(datetime.date(datetime.now()))+'.list'
    if os.path.exists(pathway):
        answer=input('It looks like you already created an image today, would you like to overwrite it? Y/N\n')
        if answer in ("Y", "y"): pass
        else: 
            print('Ok, not overwriting anything...\n')
            return
    with open(pathway, 'w') as filehandle:
        for item in filelist:
            filehandle.write(item+'\n')
    print('We wrote an image into the file: '+pathway+'\n')
    return

#Reads an image
def reader(path,filelist):
    outlist=[]
    imglist=[]
    umcheck=len(filelist)
    if not os.path.exists(path):
          print('That\'s odd, we couldn\'t find the file '+path+'\n')
          os.system('pause')
          return(False)
    with open(path,'r') as filehandle:      #Read the selected file into list
        for line in filehandle:
            pointer=line[:-1]
            imglist.append(pointer)  
    for item in filelist:
        if item in imglist:                #Compare and create new list, preforms an integrity check
            umcheck-=1
            pass
        else:
            outlist.append(item)
    print('Image read!\n\n')
    if umcheck==len(filelist):
        if path.endswith('temp.list'):
            print('----------\n')
            print('This is bad, the autosave image we made failed our integrity check\n')
            print('We\'ll clean up and restart\n')
            os.system('pause')
            os.remove(path)
            return(False)
        print('----------\n')
        print('This is bad...\n'+'The image you loaded failed our integrity check\n')
        print('It could be that the file you\'re using is unbelievably old, came from another directory or is corrupted\n')
        print('Are you sure you want to continue with this image file? If you do - the list might have. Y/N\n')
        print('----------\n')
        answer=input()
        if answer in ("Y","y"):
            return(True)
        elif answer in ("N","n"):
            answer=input('Would you like us to delete this file and quit? Y/N\n')
            if answer in ("Y", "y"):
                print('Ok, nuking and quitting...')
                os.remove(path)
                sleep(1)
                quit()
            elif answer in ("N", "n"):
                return(False)
            else:
                print('I didn\'t understand that, but I\'ll take it as a NO\n')
                os.system('pause')
                return(False)
        else:
            print('I didn\'t understand that, but I\'ll take it as a NO\n')
            os.system('pause')
            return(False)
    os.system('pause')
    return(outlist)

#Finds images for use
def loader(filelist,direct):
    listlist={}
    lcheck=0
    os.system('cls')
    for item in os.listdir(direct):
        if item.endswith('.list'):
            listlist.update({lcheck:item})  #Look for image files and add them to dictionary
            lcheck+=1
    if lcheck==0:
        print('The directory doesn\'t appear to contain a ".list" image file, you might want to find or create one before running this\n')
        if input('Would you like to create one now? Y/N\n') in ("Y", "y"):
            imager(filelist,direct)
            os.system('pause')
            quit()
    print('Please choose an image file from the list bellow:\n')
    print(listlist)
    select=int(input())
    path=direct+'\\'+listlist[select]   #Calls to read the image
    outlist=reader(path,filelist)
    if not outlist: loader(filelist,direct)
    if outlist=='cont': return(False)
    return outlist

#Plays and act on the files
def player(origin,target,pointer):
    global total, nuked, skipped
    os.system('cls')
    if not os.path.exists(origin+'\\'+target):
        print('That\'s odd, we couldn\'t find the file: '+target)
        sleep(1)
        return
    print ('Playing: '+target+' ||',pointer,'/',total)
    command= 'vlc'+ ' --sout-all --sout #display' + ' "' + origin + '\\' + target + '"'
    os.system(command)
    answer = input('What would you like to do with this file?\n (D)elete | (S)kip | (R)eplay | (Q)uit\n')
    if answer in ("D", "d"):
        print('Deleted: '+target)
        send2trash(origin+'\\'+target)
        nuked+=1
        sleep(1)
        return
    elif answer in ("S", "s"):
        print('Skipped: '+target)
        with open(origin+'\\temp.list', 'a') as filehandle:
            filehandle.write(target+'\n')
        skipped+=1
        sleep(1)
        return
    elif answer in ("R", "r"):
        print('Replaying: '+target)
        sleep(1)
        player(origin, target)
    elif answer in ("Q", "q"):
        print('Ok, quitting...')
        sleep(1)
        quit()
    else:
        print('Something didn\'t go quite right, let\'s play'+target+' again')
        sleep(1)
        player(origin, target)

#Runs the player through all the files and deals with statistics as well as a graceful exit
def player_call(files,direct):
    global total, nuked, skipped
    pointer=0
    actlist=[]
    for item in files:
        pointer+=1
        player(direct, item, pointer)
    os.system('cls')
    os.remove(direct+'\\temp.list')
    print('You have reached the end of the directory, good job!\n')
    print('Let\'s look at some numbers:\n')
    print('----------\n')
    print('You looked at',total,'files\n')
    print('----------\n')
    print('Out of those you nuked',nuked,'files\n')
    print('And spared',skipped,'files\n')
    print('----------\n')
    print('We also imaged the directory for you convenience\n')
    imager(files,direct)
    os.system('pause')
    quit()

#The executive part
def main():
    global total
    image=0
    os.system('cls')
    print('Hey, this is a video review script that lets you quickly sort through a directory of vids and act on them\n')
    print('This script requires that you set your copy of "VLC" as an Enviroment Variable\n\n')
    direct=input('Enter the directory:\n')
    os.system('cls')
    direct=clipper(direct)
    if not direct:
        main()
    if not os.path.exists(direct):
        print('The path you entered doesn\'t seem to be vaild, let\'s start over\n')
        os.system('pause')
        main()
    print('Let\'s look at '+direct+'\n')
    print('----------\n')
    filelist=formatter(direct)
    total=len(filelist)
    if total==0:
        print('It doesn\'t have any videos we can work with\n')
        print('----------\n')
        print('Please pick another directory after this quick restart\n')
        os.system('pause')
        main()
    print('It contains',total,'video(s)\n')
    for item in os.listdir(direct):
        if item[-4]=='l':
            image+=1
        else: pass
    if image!=0:
        print('It also conatins',image,'image(s) that you can load\n')
    print('----------\n')
    if os.path.exists(direct+'\\temp.list'):
        print('It looks like the program was quit before you got through the directory\n')
        answer=input('Would you like to resume that list? Y/N\n')
        if answer in ("Y","y"):
            filelistM=reader(direct+'\\temp.list', filelist)
            if type(filelistM) is bool:main()
            total=total-(total-len(filelistM))
            player_call(filelistM,direct)
        elif answer in ("N", "n"):
            print('We cleaned up, sorry about the interruption\n')
            os.remove(direct+'\\temp.list')
            print('----------\n')
        else:
            print('Something didn\'t go quite right, let\'s start over\n')
            os.system('pause')
            main()
    print ('What would you like to do?\n')
    if image!=0: print('(R)ead an image |(C)ontinue | (I)mage the directory | (Q)uit\n')
    else: print('(C)ontinue | (I)mage the directory | (Q)uit\n')
    answer=input()
    if answer in ("I","i"):
        imager(filelist,direct)
        os.system('pause')
        quit()
    elif answer in ("R","r"):
        filelistM=loader(filelist,direct)
        if not filelistM:
            player_call(filelist,direct)
        if len(filelistM)==0:
            os.system('cls')
            print('It looks like nothing has changed since we imaged the directory. Let\'s call it a day\n')
            os.system('pause')
            quit()
        total=total-(total-len(filelistM))
        player_call(filelistM,direct)
    elif answer in ("C","c"):
        player_call(filelist,direct)
    elif answer in ("Q","q"):
        print('Ok, quitting...')
        sleep(1)
    else:
        print('Something didn\'t go quite right, let\'s start over\n')
        os.system('pause')
        main()

main()
