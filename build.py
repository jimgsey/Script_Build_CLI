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
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import escape_markdown

################################################
#Colour
RED = '\033[1;31m'
CYAN = '\033[1;36m'
YELLOW = '\033[1;33m'
GREEN = '\033[1;32m'
NOC = '\033[0;0m'
BOLD = '\033[1m'

# Generic variables
argn=len(sys.argv)
romlist=["aicp",  "aex",  "altair",  "aokp",  "aoscp",  "aosip",  "baikal",  "candy",  "carbon",  "citrus",  "colt",  "corvus",  "cosmic",  "cosp",  "crdroid",  "derpfest",  "dot", "durex", "evolution", "floko", "gzosp", "havoc",  "ion",  "lineage",  "liquidremix", "lotus",  "nitrogen",  "omnirom", "paranoid", "pixel", "pixy", "posp",  "reloaded", "renouveau",  "revenge",  "resurrectionremix",  "stag",  "statix",  "superior", "syberia",  "viper",  "xenon",  "xtended"]
clen=["make", "delete", "no", "reset", "zip"]
patc=["yes", "no", "gapps"]
yesno=["yes","no"]
princof=["make", "delete","yes", "gapps", "reset", "zip"]
device="lavender"
deviceu="lavender-userdebug"
## Device Default structure
DEVICES = "xiaomi/lavender"
##Change with your CPU
CORE=os.popen("nproc --all").read()
############## CLI Setting ####################
# You could add your link to CLI, that way, you could see the process when a message is sent for example to your server:https://buildkite.com/jimgsey/ or your web: https://jimgsei.github.io.
LINKCLI = "http://jimgsei.github.io"
INFOCLI = "🔗 CLI: {0}".format(LINKCLI)
# Your link server generate. For example Sourceforge: https://sourceforge.net/projects/lavender7/files
LINKSOU = "https://sourceforge.net/projects/lavender7/files"
# Your link account to upload. For example: jim15@frs.sourceforge.net:/home/frs/project/
LINKUPL = "jim15@frs.sourceforge.net:/home/frs/project/lavender7/"

