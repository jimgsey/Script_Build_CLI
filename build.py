#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import libraries
import os
import os.path
import sys
import json
import hashlib
import fileinput
import glob
import re
import shutil
import requests
from subprocess import call
from datetime import datetime
import time

################################################
# Generic variables
argn=len(sys.argv)
romlist=["aicp",  "aex",  "altair",  "aokp",  "aoscp",  "aosip",  "candy",  "carbon",  "citrus",  "colt",  "corvus",  "cosmic",  "cosp",  "crdroid",  "derpfest",  "dot",  "floko",  "havoc",  "ion",  "lineage",  "lotus",  "nitrogen",  "paranoid",  "reloaded",  "renouveau",  "revenge",  "resurrectionremix",  "stag",  "statix",  "superior",  "viper",  "xenon",  "xtended"]
clen=["make", "delete", "no", "reset", "zip"]
patc=["yes", "no", "gapps"]
yesno=["yes","no"]
princof=["make", "delete","yes", "gapps", "reset", "zip"]
device="lavender"
deviceu="lavender-userdebug"
##################################
CORE="4"
## You could add your link to CLI, that way, you could see the process when a message is sent for example to your server:https://buildkite.com/jimgsey/ or your web: https://jimgsei.github.io.
LINKCLI = "http://jimgsei.github.io"
INFOCLI = "Link to CLI: {0}".format(LINKCLI)

## Your link server generate. For example Sourceforge: https://sourceforge.net/projects/lavender7/files
LINKSOU = "https://sourceforge.net/projects/lavender7/files"

## Your link account to upload. For example: jim15@frs.sourceforge.net:/home/frs/project/
LINKUPL = "jim15@frs.sourceforge.net:/home/frs/project/lavender7/"

## Device Default structure
DEVICES = "xiaomi/lavender"

#Telegram bot setting 
bot_token = ''
bot_chatID = ''

## Folder Builds working
RED = '\033[1;31m'
CYAN = '\033[1;36m'
YELLOW = '\033[1;33m'
GREEN = '\033[1;32m'
NOC = '\033[0;0m'
BOLD = '\033[1m'


## Tools (It is inside the android folder) and inside is the Roms and Tree folder
### Tools/Roms (A copy of the rom is made when the build is finished and then maintained. So you can delete the source folder to have more space.)
### Tools/Tree (Copy the vendor and kernel folder into the "Common" folder) (copy your device folder into another with the name of the rom)
### Example
#          __________________________________________________________________
#         |                                                                                                       |
#         |  /home/Android/Tools/Tree/                                                           |
#         |                       l___ Aicp/device/xiaomi/lavender                             |
#         |                       l___ Common/vendor/xiaomi/lavender                     |
#         |                       l___ Common/kernel/xiaomi/lavender                      |
#         |__________________________________________________________________|
#
SCRIPT = "/home/jimgsey/Android"
SCRIPTFOLDER = "/home/jimgsey/Android/Builds"
TOOL = "{0}/Tools".format(SCRIPT)
TOOLTREE = "{0}/Tree".format(TOOL)
TOOLROM = "{0}/Roms".format(TOOL)
TOOLPATCH = "{0}/Patch".format(TOOL)
TOOLLOG = "{0}/Log".format(TOOL)

# Out folder where the rom is compiled. Example to lavender: "out /target/product/lavender" 
OUTF = "out/target/product/lavender/"