#Telegram bot setting 
bot_token = ''
bot_chatID = ''
bot = telegram.Bot(token=bot_token)

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
#List repo url to roms 
ROMSI = {
'AICPLINK' : 'https://github.com/AICP/platform_manifest.git -b p9.0', 
'AEXLINK' :  'https://github.com/AospExtended/manifest.git -b 9.x', 
'ALTAIRLINK' : 'https://github.com/AltairROM/android -b p', 
'AOKPLINK' : 'https://github.com/AOKP/platform_manifest.git -b pie', 
'AOSIPLINK' : 'https://github.com/AOSiP/platform_manifest.git -b pie', 
'ARROWLINK' : 'https://github.com/ArrowOS/android_manifest.git -b arrow-9.x',
'BAIKALLINK' : 'https://github.com/baikalos/manifest.git -b pi',
'BOOTLEGGERSLINK' : 'https://github.com/BootleggersROM/manifest.git -b pasta',
'CANDYLINK' : 'https://github.com/CandyRoms/candy.git -b c9.0', 
'CARBONLINK' : 'https://github.com/CarbonROM/android.git -b cr-7.0 ', 
'COLTLINK' : 'https://github.com/Colt-Enigma/platform_manifest.git -b wip', 
'CORVUSLINK' : 'https://github.com/du-rex/android_manifest.git -b p9x-caf', 
'COSMICLINK' : 'https://github.com/Cosmic-OS/platform_manifest.git -b corona-release', 
'COSPLINK' : 'https://github.com/cosp-project/manifest -b pie', 
'CRDROIDLINK' : 'https://github.com/crdroidandroid/android.git -b 9.0', 
'DERPFESTLINK' : 'https://github.com/DerpFest-Pie/platform_manifest.git -b pie', 
'DOTLINK' : 'https://github.com/DotOS/manifest.git -b dot-p', 
'DUREXLINK' : 'https://github.com/du-rex/android_manifest.git -b p9x-caf',
'EVOLUTIONLINK' : 'https://github.com/Evolution-X-Legacy/platform_manifest -b pie', 
'FLOKOLINK' : 'https://github.com/FlokoROM/manifesto.git -b 9.0', 
'GZOSPLINK' : 'https://github.com/GZOSP/manifest.git -b 9.0', 
'HAVOCLINK' : 'https://github.com/Havoc-OS/android_manifest.git -b pie', 
'IONLINK' : 'https://github.com/i-o-n/manifest -b pie', 
'LINEAGELINK' : 'https://github.com/LineageOS/android.git -b lineage-16.0', 
'LOTUSLINK' : 'https://github.com/LotusOS/android_manifest.git -b pie', 
'LIQUIDREMIXLINK' : 'https://github.com/LiquidRemix/android_manifest.git -b pie', 
'NITROGENLINK' : 'https://github.com/nitrogen-project/android_manifest.git -b p', 
'OMNIROMLINK' : 'https://github.com/omnirom/android.git -b android-9.0', 
'PARANOIDLINK' : 'https://github.com/AOSPA/manifest -b pie', 
'PIXELLINK' : 'https://github.com/PixelExperience/manifest -b pie',
'PIXYLINK' : 'https://github.com/PixysOS/manifest -b pie', 
'POSPLINK' : 'https://github.com/PotatoProject/manifest -b baked-release', 
'RELOADEDLINK' : 'https://github.com/ReloadedOS/android_manifest.git -b pie', 
'RENOUVEAULINK' : 'https://github.com/RenouveauOS/android.git -b renouveau-9.0', 
'REVENGELINK' : 'https://github.com/RevengeOS/android_manifest -b r9.0-caf', 
'RESURRECTIONREMIXLINK' : 'https://github.com/RR-Test/platform_manifest.git -b test_pie', 
'STAGLINK' : 'https://github.com/StagOS/manifest.git -b p9', 
'STATIXLINK' : 'https://github.com/StatiXOS/android_manifest.git -b 9-caf',
'SUPERIORLINK' : 'https://github.com/SuperiorOS/manifest.git -b pie',
'SYBERIALINK' : 'https://github.com/syberia-project/manifest.git -b 9.0',
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
'BAIKALZIP' : 'Baikal*.zip',
'BOOTLEGGERSZIP' : 'BootleggersROM-Pie*.zip',
'CANDYZIP' : 'Candy*.zip', 
'CARBONZIP' : 'CARBON*.zip', 
'COLTZIP' : 'ColtOS*.zip', 
'CORVUSZIP' : 'Cor*.zip', 
'COSMICZIP' : 'Cosmic-OS-v4.0-Corona*.zip', 
'COSPZIP' : 'COSP*.zip', 
'CRDROIDZIP' : 'crDroidAndroid-9*.zip', 
'DERPFESTZIP' : 'AOSiP-9.0-DerpFest*.zip', 
'DUREXZIP' : 'du_lavender*.zip', 
'DOTZIP' : 'dotOS-P*.zip', 
'EVOLUTIONZIP' : 'evolution*.zip',
'FLOKOZIP' : 'Floko*.zip', 
'GZOSPZIP' : 'Gzosp*.zip', 
'HAVOCZIP' : 'Havoc*.zip', 
'IONZIP' : 'ion*.zip', 
'LINEAGEZIP' : 'lineage-16*.zip', 
'LOTUSZIP' : 'Lo*.zip', 
'LIQUIDREMIXZIP' : 'Liqui*.zip',
'NITROGENZIP' : 'Nitrogen*.zip', 
'OMNIROMZIP' : 'omni-*.zip', 
'PARANOIDZIP' : 'Pa*.zip', 
'PIXELZIP' : 'PixelExperience_lavender*.zip',
'PIXYZIP' : 'PixysOS*.zip', 
'POSPZIP' : 'potato_lavender-9*.zip', 
'RELOADEDZIP' : 'Reloaded-9.0*.zip', 
'RENOUVEAUZIP' : 'Reno*.zip', 
'REVENGEZIP' : 'RevengeOS*.zip', 
'RESURRECTIONREMIXZIP' : 'RR-P-v7*.zip', 
'STAGZIP' : 'stag_lavender_p*.zip', 
'STATIXZIP' : 'statix*.zip', 
'SUPERIORZIP' : 'su*.zip', 
'SYBERIAZIP' : 'syberia_lavender-v*.zip',
'VIPERZIP' : 'Viper*.zip', 
'XENONZIP' : 'XenonHD*.zip', 
'XTENDEDZIP' : 'Xtended*.zip', 
}
#####################################################

    
def inis():
    #Start show script name
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
    
def send_text(output):
    #Send notification with button
    button_list = [[
        InlineKeyboardButton(text="My server", url="https://jimgsei.github.io/")
    ]]
    reply_markup = InlineKeyboardMarkup(button_list)
    sent_message = bot.sendMessage(
        chat_id=bot_chatID,
        text=output,
        parse_mode=telegram.ParseMode.MARKDOWN,
        reply_markup=reply_markup
    )
    return sent_message

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
                print(" _______________________________________________________̣̣__________ ")
                print("| {0}aicp{1}      | {0}aex{1}      | {0}altair{1}    | {0}aokp{1}     | {0}aoscp{1}             |".format(CYAN, NOC))
                print("| {0}aosip{1}     | {0}candy{1}    | {0}carbon{1}    | {0}citrus{1}   | {0}colt{1}              |".format(CYAN, NOC)) 
                print("| {0}corvus{1}    | {0}cosmic{1}   | {0}cosp{1}      | {0}crdroid{1}  | {0}evolution{1}         |".format(CYAN, NOC))
                print("| {0}derpfest{1}  | {0}dot{1}      | {0}floko{1}     | {0}havoc{1}    | {0}ion{1}               |".format(CYAN, NOC))
                print("| {0}lineage{1}   | {0}lotus{1}    | {0}nitrogen{1}  | {0}omnirom{1}  | {0}paranoid{1}          |".format(CYAN, NOC))
                print("| {0}pixy{1}      | {0}reloaded{1} | {0}renouveau{1} | {0}revenge{1}  | {0}resurrectionremix{1} |".format(CYAN, NOC))
                print("| {0}stag{1}      | {0}statix{1}   | {0}superior{1}  | {0}viper{1}    | {0}xenon{1}             |".format(CYAN, NOC))
                print("| {0}xtended{1}   |".format(CYAN, NOC))
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
                print(" ⚡ You didn't entered enough arguments")
                print("Type 'python3 build.py {0}help{1}' for getting help".format(CYAN, NOC))
                telegram_bot_sendtext(" ⚡ Error in arguments {0}".format(INFOCLI))
                ending()
                exit(1)
    # Checks if the arguments are compatible
        if sys.argv[1] not in romlist:
            print(" ⚡ You didn't write a valid ROM")
            print("Be sure to write the same as in the help message")
            send_text(" ⚡ Error in arguments in Rom name")
            ending()
            exit(1)
        if sys.argv[2] not in yesno:
            print(" ⚡ Your sync argument is not correct")
            print("Be sure to write the same as in the help message")
            send_text(" ⚡ Error in arguments in Sync")
            ending()
            exit(1)
        if sys.argv[3] not in patc:
            print(" ⚡ Your patch argument is not correct")
            print("Be sure to write the same as in the help message")
            send_text(" ⚡ Error in arguments in Patch")
            ending()
            exit(1)
        if sys.argv[4] not in yesno:
            print(" ⚡ Your build argument is not correct")
            print("Be sure to write the same as in the help message")
            send_text(" ⚡ Error in arguments in Build")
            ending()
            exit(1)
        if sys.argv[5] not in yesno:
            print(" ⚡ Your upload argument is not correct")
            print("Be sure to write the same as in the help message")
            send_text(" ⚡ Error in arguments in Upload")
            ending(1)
            exit
        if sys.argv[6] not in clen:
            print(" ⚡ Your clean argument is not correct")
            print("Be sure to write the same as in the help message")
            send_text(" ⚡ Error in arguments in Clean")
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
        #Show only yuor "yes" or "custom" setting, not show negattive commands.
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
        #You can see your choose witch colour in 1 line
        print("{0} {1} {2} {3} {4} {5}".format (r1, ra, re, ri, ro, ru))
        print()
        print("********** {0}End{1} ************".format(GREEN, NOC))    
        print()
        