####################################################
# You can add your repo Q or Pie
ROMSI = {
'AICPLINK' : 'https://github.com/AICP/platform_manifest.git -b p9.0', 
'AEXLINK' :  'https://github.com/AospExtended/manifest.git -b 9.x', 
'ALTAIRLINK' : 'https://github.com/AltairROM/android -b p', 
'AOKPLINK' : 'https://github.com/AOKP/platform_manifest.git -b pie', 
'AOSIPLINK' : 'https://github.com/AOSiP/platform_manifest.git -b pie', 
'ARROWLINK' : 'https://github.com/ArrowOS/android_manifest.git -b arrow-9.x', 
'BOOTLEGGERSLINK' : 'https://github.com/BootleggersROM/manifest.git -b pasta',
'CANDYLINK' : 'https://github.com/CandyRoms/candy.git -b c9.0', 
'CARBONLINK' : 'https://github.com/CarbonROM/android.git -b cr-7.0 ', 
'COLTLINK' : 'https://github.com/Colt-Enigma/platform_manifest.git -b wip', 
'CORVUSLINK' : 'https://github.com/du-rex/android_manifest.git -b p9x-caf', 
'COSMICLINK' : 'https://github.com/Cosmic-OS/platform_manifest.git -b corona-release', 
'COSPLINK' : 'https://github.com/cosp-project/manifest -b pie', 
'CRDROIDLINK' : 'https://github.com/crdroidandroid/android.git -b 9.0', 
'DERPFESTLINK' : 'https://github.com/DerpFest-Pie/platform_manifest.git -b pie', 
'DOTPLINK' : 'https://github.com/DotOS/manifest.git -b dot-p', 
'FLOKOLINK' : 'https://github.com/FlokoROM/manifesto.git -b 9.0', 
'HAVOCLINK' : 'https://github.com/Havoc-OS/android_manifest.git -b pie', 
'IONLINK' : 'https://github.com/i-o-n/manifest -b pie', 
'LINEAGELINK' : 'https://github.com/LineageOS/android.git -b lineage-16.0', 
'LOTUSLINK' : 'https://github.com/LotusOS/android_manifest.git -b pie', 
'NITROGENLINK' : 'https://github.com/nitrogen-project/android_manifest.git -b p', 
'PARANOIDLINK' : 'https://github.com/AOSPA/manifest -b pie', 
'RELOADEDLINK' : 'https://github.com/ReloadedOS/android_manifest.git -b pie', 
'RENOUVEAULINK' : 'https://github.com/RenouveauOS/android.git -b renouveau-9.0', 
'REVENGELINK' : 'https://github.com/RevengeOS/android_manifest -b r9.0-caf', 
'RESURRECTIONREMIXLINK' : 'https://github.com/RR-Test/platform_manifest.git -b test_pie', 
'STAGLINK' : 'https://github.com/StagOS/manifest.git -b p9', 
'STATIXLINK' : 'https://github.com/StatiXOS/android_manifest.git -b 9-caf', 
'VIPERLINK' : 'https://github.com/ViperOS/viper_manifest.git -b pie', 
'XENONLINK' : 'https://github.com/TeamHorizon/platform_manifest.git -b p', 
'XTENDEDLINK' : 'https://github.com/Project-Xtended/manifest.git -b xp', 
}
################### ZIP ROMS #################################
ROMZI = {
'AICPZIP' : 'aicp_lavender_p*.zip', 
'AEXZIP' : 'AospEx*.zip', 
'ALTAIRZIP' : 'Altair*.zip', 
'AOKPZIP' : 'aokp_lavender_pie*.zip', 
'AOSIPZIP' : 'AOSiP-9.0-Pizza*.zip', 
'ARROWZIP' : 'Arrow-v9.0-lavender*.zip', 
'BOOTLEGGERSZIP' : 'BootleggersROM-Pie*.zip',
'CANDYZIP' : 'Candy*.zip', 
'CARBONZIP' : 'CARBON*.zip', 
'COLTZIP' : 'ColtOS*.zip', 
'CORVUSZIP' : 'Cor*.zip', 
'COSMICZIP' : 'Cosmic-OS-v4.0-Corona*.zip', 
'COSPZIP' : 'COSP*.zip', 
'CRDROIDZIP' : 'crDroidAndroid-9*.zip', 
'DERPFESTZIP' : 'AOSiP-9.0-DerpFest*.zip', 
'DOTZIP' : 'dotOS-P*.zip', 
'FLOKOZIP' : 'Floko*.zip', 
'HAVOCZIP' : 'Havoc*.txt', 
'IONZIP' : 'ion*.zip', 
'LINEAGEZIP' : 'lineage-16*.zip', 
'LOTUSZIP' : 'Lo*.zip', 
'NITROGENZIP' : 'Nitrogen*.zip', 
'PARANOIDZIP' : 'Pa*.zip', 
'RELOADEDZIP' : 'Reloaded-9.0*.zip', 
'RENOUVEAUZIP' : 'Reno*.zip', 
'REVENGEZIP' : 'RevengeOS*.zip', 
'RESURRECTIONREMIXZIP' : 'RR-P-v7*.zip', 
'STAGZIP' : 'stag_lavender_p*.zip', 
'STATIXZIP' : 'statix*.zip', 
'VIPERZIP' : 'Viper*.zip', 
'XENONZIP' : 'XenonHD*.zip', 
'XTENDEDZIP' : 'Xtended*.zip', 
}
#####################################################

    
def inis():
    print("{0}".format(BOLD))    
    print("*********************************")		
    print("                                 ")		
    print("            𝕾𝖈𝖗𝖎𝖕𝖙 𝕭𝖚𝖎𝖑𝖉            ")		
    print("                                 ")		
    print("                𝖇𝖞               ")
    print("                                 ")		
    print("             {0}𝕵𝖎𝖒𝖌𝖘𝖊𝖞{1}".format(CYAN, NOC))		
    print("{0}                  ".format(BOLD))		
    print("*********************************")
    print("{0}".format(NOC)) 	
    
def telegram_bot_sendtext(bot_message):
    #Telegram msg Bot
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()       

if argn > 6:
	# Pass arguments to variables
	# This is with a conditional because if arguments are less than 7 the program would fail

    romname=sys.argv[1]
    sync=sys.argv[2]
    patch=sys.argv[3]
    build=sys.argv[4]
    upload=sys.argv[5]
    clean=sys.argv[6]
    
# Variable when you select rom
    ROM = romname.capitalize()
    ROMDIR="{0}/{1}".format(SCRIPTFOLDER,ROM)
    RIS = romname.upper()
    REP = "{0}LINK".format(RIS)
    ZOPO="{0}ZIP".format(RIS)
    
def setup():
        # Checks for no arguments
        if argn == 1:
            inis()
            print()
            print("Type 'python3 build.py {0}help{1}' for getting help".format(CYAN, NOC))
            print()
            ending()
            exit(1)
        # Checks for less than 6 arguments
        if argn < 6:
            # Checks for help argument
            if sys.argv[1] == "help":
                inis()
                print()
                print("{2}Usage{1}: python3 build.py {0}rom_name{1} {0}sync{1} {0}patch{1} {0}build{1} {0}upload{1} {0}clean{1} ".format(CYAN,  NOC, GREEN))
                print()
                print("                        {0} Name Roms  {1}                           ".format(BOLD, NOC))
                print(" _______________________________________________________ ")
                print("| {0}aicp{1}      | {0}aex{1}      | {0}altair{1}   | {0}aokp{1}     | {0}aoscp{1}     |".format(CYAN, NOC))
                print("| {0}aosip{1}     | {0}candy{1}    | {0}carbon{1}   | {0}citrus{1}   | {0}colt{1}      |".format(CYAN, NOC))
                print("| {0}corvus{1}    | {0}cosmic{1}   | {0}cosp{1}     | {0}crdroid{1}  | {0}derpfest{1}  |".format(CYAN, NOC))
                print("| {0}dot{1}       | {0}floko{1}    | {0}havoc{1}    | {0}ion{1}      | {0}lineage{1}   |".format(CYAN, NOC))
                print("| {0}lotus{1}     | {0}nitrogen{1} | {0}paranoid{1} | {0}reloaded{1} | {0}renouveau{1} |".format(CYAN, NOC))
                print("| {0}renouveau{1} | {0}revenge{1}  | {0}resurrectionremix{1}   | {0}stag{1}      |".format(CYAN, NOC))
                print("| {0}statix{1}    | {0}superior{1} | {0}viper{1}    |{0}xenon{1}     | {0}xtended{1}   |".format(CYAN, NOC))
                print()
                print(" {0}You could write this option:{1}".format(BOLD, NOC))
                print(" _________________________________________ ")
                print("| {2}Rom name:    | {0}read tablet (UP){1}           |".format(CYAN,  NOC, BOLD))
                print("| {2}Sync:        | {0}yes/no{1}                     |".format(CYAN,  NOC, BOLD))
                print("| {2}Patch;       | {0}yes/no/Gapps{1}               |".format(CYAN,  NOC, BOLD))
                print("| {2}Build:       | {0}yes/no{1}                     |".format(CYAN,  NOC, BOLD))	
                print("| {2}Upload:      | {0}yes/no{1}                     |".format(CYAN,  NOC, BOLD))
                print("| {2}Clean:       | {0}make/zip/delete/reset/no{1}   |".format(CYAN,  NOC, BOLD)) 
                print()
                print(" {0}Example{1}: python3 build.py {2}aicp yes yes yes yes no no{1}".format(GREEN, NOC, BOLD))
                ending()
                exit()
            else:
                print("You didn't entered enough arguments")
                print("Type 'python3 build.py {0}help{1}' for getting help".format(CYAN, NOC))
                telegram_bot_sendtext("Error in arguments {0}".format(INFOCLI))
                ending()
                exit(1)
    # Checks if the arguments are compatible
        if sys.argv[1] not in romlist:
            print("You didn't write a valid ROM")
            print("Be sure to write the same as in the help message")
            telegram_bot_sendtext("Error in arguments in Rom {0}".format(INFOCLI))
            ending()
            exit(1)
        if sys.argv[2] not in yesno:
            print("Your sync argument is not correct")
            print("Be sure to write the same as in the help message")
            telegram_bot_sendtext("Error in arguments in Sync {0}".format(INFOCLI))
            ending()
            exit(1)
        if sys.argv[3] not in patc:
            print("Your patch argument is not correct")
            print("Be sure to write the same as in the help message")
            telegram_bot_sendtext("Error in arguments in Patch {0}".format(INFOCLI))
            ending()
            exit(1)
        if sys.argv[4] not in yesno:
            print("Your build argument is not correct")
            print("Be sure to write the same as in the help message")
            telegram_bot_sendtext("Error in arguments in Build {0}".format(INFOCLI))
            ending()
            exit(1)
        if sys.argv[5] not in yesno:
            print("Your upload argument is not correct")
            print("Be sure to write the same as in the help message")
            telegram_bot_sendtext("Error in arguments in upload {0}".format(INFOCLI))
            ending(1)
            exit
        if sys.argv[6] not in clen:
            print("Your clean argument is not correct")
            print("Be sure to write the same as in the help message")
            telegram_bot_sendtext("Error in arguments in Clean {0}".format(INFOCLI))
            ending()
            exit(1)