def startfo():
    #Create folder  "home/user/Android"
    if not os.path.isdir( SCRIPT ):
        print(" 📂 Create Folder {0}".format(SCRIPT))
        os.mkdir( SCRIPT )
    #Create folder  "home/user/Android/Builds"
    if not os.path.isdir( SCRIPTFOLDER ):
        print(" 📂 Create Folder {0}".format(SCRIPTFOLDER))
        os.mkdir( SCRIPTFOLDER )
    #Create folder  "home/user/Android/Tools"
    if not os.path.isdir( TOOL ):
        print(" 📂 Create Folder {0}".format(TOOL))
        os.mkdir( TOOL )
    #Create folder  "home/user/Android/Tools/Tree"
    if not os.path.isdir( TOOLTREE ):
        print(" 📂 Create Folder {0}".format(TOOLTREE))
        os.mkdir( TOOLTREE )
    #Create folder  "home/user/Android/Tools/Rom"
    if not os.path.isdir( TOOLROM ):
        print(" 📂 Create Folder {0}".format(TOOLROM))
        os.mkdir( TOOLROM )
    #Create folder  "home/user/Android/Tools/Patch"
    if not os.path.isdir( TOOLPATCH ):
        print(" 📂 Create Folder {0}".format(TOOLPATCH))
        os.mkdir( TOOLPATCH )
    #Create folder  "home/user/Android/Tools/Log"
    if  not os.path.isdir( TOOLLOG ):
        print(" 📂 Create Folder {0}".format(TOOLLOG))
        os.mkdir( TOOLLOG )
        #Create folder  "home/user/Android/Tools/Log/upload"
        os.mkdir( "{0}/upload".format(TOOLLOG) )
    
def romfolder():
    #Create folder  "home/user/Android/Build/name_rom"
    if os.path.isdir( ROMDIR ):
        print("{0}..................................!".format(YELLOW))
        print("{0}{1} 📂 folder exists".format(ROM, NOC))
        print("")
    else:
        print("{0}................................../{1}".format(GREEN, NOC))
        print(" 📂 Create folder to {0}{1}{2}" .format(GREEN, ROM, NOC))
        print("")
        os.mkdir( ROMDIR )
    #Create folder  .repo  in "home/user/Android/Builds/name_rom" 
    if os.path.isdir( "{0}/.repo/".format(ROMDIR) ):
        print("{0}..................................!".format(YELLOW))
        print("{0}{1} 📂 folder exists" .format(ROM,  NOC))
        print("")
    else:
        print("{0}................................../{1}".format(GREEN, NOC))
        print(" 📂 Create folder to {0}{1}{2}" .format(GREEN, ROM, NOC))
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
        time = datetime.now()
        DATE = time.strftime("%Y-%m-%d %H:%M")
        send_text("📂 Start sync {0} \n⌚ {1}".format(ROM, DATE))
        #Telegram notification
        print("{0}................................../{1}".format(GREEN, NOC))
        print(" 📥 Start sync {0}{1}{2}".format(GREEN, ROM, NOC))
        print("")
        os.chdir ( ROMDIR )
        os.system("repo sync -q --force-sync --no-clone-bundle --no-tags -j$(nproc --all)")
        print("{0}..................................|{1}".format(YELLOW, NOC))
        print(" 📦 Finish sync {0}{1}{2}".format(YELLOW, ROM, NOC))
        print("")
        time = datetime.now()
        DATE = time.strftime("%Y-%m-%d %H:%M")
        send_text("🗄 Finish sync {0} \n⌚ {1}".format(ROM, DATE))
    elif sync == "no":
        print("{0}..................................!{1}".format(YELLOW, NOC))
        print("Skip sync {0}{1}{2}".format(YELLOW, ROM, NOC))
        print("")