def printconfig():
	# Prints the config for the build
        print("+++ Select ....... {0}{1}{2}     :android:".format(GREEN,ROM, NOC))
        #Use in buildkite to show emoji
        print()
        inis()
        print()
        print("******* {0}Commands{1} **********".format(GREEN,  NOC))
        print()
        if sys.argv[1] in romlist:
            print("{3}ROM    = {0}{1}{2}".format(CYAN, ROM, NOC, BOLD))
            r1="{0}Your command is: {0}{1}{2}".format(BOLD,  CYAN, ROM, NOC)
        if sync == "yes": 
            print("{3}SYNC   = {0}{1}{2}".format(GREEN, sync, NOC, BOLD))
            ra = "{0}{1}{2}".format(GREEN, sync, NOC)
        else:
            ra = "{0}{1}{2}".format(YELLOW, sync, NOC)
        if sys.argv[3] in princof: 
            print("{3}PATCH  = {0}{1}{2}".format(GREEN, patch, NOC, BOLD))
            re = "{0}{1}{2}".format(GREEN, patch, NOC)
        else:
            re = "{0}{1}{2}".format(YELLOW, patch, NOC)
        if build == "yes": 
            print("{3}BUID   = {0}{1}{2}".format(GREEN, build, NOC, BOLD))
            ri = "{0}{1}{2}".format(GREEN, build, NOC)
        else:
            ri = "{0}{1}{2}".format(YELLOW, build, NOC)
        if upload == "yes": 
            print("{3}UPLOAD = {0}{1}{2}".format(GREEN, upload, NOC, BOLD))
            ro = "{0}{1}{2}".format(GREEN, upload, NOC)
        else:
            ro = "{0}{1}{2}".format(YELLOW, upload, NOC)
        if sys.argv[6] in princof: 
            print("{3}CLEAN  = {0}{1}{2}".format(GREEN, clean, NOC, BOLD))
            ru = "{0}{1}{2}".format(GREEN, clean, NOC)
        else:
            ru = "{0}{1}{2}".format(YELLOW, clean, NOC)
        print()
        print("{0} {1} {2} {3} {4} {5}".format (r1, ra, re, ri, ro, ru))
        print()
        print("********** {0}End{1} ************".format(GREEN, NOC))    
        print()
        
def startfo():
    #Create folder
    if not os.path.isdir( SCRIPT ):
        print("Create Folder {0}".format(SCRIPT))
        os.mkdir( SCRIPT )
    #Create folder
    if not os.path.isdir( SCRIPTFOLDER ):
        print("Create Folder {0}".format(SCRIPTFOLDER))
        os.mkdir( SCRIPTFOLDER )
    #Create folder
    if not os.path.isdir( TOOL ):
        print("Create Folder {0}".format(TOOL))
        os.mkdir( TOOL )
    #Create folder
    if not os.path.isdir( TOOLTREE ):
        print("Create Folder {0}".format(TOOLTREE))
        os.mkdir( TOOLTREE )
    #Create folder
    if not os.path.isdir( TOOLROM ):
        print("Create Folder {0}".format(TOOLROM))
        os.mkdir( TOOLROM )
    #Create folder
    if not os.path.isdir( TOOLPATCH ):
        print("Create Folder {0}".format(TOOLPATCH))
        os.mkdir( TOOLPATCH )
    #Create folder
    if  not os.path.isdir( TOOLLOG ):
        print("Create Folder {0}".format(TOOLLOG))
        os.mkdir( TOOLLOG )
        os.mkdir( "{0}/upload".format(TOOLLOG) )
    
def romfolder():
    #Create folder to rom
    if os.path.isdir( ROMDIR ):
        print("{0}..................................!".format(YELLOW))
        print("{0}{1} folder exists".format(ROM, NOC))
        print("")
    else:
        print("{0}................................../{1}".format(GREEN, NOC))
        print("Create folder to {0}{1}{2}" .format(GREEN, ROM, NOC))
        print("")
        os.mkdir( ROMDIR )
    if os.path.isdir( "{0}/.repo/".format(ROMDIR) ):
        print("{0}..................................!".format(YELLOW))
        print("{0}{1} folder exists" .format(ROM,  NOC))
        print("")
    else:
        print("{0}................................../{1}".format(GREEN, NOC))
        print("Create folder to {0}{1}{2}" .format(GREEN, ROM, NOC))
        print("")
        os.chdir ( ROMDIR )
        OSC = ROMSI.get('{0}'.format(REP))  
        cmd =  "repo init -u {0}".format(OSC) 
        os.system(cmd)

def syncrom():
    #Sync the rom  
    if sync == "yes":
        print("--- Sync ......... {0}{1}{2}  :flowtype:".format(CYAN,ROM, NOC))
        #Use in buildkite to show emoji
        print()
        romfolder()
        os.system("bash {0}/telegram.sh sync1 {1} {2} {3} {4}".format(TOOL, ROM,  TOOLLOG, bot_chatID, bot_token))
        print("{0}................................../{1}".format(GREEN, NOC))
        print("Start sync {0}{1}{2}".format(GREEN, ROM, NOC))
        print("")
        os.chdir ( ROMDIR )
        os.system("repo sync -q --force-sync --no-clone-bundle --no-tags -j$(nproc --all)")
        print("{0}..................................|{1}".format(YELLOW, NOC))
        print("Finish sync {0}{1}{2}".format(YELLOW, ROM, NOC))
        print("")
        os.system("bash {0}/telegram.sh sync2 {1} {2} {3} {4}".format(TOOL, ROM,  TOOLLOG, bot_chatID, bot_token))
    elif sync == "no":
        print("{0}..................................!{1}".format(YELLOW, NOC))
        print("Skip sync {0}{1}{2}".format(YELLOW, ROM, NOC))
        print("")