def patchrom():
    #Path rom
    if patch == "yes":
        if romname == "aicp":
            #Add custon OTA
            os.system( "cp -r {0}/{1}/updater/strings.xml         {2}/packages/apps/Updater/res/values".format(TOOLPATCH, ROM, ROMDIR))
            print("{0}................................../{1}".format(GREEN, NOC))
            print(" 📋 Patching {0}{1}{2}".format(GREEN, ROM, NOC))
            print("") 
        elif romname == "paranoid":
            #Add custom folder
            os.system("cp -r {0}/Paranoid/         {1}".format(TOOLPATCH, ROMDIR))
            print("{0}................................../{1}".format(GREEN, NOC))
            print(" 📋 Patcing {0}{1}{2}".format(GREEN, ROM, NOC))
            print("")
    elif patch == "gapps":
        #Add gapps
        print("{0}................................../{1}".format(GREEN, NOC))
        print(" 📋 Patching {0}{1}{2} with Gapps".format(GREEN, ROM, NOC))
        print("")
        os.system("cp -r {0}/Gapps/*         {1}".format(TOOLPATCH, ROMDIR))
    elif patch == "no":
        print("{0}..................................!{1}".format(YELLOW, NOC))
        print("Skip patch {0}{1}{2}".format(YELLOW, ROM, NOC))
        print("")

def copytrees():
    #Copy DT
    if os.path.isdir( "{0}/device/{1}".format(ROMDIR, DEVICES)):
        print("{0}..................................!{1}".format(YELLOW, NOC))
        print(" 🗃 {0}DT{1} already exists".format(YELLOW, NOC))
        print("")
    else:
        print("{0}................................../{1}".format(GREEN, NOC))
        print(" 📂 Copying {0}DT{1}".format(GREEN, NOC))
        print("")
    os.system( "cp -r {0}/{1}/         {2}".format(TOOLTREE, ROM, SCRIPTFOLDER))
    #Copy VT
    if os.path.isdir("{0}/vendor/{1}".format(ROMDIR, DEVICES)):
        print("{0}..................................!{1}".format(YELLOW,  NOC))
        print(" 🗃 {0}VT{1} already exists".format(YELLOW, NOC))
        print("")
    else:
        print("{0}................................../{1}".format(GREEN, NOC))
        print(" 📂 Copying {0}VT{1}".format(GREEN, NOC))
        print("")
        os.system("cp -r {0}/Common/vendor         {1}".format(TOOLTREE,ROMDIR))
    #Copy KT
    if os.path.isdir( "{0}/kernel/{1}".format(ROMDIR, DEVICES)):
        print("{0}..................................!{1}".format(YELLOW, NOC))
        print(" 🗃 {0}KT{1} already exists".format(YELLOW, NOC))
        print("")
    else:
        print("{0}................................../{1}".format(GREEN, NOC))
        print(" 📂 Copying {0}KT{1}".format(GREEN, NOC))
        print("")
        os.system("cp -r {0}/Common/kernel/         {1}".format(TOOLTREE,ROMDIR))
    