def patchrom():
    #Path rom
    if patch == "yes":
        if romname == "aicp":
            cms = "cp -r {0}/{1}/updater/strings.xml         {2}/packages/apps/Updater/res/values".format(TOOLPATCH, ROM, ROMDIR)
            os.system(cms)
            print("{0}................................../{1}".format(GREEN, NOC))
            print("Patching {0}{1}{2}".format(GREEN, ROM, NOC))
            print("") 
        elif romname == "paranoid":
            cms = "cp -r {0}/Paranoid/         {1}".format(TOOLPATCH, ROMDIR)
            os.system(cms)
            print("{0}................................../{1}".format(GREEN, NOC))
            print("Patcing {0}{1}{2}".format(GREEN, ROM, NOC))
            print("")
    elif patch == "gapps":
        print("{0}................................../{1}".format(GREEN, NOC))
        print("Patching {0}{1}{2} with Gapps".format(GREEN, ROM, NOC))
        print("")
        cms = "cp -r {0}/Gapps/*         {1}".format(TOOLPATCH, ROMDIR)
        os.system(cms)
    elif patch == "no":
        print("{0}..................................!{1}".format(YELLOW, NOC))
        print("Skip patch {0}{1}{2}".format(YELLOW, ROM, NOC))
        print("")

def copytrees():
    #Function copy DT
    if os.path.isdir( "{0}/device/{1}".format(ROMDIR,DEVICES)):
        print("{0}..................................!".format(YELLOW))
        print("DT{0} already exists".format(NOC))
        print("")
    else:
        print("{0}................................../{1}".format(GREEN, NOC))
        print("Copying {0}DT{1}".format(GREEN, NOC))
        print("")
    cms = "cp -r {0}/{1}/         {2}".format(TOOLTREE,ROM,SCRIPTFOLDER)
    os.system(cms)
    #Function copy VT
    if os.path.isdir("{0}/vendor/{1}".format(ROMDIR,DEVICES)):
        print("{0}..................................!".format(YELLOW))
        print("vt{0} already exists".format(NOC))
        print("")
    else:
        print("{0}................................../{1}".format(GREEN, NOC))
        print("Copying {0}VT{1}".format(GREEN, NOC))
        print("")
        cms = "cp -r {0}/Common/vendor         {1}".format(TOOLTREE,ROMDIR)
        os.system(cms)
    #Function copy KT
    if os.path.isdir( "{0}/kernel/{1}".format(ROMDIR, DEVICES)):
        print("{0}..................................!".format(YELLOW))
        print("KT{0} already exists".format(NOC))
        print("")
    else:
        print("{0}................................../{1}".format(GREEN, NOC))
        print("Copying {0}KT{1}".format(GREEN, NOC))
        print("")
        cms = "cp -r {0}/Common/kernel/         {1}".format(TOOLTREE,ROMDIR)
        os.system(cms)
    
def buildrom():
    if build == "yes":
        print("--- Build ........ {0}{1}{2}  :building_construction:".format(CYAN,ROM, NOC))
        #Use in buildkite to show emoji
        print()
        copytrees()
        print("{0}................................../{1}".format(GREEN, NOC))
        print("Start to build {0}{1}{2}".format(GREEN, ROM, NOC))
        print("")
        os.system("bash {0}/telegram.sh build1 {1} {2} {3} {4}".format(TOOL, ROM,  TOOLLOG, bot_chatID, bot_token))
        os.chdir ( ROMDIR )
        #Cloning Lineage Setting
        if os.path.isdir( "packages/resources/devicesettings" ):
            print("Already exists Setting")
        else:
            print("Cloning Setting")
            cmd="git clone -b lineage-16.0 https://github.com/LineageOS/android_packages_resources_devicesettings packages/resources/devicesettings"
            os.system(cmd)
        if romname == "aicp":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0} -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "aex":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch aosp_{0} && mka aex -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "altair":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch altair_{0} -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "aokp":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch aokp_{0} && mkarainbowfarts  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "aoscp":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch aoscp_{0}  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "arrow":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "bootleggers":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch bootleg_{0}  && mka bacon -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "candy":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "carbon":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch carbon_{0}  && make carbon  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "citrus":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch citrus_{0}  && mka lemonade -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "colt":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch colt_{0}  && make colt  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "corvus":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch du_{0}  && make corvus  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "cosmic":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch cos_{0}  && brunch {0}  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu,  CORE, TOOLLOG, ROM)
        if romname == "cosp":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch cosp_{0}  && mka bacon   -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "crdroid":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "derpfest":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch aosip_{0}  && mka kronic  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "dot":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch dot_{0}  &&  make bacon  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "floko":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "havoc":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  > {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "ion":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch ion_{0} &&  mka bacon  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "lineage":
            cmd="/bin/bash -c 'source build/envsetup.sh && breakfast {0} && brunch {0} -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "lotus":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch lotus_{0}  && make bacon   -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "nitrogen":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch nitrogen_{0}  && make -j{1} otapackge  > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "paranoid":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch pa_{0}  && ./rom-build.sh  > {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "reloaded":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch reloaded_{0}  && make reloaded  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "renouveau":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "revenge":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch revengeos_{0}  && make -j{1} bacon > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "resurrectionremix":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "stag":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch stag_{0}  && make stag  > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "statix":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "superior":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch superior_{0}  && mka bacon  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "viper":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch viper_{0}  && mka poison   -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "xenon":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "xtended":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch xtended_{0}  && make xtended    -j{1} > {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        os.system(cmd) 
        #save log to upload in buildkite
        cml="rm -rf {0}/upload/*.log && cp -r {0}/buil-{1}.log  {0}/upload".format(TOOLLOG, ROM)
        os.system(cml)
        with open("/tmp/buildexitcode.txt") as f:
            exitstatus=f.readlines()
        print("Build exit status code is: ",exitstatus[0])
        print("")
        if "1" in exitstatus[0]:
            print("{0}..................................0".format(RED))
            print("Build failed{0}".format(NOC))
            print("")
            os.system("bash {0}/telegram.sh build2 {1} {2} {3} {4}".format(TOOL, ROM,  TOOLLOG, bot_chatID, bot_token))
            ending()
            exit(1)
        if "2" in exitstatus[0]:
            print("{0}..................................0".format(RED))
            print("Build failed{0}".format(NOC))
            print("")
            os.system("bash {0}/telegram.sh build2 {1} {2} {3} {4}".format(TOOL, ROM,  TOOLLOG, bot_chatID, bot_token))
            ending
            exit(1)
        if "0" in exitstatus[0]:
            print("{0}..................................|".format(YELLOW))
            print("Build completed succesfully{0}".format(NOC))
            print("")
            os.system("bash {0}/telegram.sh build3 {1} {2} {3} {4}".format(TOOL, ROM,  TOOLLOG, bot_chatID, bot_token))
            print("{0}................................../".format(GREEN))
            print("Copying {0}{1} to {2}{3}".format(GREEN, ROM,TOOLROM, NOC))
            print("")
            OSC = ROMZI.get('{0}'.format(ZOPO))  
            cmd="cp -r {0}/{1}/{2}         {3}".format(ROMDIR, OUTF,OSC,TOOLROM)
            os.system(cmd)
    elif build == "no":
            print("{0}..................................!{1}".format(YELLOW, NOC))
            print("Skip build {0}{1}{2}".format(YELLOW, ROM, NOC))
            print("")

def uploadrom():
    #Upload rom
        if upload == "yes":
            print("--- Upload ....... {0}{1}{2}  :packagecloud:".format(CYAN,ROM, NOC))
            #Use in buildkite to show emoji
            print()
            print("{0}................................../{1}".format(GREEN, NOC))
            print("Uploading {0}{1}{2}".format(GREEN, ROM, NOC))
            print("")
            os.chdir ( TOOLROM )       
            os.system("bash {0}/telegram.sh upload1 {1} {2} {3} {4}".format(TOOL, ROM,  TOOLLOG, bot_chatID, bot_token))
            OSC = ROMZI.get('{0}'.format(ZOPO)) 
            cmd = "scp {0}/{1}    {2}{3}/".format(TOOLROM,OSC,LINKUPL,ROM) 
            os.system(cmd)           
            for file in glob.glob("{0}".format(OSC)):
                    FILENAME=file
                    UPDATE_URL = "{0}/{1}/{2}".format(LINKSOU, ROM, FILENAME)
            print("{0}..................................|{1}".format(YELLOW, NOC))
            print("Uploaded {0}{1}{2}".format(YELLOW, ROM, NOC))
            print("")
            time = datetime.now()
            DATE = time.strftime("%Y-%m-%d %H:%M")
            telegram_bot_sendtext("Uploaded {0} Link: {1} Date {2} {3}".format(ROM, UPDATE_URL, DATE, INFOCLI))
        elif upload == "no":
            print("{0}..................................!{1}".format(YELLOW, NOC))
            print("Skip upload {0}{1}{2}".format(YELLOW, ROM, NOC))
            print("")

def romclean():
    #Function to clean
        if clean == "make":
            print("--- Finish ....... {0}{1}{2}  :amazon-clouddirectory:".format(CYAN,ROM, NOC))
            #Use in buildkite to show emoji
            print()
            print("{0}................................../{1}".format(GREEN, NOC))
            print("Make clean {0}{1}{2}".format(GREEN, ROM, NOC))
            print("")
            os.chdir ( ROMDIR )
            os.system("make clean")
        elif clean == "zip":
            print("--- Finish ....... {0}{1}{2}  :amazon-clouddirectory:".format(CYAN,ROM, NOC))
            print()
            print("{0}................................../{1}".format(GREEN, NOC))
            print("Delete folder {0}{1}{2}".format(GREEN, ROM, NOC))
            print("")
            os.system("rm -rf {0}/{1}/*.zip".format(ROMDIR, OUTF))
        elif clean == "delete":
            print("--- Finish ....... {0}{1}{2}  :amazon-clouddirectory:".format(CYAN,ROM, NOC))
            print()
            print("{0}................................../{1}".format(GREEN, NOC))
            print("Delete folder {0}{1}{2}".format(GREEN, ROM, NOC))
            print("")
            os.chdir ( ROMDIR )
            shutil.rmtree("ROM")
        elif clean == "reset":
            print("--- Finish ....... {0}{1}{2}  :amazon-clouddirectory:".format(CYAN,ROM, NOC))
            print()
            os.chdir ( ROMDIR )
            os.system("find ./  -mindepth 1 ! -regex '^./.repo\(/.*\)?' -delete")              
            print("{0}................................../{1}".format(GREEN, NOC))
            print("Delete folder to {0}{1}{2} except .repo ".format(GREEN, ROM, NOC))
            print("")
        elif clean == "no":
            print("{0}..................................!".format(YELLOW))
            print("Nothing {0} to do".format(NOC))
            print("")
            
def ending():
    time.sleep(5)
    print("{0}".format(BOLD))
    print("**********************************")
    print("")
    print("   Thanks to use Script Build    ")  
    print("") 
    print("")  
    print(" It was created for true {0}BuildBot{1}".format(CYAN, NOC))	
    print("{0}".format(BOLD)) 	
    print("**********************************")
    print("              * *")	
    print("               *")	
    print("")	
    print("            Contact:")
    print("")		
    print(" My Telegram:{0}http://t.me/Jimgsey {1}".format(CYAN, NOC))		
    print("")		
    print(" {0}My Github:{1} https://github.com/jimgsey{2}".format(BOLD, CYAN, NOC))
    print("")
    print(" {0}Source code:{1} https://github.com/jimgsey/Script_Build{2}".format(BOLD, CYAN, NOC))
    print("")

  
# Execute functions
setup()
printconfig()
startfo()
syncrom()
patchrom()
buildrom() 
uploadrom()
romclean()
ending()