def buildrom():
    if build == "yes":
        print("--- Build ........ {0}{1}{2}  :building_construction:".format(CYAN,ROM, NOC))
        #Use in buildkite to show emoji
        print()
        copytrees()
        print("{0}................................../{1}".format(GREEN, NOC))
        print(" 💻 Start to build {0}{1}{2}".format(GREEN, ROM, NOC))
        print("")        
        #Telegram notification
        time = datetime.now()
        DATE = time.strftime("%Y-%m-%d %H:%M")
        send_text("💻 Start to build {0} \n⌚ {1}".format(ROM, DATE))
        os.chdir ( ROMDIR )
        #Cloning Lineage Setting
        if os.path.isdir( "packages/resources/devicesettings" ):
            print("Already exists Setting")
        else:
            print("Cloning Setting")
            os.system("git clone -b lineage-16.0 https://github.com/LineageOS/android_packages_resources_devicesettings packages/resources/devicesettings")        
        if romname == "aex":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch aosp_{0} && mka aex -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "aicp":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0} | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "altair":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch altair_{0} -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "aokp":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch aokp_{0} && mkarainbowfarts  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, TOOLLOG, ROM)
        if romname == "aoscp":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch aoscp_{0}  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, TOOLLOG, ROM)
        if romname == "aosip":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch aosip_{0} && mka kronic | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, TOOLLOG, ROM)
        if romname == "arrow":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "baikal":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch baikalos_{0} && make -j{1} otapackage | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "bootleggers":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch bootleg_{0}  && mka bacon -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "candy":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  -j{1} | tee {2}/build-{3}.log; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "carbon":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch carbon_{0}  && make carbon  -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "citrus":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch citrus_{0}  && mka lemonade -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "colt":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch colt_{0}  && make colt  -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "corvus":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch du_{0}  && make corvus  -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "cosmic":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch cos_{0}  && brunch {0}  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, TOOLLOG, ROM)
        if romname == "cosp":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch cosp_{0}  && mka bacon   -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "crdroid":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "derpfest":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch aosip_{0}  && mka kronic  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, TOOLLOG, ROM)
        if romname == "dot":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch dot_{0}  &&  make bacon  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, TOOLLOG, ROM) 
        if romname == "durex":
            cmd="/bin/bash -c 'source build/envsetup.sh && breakfast {0} && mka bacon | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "evolution":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch aosp_{0}  &&  mka bacon  -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)    
        if romname == "floko":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "gzosp":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "havoc":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  | tee {1}/build-{2}.log; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "ion":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch ion_{0} &&  mka bacon  -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "lineage":
            cmd="/bin/bash -c 'source build/envsetup.sh && breakfast {0} && brunch {0} | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "lotus":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch lotus_{0}  && make bacon   -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "nitrogen":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch nitrogen_{0}  && make -j{1} otapackge  | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "omnirom":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "paranoid":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch pa_{0}  && ./rom-build.sh  | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "pixel":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch aosp_{0}  && mka bacon -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "pixy":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch pixys_{0}  && make pixys -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "posp":
            cmd="/bin/bash -c 'source build/envsetup.sh && add_lunch_combo potato_{0}  && brunch {0} | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu,  TOOLLOG, ROM)
        if romname == "reloaded":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch reloaded_{0}  && make reloaded  -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "renouveau":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, CORE, TOOLLOG, ROM)
        if romname == "revenge":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch revengeos_{0}  && make -j{1} bacon | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "resurrectionremix":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "stag":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch stag_{0}  && make stag  | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "statix":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0}  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "superior":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch superior_{0}  && mka bacon  -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "syberia":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch syberia_{0}  && make bacon  | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, TOOLLOG, ROM)
        if romname == "viper":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch viper_{0}  && mka poison   -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        if romname == "xenon":
            cmd="/bin/bash -c 'source build/envsetup.sh && brunch {0} | tee {1}/build-{2}.log ; echo $? > /tmp/buildexitcode.txt '".format(device, TOOLLOG, ROM)
        if romname == "xtended":
            cmd="/bin/bash -c 'source build/envsetup.sh && lunch xtended_{0}  && make xtended    -j{1} | tee {2}/build-{3}.log ; echo $? > /tmp/buildexitcode.txt '".format(deviceu, CORE, TOOLLOG, ROM)
        os.system(cmd) 
        #save log to upload in buildkite
        os.system("rm -rf {0}/upload/*.log && cp -r {0}/build-{1}.log  {0}/upload".format(TOOLLOG, ROM))
        with open("/tmp/buildexitcode.txt") as f:
            exitstatus=f.readlines()
        print("Build exit status code is: ",exitstatus[0])
        print("")
        if "1" in exitstatus[0]:
            print("{0}..................................0{1}".format(RED,  NOC))
            print(" ⛈  Build {0}failed{1}".format(RED, NOC))
            print("")
            time = datetime.now()
            DATE = time.strftime("%Y-%m-%d %H:%M")
            with open('{0}/upload/build-{1}.log'.format(TOOLLOG, ROM), 'rb') as document_file:
                MESSAGE=" ⛈ Error building {0} \n⌚ {1} \n{2}".format(ROM, DATE, INFOCLI )
                bot.send_document(chat_id=bot_chatID,  document=document_file,  caption=MESSAGE,  timeout=1000)
            ending()
            exit(1)
        if "2" in exitstatus[0]:
            print("{0}..................................0{1}".format(RED,  NOC))
            print(" ⛈  Build {0}failed{1}".format(RED, NOC))
            print("")
            with open('{0}/upload/build-{1}.log'.format(TOOLLOG, ROM), 'rb') as document_file:
                MESSAGE="⛈ Error building {0} \n⌚ {1} \n{2}".format(ROM, DATE, INFOCLI )
                bot.send_document(chat_id=bot_chatID,  document=document_file,  caption=MESSAGE,  timeout=1000)
            ending
            exit(1)
        if "0" in exitstatus[0]:
            print("{0}..................................|".format(YELLOW))
            print(" ☀ Build completed succesfully{0}".format(NOC))
            print("")
            with open('{0}/upload/build-{1}.log'.format(TOOLLOG, ROM), 'rb') as document_file:
                MESSAGE=" ☀ Finish build {0} \n⌚ {1} \n{2}".format(ROM, DATE, INFOCLI )
                bot.send_document(chat_id=bot_chatID,  document=document_file,  caption=MESSAGE,  timeout=1000)
            print("{0}................................../".format(GREEN))
            print(" 📂 Copying {0}{1} to {2}{3}".format(GREEN, ROM,TOOLROM, NOC))
            print("")
            OSC = ROMZI.get('{0}'.format(ZOPO))  
            os.system("cp -r {0}/{1}/{2}         {3}".format(ROMDIR, OUTF,OSC,TOOLROM))
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
            print(" 📤 Uploading {0}{1}{2}".format(GREEN, ROM, NOC))
            print("")
            os.chdir ( TOOLROM )     
            time = datetime.now()
            DATE = time.strftime("%Y-%m-%d %H:%M")
            send_text("📤 Uploading {0} \n\n⌚ {1}".format(ROM, DATE))  
            #Telegram notification
            OSC = ROMZI.get('{0}'.format(ZOPO)) 
            cmd = "scp {0}/{1}    {2}{3}/".format(TOOLROM,OSC,LINKUPL,ROM) 
            os.system(cmd)
            os.chdir ( TOOLROM )            
            for file in glob.glob("{0}".format(OSC)):
                    FILENAME=file
                    UPDATE_URL = "{0}/{1}/{2}".format(LINKSOU, ROM, FILENAME)
            print("{0}..................................|{1}".format(YELLOW, NOC))
            print(" 📂 Uploaded {0}{1}{2} {3}".format(YELLOW, ROM, NOC,  UPDATE_URL))
            print("")
            time = datetime.now()
            DATE = time.strftime("%Y-%m-%d %H:%M")
            send_text("📂 Uploaded {0} \nLink: {1} \n⌚{2}".format(ROM, UPDATE_URL, DATE))
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
            print(" 🗑 Make clean {0}{1}{2}".format(GREEN, ROM, NOC))
            print("")
            os.chdir ( ROMDIR )
            os.system("make clean")
            ending()
        elif clean == "zip":
            print("--- Finish ....... {0}{1}{2}  :amazon-clouddirectory:".format(CYAN,ROM, NOC))
            print()
            print("{0}................................../{1}".format(GREEN, NOC))
            print(" 🗑 Delete folder {0}{1}{2}".format(GREEN, ROM, NOC))
            print("")
            os.system("rm -rf {0}/{1}/*.zip".format(ROMDIR, OUTF))
            ending()
        elif clean == "delete":
            print("--- Finish ....... {0}{1}{2}  :amazon-clouddirectory:".format(CYAN,ROM, NOC))
            print()
            print("{0}................................../{1}".format(GREEN, NOC))
            print(" 🗑 Delete folder {0}{1}{2}".format(GREEN, ROM, NOC))
            print("")
            os.chdir ( ROMDIR )
            shutil.rmtree("ROM")
            ending()
        elif clean == "reset":
            print("--- Finish ....... {0}{1}{2}  :amazon-clouddirectory:".format(CYAN,ROM, NOC))
            print()
            os.chdir ( ROMDIR )
            os.system("find ./  -mindepth 1 ! -regex '^./.repo\(/.*\)?' -delete")              
            print("{0}................................../{1}".format(GREEN, NOC))
            print(" 🗑 Delete folder to {0}{1}{2} except .repo ".format(GREEN, ROM, NOC))
            print("")
            ending()
        elif clean == "no":
            print("{0}..................................!".format(YELLOW))
            print("Nothing {0} to do".format(NOC))
            print("")
            ending()
            
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
