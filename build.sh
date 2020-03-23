# Copyright (C) 2020 Jimgsey All rights reserved

# Declare all functions

## You could add your link to CLI, that way, you could see the process when a message if you add your server link: https://buildkite.com/jimgsey/ or your web: https://jimgsei.github.io.
LINKCLI=""
INFOCLI="Link to CLI: $LINKCLI"
## Your link server generate. For example Sourceforge: https://sourceforge.net/projects/lavender7/files
LINKSOU=""

## Your link account to upload. For example: jim15@frs.sourceforge.net:/home/frs/project/
LINKUPL=""

## Device Default structure
DEVICES="/xiaomi/lavender"

## Folder Script (where everything is compiled) 
SCRIPT="${HOME}/Android"
## Folder Builds working
SCRIPTFOLDER="${HOME}/Android/Builds"

# Add colors
red=$(tput setaf 001)             #  red
green=$(tput setaf 002)           #  green
orange=$(tput setaf 208)          #  orange
blue=$(tput setaf 004)            #  blue
magenta=$(tput setaf 005)         #  magenta
cyan=$(tput setaf 006)            #  cyan
grey=$(tput setaf 242)            #  grey
smul=$(tput smul)                 #  smul
bold=$(tput bold)                 #  bold
txtrst=$(tput sgr0)               #  reset


## Tools (It is inside the android folder) and inside is the Roms and Tree folder
### Tools/Roms (A copy of the rom is made when the build is finished and then maintained. So you can delete the source folder to have more space.)
### Tools/Tree (Copy the vendor and kernel folder into the "Common" folder) (copy your device folder into another with the name of the rom)
### Example
#          __________________________________________________________________
#         |                                                                  |
#         |  /home/Android/Tools/Tree/                                       |
#         |                       l___ Aicp/device/xiaomi/lavender           |
#         |                       l___ Common/vendor/xiaomi/lavender         |
#         |                       l___ Common/kernel/xiaomi/lavender         |
#         |__________________________________________________________________|
#
TOOL="${SCRIPT}/Tools"
TOOLTREE="${SCRIPT}/Tools/Tree"
TOOLROM="${SCRIPT}/Tools/Roms"
TOOLPATCH="/Tools/Patch"

## Out folder where the rom is compiled. Example to lavender: "out/target/product/lavender" 
OUTF="out/target/product/lavender/"

####################################################
VAL="aicp aex altair aokp aosip candy carbon colt corvus cosmic cosp crdroid derpfest dot floko havoc ion lineage lotus nitrogen paranoid reloaded renouveau revenge resurrectionremix stag statix viper xenon xtended"
## You can add your repo Q or Pie

AICPLINK="https://github.com/AICP/platform_manifest.git -b p9.0"
AEXLINK="https://github.com/AospExtended/manifest.git -b 9.x"
ALTAIRLINK="https://github.com/AltairROM/android -b p"
AOKPLINK="https://github.com/AOKP/platform_manifest.git -b pie"
AOSIPLINK="https://github.com/AOSiP/platform_manifest.git -b pie"
ARROWLINK="https://github.com/ArrowOS/android_manifest.git -b arrow-9.x"
CANDYLINK="https://github.com/CandyRoms/candy.git -b c9.0"
CARBONLINK="https://github.com/CarbonROM/android.git -b cr-7.0 "
COLTLINK="https://github.com/Colt-Enigma/platform_manifest.git -b wip"
CORVUSLINK="https://github.com/du-rex/android_manifest.git -b p9x-caf"
COSMICLINK="https://github.com/Cosmic-OS/platform_manifest.git -b corona-release"
COSPLINK="https://github.com/cosp-project/manifest -b pie"
CRDROIDLINK="https://github.com/crdroidandroid/android.git -b 9.0"
DERPFESTLINK="https://github.com/DerpFest-Pie/platform_manifest.git -b pie"
DOTPLINK="https://github.com/DotOS/manifest.git -b dot-p"
FLOKOLINK="https://github.com/FlokoROM/manifesto.git -b 9.0"
HAVOCLINK="https://github.com/Havoc-OS/android_manifest.git -b pie"
IONLINK="https://github.com/i-o-n/manifest -b pie"
LINEAGELINK="https://github.com/LineageOS/android.git -b lineage-16.0"
LOTUSLINK="https://github.com/LotusOS/android_manifest.git -b pie"
NITROGENLINK="https://github.com/nitrogen-project/android_manifest.git -b p"
PARANOIDLINK="https://github.com/AOSPA/manifest -b pie"
RELOADEDLINK="https://github.com/ReloadedOS/android_manifest.git -b pie"
RENOUVEAULINK="https://github.com/RenouveauOS/android.git -b renouveau-9.0"
REVENGELINK="https://github.com/RevengeOS/android_manifest -b r9.0-caf"
RESURRECTIONREMIXLINK="https://github.com/RR-Test/platform_manifest.git -b test_pie"
STAGLINK="https://github.com/StagOS/manifest.git -b p9"
STATIXLINK="https://github.com/StatiXOS/android_manifest.git -b 9-caf"
VIPERLINK="https://github.com/ViperOS/viper_manifest.git -b pie"
XENONLINK="https://github.com/TeamHorizon/platform_manifest.git -b p"
XTENDEDLINK="https://github.com/Project-Xtended/manifest.git -b xp"

################### ZIP ROMS #################################
AICPZIP="aicp_lavender_p*.zip"
AEXZIP="AospEx*.zip"
ALTAIRZIP="Altair*.zip"
AOKPZIP="aokp_lavender_pie*.zip"
AOSIPZIP="AOSiP-9.0-Pizza*.zip"
ARROWZIP="Arrow-v9.0-lavender*.zip"
CANDYZIP="Candy*.zip"
CARBONZIP="CARBON*.zip"
COLTZIP="ColtOS*.zip"
CORVUSZIP="Cor*.zip"
COSMICZIP="Cosmic-OS-v4.0-Corona*.zip"
COSPZIP="COSP*.zip"
CRDROIDZIP="crDroidAndroid-9*.zip"
DERPFESTZIP="AOSiP-9.0-DerpFest*.zip"
DOTZIP="dotOS-P*.zip"
FLOKOZIP="Floko*.zip"
HAVOCZIP="Havoc*.zip"
IONZIP="ion*.zip"
LINEAGEZIP="lineage-16*.zip"
LOTUSZIP="Lo*.zip"
NITROGENZIP="Nitrogen*.zip"
PARANOIDZIP="Pa*.zip"
RELOADEDZIP="Reloaded-9.0*.zip"
RENOUVEAUZIP="Reno*.zip"
REVENGEZIP="RevengeOS*.zip"
RESURRECTIONREMIXZIP="RR-P-v7*.zip"
STAGZIP="stag_lavender_p*.zip"
STATIXZIP="statix*.zip"
VIPERZIP="Viper*.zip"
XENONZIP="XenonHD*.zip"
XTENDEDZIP="Xtended*.zip"
#####################################################

# Telegram Messages Bot

function telegrammsg() {
TOKEN=""
ID=""
curl -s -X POST https://api.telegram.org/bot$TOKEN/sendMessage -d chat_id=$ID -d text="$MESSAGE"
}

## Start script

function startfo() {
             if [ -d ${SCRIPT}/ ]; then
               echo ""
             else   
                mkdir ${SCRIPT}
             fi

			if [ -d ${SCRIPTFOLDER}/ ]; then	
                  echo ""
             else   
                mkdir ${SCRIPTFOLDER}
             fi

            if [ -d ${TOOL}/ ]; then	
                 echo ""
             else   
                mkdir ${TOOL}
             fi 

            if [ -d ${TOOLTREE}/ ]; then	
                 echo ""
             else   
                 mkdir ${TOOLTREE}
             fi 

            if [ -d ${TOOLROM}/ ]; then	
                 echo ""
             else   
                 mkdir ${TOOLROM}
             fi  
            
}

# Select ROM
function romselect() {
    # You can export the ROM by running export SCRIPTROM="<romnumber>". Example: export SCRIPTROM="1" (for LineageOS 16.0)
    if [[ -v SCRIPTROM ]]; then
    echo ""
    else
        	
        echo ""
		echo "         #####################################"
        echo ""	
		echo "         ${bold}   What rom do you want to ${cyan}build${txtrst}${bold} ?${txtrst}"
        echo ""
        echo "         #####################################"
		echo ""
        echo "                  [${cyan}${bold}aicp${txtrst}]                 Aicp"
        echo "                  [${cyan}${bold}aex${txtrst}]                  Aex"
        echo "                  [${cyan}${bold}altair${txtrst}]               Altair"
        echo "                  [${cyan}${bold}aokp${txtrst}]                 Aokp"
		echo "                  [${cyan}${bold}aosip${txtrst}]                Aosip"
        echo "                  [${cyan}${bold}candy${txtrst}]                Candy"
        echo "                  [${cyan}${bold}carbon${txtrst}]               Carbon"
        echo "                  [${cyan}${bold}colt${txtrst}]                 Colt"
        echo "                  [${cyan}${bold}corvus${txtrst}]               Corvus"
        echo "                  [${cyan}${bold}cosmic${txtrst}]               Cosmic"
        echo "                  [${cyan}${bold}cosp${txtrst}]                 Cosp"
        echo "                  [${cyan}${bold}crdroid${txtrst}]              CrDroid"
        echo "                  [${cyan}${bold}derpfest${txtrst}]             Derpfest"
        echo "                  [${cyan}${bold}dot${txtrst}]                  Dot"
		echo "                  [${cyan}${bold}floko${txtrst}]                Floko"
        echo "                  [${cyan}${bold}havoc${txtrst}]                Havoc"
        echo "                  [${cyan}${bold}ion${txtrst}]                  Ion"
        echo "                  [${cyan}${bold}lineage${txtrst}]              Lineage"
        echo "                  [${cyan}${bold}lotus${txtrst}]                Lotus"
        echo "                  [${cyan}${bold}nitrogen${txtrst}]             Nitrogen"
        echo "                  [${cyan}${bold}paranoid${txtrst}]             Paranoid"
		echo "                  [${cyan}${bold}reloaded${txtrst}]             Reloaded"
        echo "                  [${cyan}${bold}renouveau${txtrst}]            Renouveau"
        echo "                  [${cyan}${bold}revenge${txtrst}]              Revenge"
        echo "                  [${cyan}${bold}resurrectionremix${txtrst}]    Resurrection Remix"
		echo "                  [${cyan}${bold}stag${txtrst}]                 Stag"
		echo "                  [${cyan}${bold}statix${txtrst}]               Statix"
		echo "                  [${cyan}${bold}viper${txtrst}]                Viper"
		echo "                  [${cyan}${bold}xenon${txtrst}]                Xenon HD"
        echo "                  [${cyan}${bold}xtended${txtrst}]              Xtended"     
        echo ""
        echo ""
        read -p "        ${smul}${bold} Please, enter your choice ${txtrst}: ${cyan}${bold} " SCRIPTROM
        echo "${txtrst}"
    fi

    if [[ ${#SCRIPTROM} -lt 2 ]]; then 
    		
	    echo ""
		echo "        ${red}${bold}..................................O ${txtrst}"
        echo "        You didn't entered a valid option"
        echo ""
		ending
#Finish with error
        exit 1
     elif [[ $VAL == *$SCRIPTROM*   ]]; then

       ROS=$(echo -n ${SCRIPTROM:0:1} | tr '[:lower:]' '[:upper:]' ; echo ${SCRIPTROM:1} | tr '[:upper:]' '[:lower:]' )
       ROM="$ROS"
       ROMDIR="${SCRIPTFOLDER}/${ROM}"
       ZOPO=$(echo -n ${ROM}ZIP | tr '[:lower:]' '[:upper:]')
		echo ""
		echo "        ${green}${bold}................................./ ${txtrst}"
		echo "        You will build ${green}${bold}${ROM}${txtrst}"
        echo ""
     else 
        echo ""
		echo "        ${red}${bold}.................................0 ${txtrst}"
		echo "        You have not entered a correct option"
        echo ""
        ending
#Finish with error
        exit 1
     fi   
}

## Rom Folder
function romfolder() {
    if [ -d ${ROMDIR} ]; then
                   echo ""
				   echo "        ${orange}${bold}..................................!"
                   echo "        ${ROM}${txtrst} folder already exists"
                   echo ""
    else
                   echo ""
				   echo "        ${green}${bold}................................../ ${txtrst}"
                   echo "        Create folder to ${green}${bold}${ROM}${txtrst}"
                   echo ""
                   mkdir ${ROMDIR} 
    fi
	
	if [ -d ${ROMDIR}/.repo/ ]; then
                   echo ""
				   echo "        ${orange}${bold}..................................!"
                   echo "        ${ROM}${txtrst} repo already exists"
                   echo ""
    else
                   echo ""
				   echo "        ${green}${bold}................................../ ${txtrst}"
				   echo "        Add link to ${green}${bold}${ROM}${txtrst} repo" 
                   cd $ROMDIR
                   echo ""
                   echo "" 
		#Add repo link		   
        REP=$(echo -n ${ROM}LINK | tr '[:lower:]' '[:upper:]')
        repo init -u ${!REP}
    fi
}

# Repo sync
function syncrom() {
     
	if [[ -v SCRIPTSYNC ]]; then
    echo ""
    else
	    echo ""
		echo ""
		echo "         #######################################"
        echo ""
        echo "                   ${bold} Sync or skip: ${txtrst}"
        echo ""
        echo "           You could update ${cyan}${bold}${ROM}${txtrst} repository"
        echo ""
		echo "         #######################################"
		echo ""
        echo "                 [${cyan}${bold}yes${txtrst}] Sync Repository"
        echo "                 [${cyan}${bold}no${txtrst}]  Skip Sync"
		echo ""
		read -p "            ${smul}${bold} Please, write your choise ${txtrst}: ${cyan}${bold}"  SCRIPTSYNC
        echo "${txtrst}" 
    fi
    if [ $SCRIPTSYNC = "yes" ]; then
	    echo ""
		echo "        ${green}${bold}................................../ ${txtrst}"
        echo "        Synchronizing repository ${green}${bold}${ROM}${txtrst}"
        echo ""
		romfolder
###########################################################################################################################
DATE=$(date '+%d/%m/%Y')
HOURS=$(date '+%H:%M min')
MESSAGE="Start sync $ROM at $HOURS to $DATE $INFOCLI"
        telegrammsg
###########################################################################################################################
	    cd $ROMDIR	
	    if ping -c1 google.com &>/dev/null; then
        repo sync --force-sync --no-clone-bundle --no-tags -j4 
		     echo ""
			 echo "        ${orange}${bold}.............................| ${txtrst}"
             echo "        Sync done ${orange}${bold}${ROM}${txtrst}"
             echo ""
###########################################################################################################################
DATE=$(date '+%d/%m/%Y')
HOURS=$(date '+%H:%M min')
MESSAGE="Finish sync $ROM at $HOURS to $DATE $INFOCLI"
        telegrammsg
###########################################################################################################################
        else
		     echo ""
		     echo "        ${red}${bold}..................................- ${txtrst}"
             echo "        Sync failed ${red}${bold}${ROM}${txtrst} You need internet"
             echo ""
###########################################################################################################################
DATE=$(date '+%d/%m/%Y')
HOURS=$(date '+%H:%M min')
MESSAGE="Failed sync $ROM at $HOURS to $DATE $INFOCLI"
        telegrammsg
###########################################################################################################################
        ending
#Finish with error
        exit 1
        fi
    elif [ $SCRIPTSYNC = "no" ]; then
	    echo ""
		echo "        ${orange}${bold}..................................! ${txtrst}"
        echo "        Skip sync ${orange}${bold}${ROM}${txtrst}"
        echo ""
    else
		echo ""
		echo "        ${red}${bold}.....................................O ${txtrst}"
        echo "        You didn't entered a valid option"
        echo ""
		ending
#Finish with error
        exit 1

    fi
}

# Generate mirror json

function gen_ota_json() {
     
    if [ $SCRIPTROM = "aicp" ]; then
	    echo ""
		echo "        ${green}${bold}................................../ ${txtrst}"
        echo "        Generating $ROM 14.0 json"
            cd $ROMDIR
            DATETIME=$(grep "ro.build.date.utc=" ${OUTF}/system/build.prop | cut -d "=" -f 2)
            FILENAME=$(find ${OUTF}/${!ZOPO} | cut -d "/" -f 5)
            ID=$(md5sum ${OUTF}/${!ZOPO} | cut -d " " -f 1)
            SIZE=$(wc -c ${OUTF}/${!ZOPO} | awk '{print $1}')
            URL1="${LINKSOU}/${ROM}/$FILENAME"
            URL=$URL1
            VERSION="14.0"
            ROMTYPE="unofficial"
                   JSON_FMT='{\n"response": [\n{\n"filename": "%s",\n"datetime": %s,\n"size":%s, \n"url":"%s", \n"version": "%s",\n"romtype": "%s", \n"id": "%s"\n}\n]\n}'
                   printf "$JSON_FMT" "$FILENAME" "$DATETIME" "$SIZE" "$URL" "$VERSION" "$ROMTYPE" "$ID" > ~/script/ota/lavender-aicp.json 
#Example 	
	elif [ $SCRIPTROM = "xtended" ]; then
        echo ""
		echo "${green}${bold}................................../ ${txtrst}"
        echo "$ROM OTA is not supported by the script, skipping generation"
	else
        echo ""
		echo "${orange}${bold}..................................! ${txtrst}"
        echo "$ROM OTA is not supported by the script, skipping generation"       		
    fi
}

## UPload OTA to github repo
function push_ota () {
	cd  ${HOME}/script/ota/ 
	git add . 
	git commit -m "Update" 
	git push -u origin master
}

# ROM patcher this is for using custom OTA services for example
function patchrom () {
    
    if [[ -v PATCHROMS ]]; then
    echo ""
    else
        	
        echo ""
        echo ""
		echo ""
		echo "         #####################################"
        echo ""
        echo "                ${bold}Patch rom or Skip :    ${txtrst}"
        echo ""
        echo ""
        echo "         You need mod script if you want patch"
        echo "                       ${cyan}${bold}${ROM}${txtrst}"
        echo "         #####################################"
		echo ""
        echo "               [${cyan}${bold}yes${txtrst}] Patch"
        echo "               [${cyan}${bold}no${txtrst}]  No"
        echo ""
        read -p "            ${smul}${bold} Please, write your choise ${txtrst}: ${cyan}${bold}" PATCHROMS
        echo "${txtrst}"
    fi

    if [ $PATCHROMS = "yes" ]; then
### Copy Gapps by default
      cp -r ${SCRIPT}${TOOLPATCH}/Common/*      ${SCRIPTFOLDER}/${ROM}

         if [ $SCRIPTROM = "aicp" ]; then
	        echo ""
		    echo "        ${green}${bold}................................../ ${txtrst}"
            echo "        Changing updater to ${green}${bold}${ROM}${txtrst}"
            cp ~/script/aicp/updater/strings.xml ${ROMDIR}/packages/apps/Updater/res/values
        elif [ $SCRIPTROM = "derpfest" ]; then
            echo "${!ZOPO}"
		    echo "${green}${bold}................................../ ${txtrst}"
            echo "        OTA for ${green}${bold}${ROM}${txtrst} not supported by the script, skipping patch"
            echo ""
         else
            echo "        ${green}${bold}................................../ ${txtrst}"
            echo "        Any patch to ${green}${bold}${ROM}${txtrst} "
            echo ""
         fi 
   elif [ $PATCHROMS = "no" ]; then  
        echo "        ${orange}${bold}................................../ ${txtrst}"
        echo "        Skip patch ${orange}${bold}${ROM}${txtrst}"
        echo ""   
   else
	    echo ""
		echo "        ${red}${bold}..................................O ${txtrst}"
        echo "        You didn't entered a valid option"
        echo ""
		ending
#Finish with error
        exit 1

    fi
}

## Start build
function buildin() {
		    echo ""
	        echo "        ${green}${bold}................................../ ${txtrst}"
		    echo "        it will begin to build ${green}${bold}${ROM}${txtrst}"
            echo ""
            copytrees
##############################################Push telegram message####################################################
    DATE=$(date '+%d/%m/%Y')
    HOURS=$(date '+%H:%M min')
	MESSAGE="Start build  $ROM. Date: $DATE at $HOURS $INFOCLI"
	       telegrammsg
#######################################################################################################################	
}

#Clonado device tree
function copytrees() {

### Device T  
              if [ -d ${ROMDIR}/device/${DEVICES}/ ]; then
                   echo ""
				   echo "        ${orange}${bold}..................................! ${txtrst}"
                   echo "        ${orange}${bold}DT${txtrst} already exists"
                   echo ""
## Default
             elif [ -d ${TOOLTREE}/${ROM}/ ]; then	
                    echo ""
				    echo "        ${green}${bold}................................../ ${txtrst}"
                    echo "        Copying ${green}${bold}DT${txtrst}"
                    echo ""
                    cp -r ${TOOLTREE}/${ROM}/*         ${ROMDIR}

## Internet
			 elif ping -c1 google.com &>/dev/null; then
                    echo ""
                    echo ""
                    read -p "${smul}${bold} Please, write DT link ${txtrst}: ${cyan}${bold}" DT
                    echo "${txtrst}"
					echo "        Sync ${green}${bold}Repo DT${txtrst}"
                git clone $DT ${ROMDIR}/device/${DEVICES}

## Local
            else 
	 echo "      _________________________________________________________________________ "
     echo "     |                                                                         |"
     echo "     |                                                                         |"   
     echo "     |   - Prepare the dt, vt and kernel  a folder with the name you want.     |"                          
     echo "     |          Remember that the architecture is correct device and           |"   
     echo "     |             the files are extracted, not compressed in zip.             |"
     echo "     |                                                                         |" 
     echo "     |              For example to *Lavender*                                  |" 
     echo "     |                                                                         |"
     echo "     |                    My Folder/                                           |"
     echo "     |                       l___ device/xiaomi/lavender                       |"
     echo "     |                       l___ vendor/xiaomi/lavender                       |"
     echo "     |                       l___ kernel/xiaomi/lavender                       |"
     echo "     |                                                                         |"
     echo "     |                                                                         |"
     echo "     |        * Write the full path where your folder is located.              |"
     echo "     |                                                                         |" 
     echo "     |             For example: /home/YourUserPc/My Folder                     |" 
     echo "     |_________________________________________________________________________|"
		            echo ""
                    echo ""    
		            read -p "${smul}${bold} Please, write the *route* where you have saved your 3 tree ${txtrst}: ${cyan}${bold}" RUTA
                    echo "${txtrst}"
                    cp -r ${RUTA}/*         ${ROMDIR}
                    echo ""
				    echo "        ${green}${bold}................................../ ${txtrst}"
                    echo "        Copying your choise ${green}${bold} tree{txtrst}"	
                    echo ""			
                
			fi

### Vendor T         
           if [ -d ${ROMDIR}/vendor/${DEVICES}/ ]; then
                   echo ""
				   echo "        ${orange}${bold}..................................! ${txtrst}"
                   echo "        ${orange}${bold}VT${txtrst} already exists"
                   echo ""
## Default
           elif [ -d ${TOOLTREE}/${ROM}/ ]; then	
                   echo ""
				   echo "        ${green}${bold}................................../ ${txtrst}"
                   echo "        Copying ${green}${bold}VT{txtrst}"
                   echo ""
                   cp -r ${TOOLTREE}/Common/vendor         ${ROMDIR}
## Internet
			elif ping -c1 google.com &>/dev/null; then
                   echo ""
                   echo ""
                   read -p "${smul}${bold} Please, write VT link ${txtrst}: ${cyan}${bold}" VT
                   echo "${txtrst}"
				   echo "        Sync ${green}${bold}Repo VT${txtrst}"
                git clone $VT ${ROMDIR}/vendor/${DEVICES}
                
## Local
           else 
	 echo "      _________________________________________________________________________ "
     echo "     |                                                                         |"
     echo "     |                                                                         |"   
     echo "     |   - Prepare the dt, vt and kernel  a folder with the name you want.     |"                          
     echo "     |          Remember that the architecture is correct device and           |"   
     echo "     |             the files are extracted, not compressed in zip.             |"
     echo "     |                                                                         |" 
     echo "     |              For example to *Lavender*                                  |" 
     echo "     |                                                                         |"
     echo "     |                    My Folder/                                           |"
     echo "     |                       l___ device/xiaomi/lavender                       |"
     echo "     |                       l___ vendor/xiaomi/lavender                       |"
     echo "     |                       l___ kernel/xiaomi/lavender                       |"
     echo "     |                                                                         |"
     echo "     |                                                                         |"
     echo "     |        * Write the full path where your folder is located.              |"
     echo "     |                                                                         |" 
     echo "     |             For example: /home/YourUserPc/My Folder                     |" 
     echo "     |_________________________________________________________________________|"
		            echo ""
                    echo ""    
		            read -p "${smul}${bold} Please, write the *route* where you have saved your 3 tree ${txtrst}: ${cyan}${bold}" RUTA
                    echo "${txtrst}"
                    cp -r ${RUTA}/*         ${ROMDIR}
                    echo ""
				    echo "        ${green}${bold}................................../ ${txtrst}"
                    echo "        Copying your choise ${green}${bold}tree${txtrst} "	
                    echo ""			
                
		     fi

             if [ -d ${ROMDIR}/kernel/${DEVICES}/ ]; then
                   echo ""
				   echo "        ${orange}${bold}..................................! ${txtrst}"
                   echo "        ${orange}${bold}KT${txtrst}  already exists"
                   echo ""
## Default
            elif [ -d ${TOOLTREE}/${ROM}/ ]; then	
                    echo ""
				    echo "        ${green}${bold}................................../ ${txtrst}"
                    echo "        Copying ${green}${bold}KT${txtrst} "
                    echo ""
                    cp -r ${TOOLTREE}/Common/kernel/         ${ROMDIR}
## Internet
			elif ping -c1 google.com &>/dev/null; then
                
                    echo ""
                    echo ""
                    read -p "${smul}${bold} Please, write KT link ${txtrst}: ${cyan}${bold}" KT
                    echo "${txtrst}"
                    echo "        Sync ${green}${bold}Repo KT${txtrst}"
                git clone $KT ${ROMDIR}/kernel/${DEVICES}
## Local
            else 
	 echo "      _________________________________________________________________________ "
     echo "     |                                                                         |"
     echo "     |                                                                         |"   
     echo "     |   - Prepare the dt, vt and kernel  a folder with the name you want.     |"                          
     echo "     |          Remember that the architecture is correct device and           |"   
     echo "     |             the files are extracted, not compressed in zip.             |"
     echo "     |                                                                         |" 
     echo "     |              For example to *Lavender*                                  |" 
     echo "     |                                                                         |"
     echo "     |                    My Folder/                                           |"
     echo "     |                       l___ device/xiaomi/lavender                       |"
     echo "     |                       l___ vendor/xiaomi/lavender                       |"
     echo "     |                       l___ kernel/xiaomi/lavender                       |"
     echo "     |                                                                         |"
     echo "     |                                                                         |"
     echo "     |        * Write the full path where your folder is located.              |"
     echo "     |                                                                         |" 
     echo "     |             For example: /home/YourUserPc/My Folder                     |" 
     echo "     |_________________________________________________________________________|"
		            echo ""
                    echo ""    
		            read -p "${smul}${bold} Please, write the *route* where you have saved your 3 tree ${txtrst}: ${cyan}${bold}" RUTA
                    echo "${txtrst}"
                    cp -r ${RUTA}/*         ${ROMDIR}
                    echo ""
				    echo "        ${green}${bold}................................../ ${txtrst}"
                    echo "        Copying your choise ${green}${bold}tree${txtrst}"
                    echo ""				
                
				fi

}


## End build
function buildfin() {
if [ $? -eq 0 ]; then
                     echo ""
	                 echo "        ${orange}${bold}..................................| ${txtrst}"
                     echo "        Finished build ${orange}${bold}${ROM}${txtrst}" 
                     echo "" 
		             cp ${OUTF}${!ZOPO}   ${TOOLROM}
##############################################Push telegram message####################################################
    DATE=$(date '+%d/%m/%Y')
    HOURS=$(date '+%H:%M min')
	MESSAGE="Finished build ${ROM}. Date: $DATE at $HOURS $INFOCLI"
	         telegrammsg
#######################################################################################################################		
                else
                      echo ""
	                  echo "        ${red}${bold}..................................- ${txtrst}"
                      echo "        Error compiling ${red}${bold}${ROM}${txtrst}"
                      echo ""
##############################################Push telegram message####################################################
    DATE=$(date '+%d/%m/%Y')
    HOURS=$(date '+%H:%M min')
	MESSAGE="Error compiling $ROM. Date: $DATE at $HOURS $INFOCLI"
	         telegrammsg
#######################################################################################################################	
	               ending
#Finish with error
        exit 1
                fi

}

# Build Rom
function buildrom() {

    if [[ -v BUILDROM ]]; then
    echo ""
    else
        echo ""
		echo "         #####################################"
		echo ""
        echo "               ${bold}  Build or Skip :    ${txtrst}"
        echo ""
        echo "               You could build ${cyan}${bold}${ROM}${txtrst}"
        echo ""
		echo "         #####################################"
		echo ""
        echo "               [${cyan}${bold}yes${txtrst}] Build"
        echo "               [${cyan}${bold}no${txtrst}]  No"
        echo ""
        read -p "           ${smul}${bold} Please, write your choise ${txtrst}: ${cyan}${bold}" BUILDROM
        echo "${txtrst}"
    fi

    if [ $BUILDROM = "yes" ]; then
	    echo ""
		echo "        ${green}${bold}................................../ ${txtrst}"
        echo "        Cloning necessary files"
        echo ""
        cd $ROMDIR
		git clone -b lineage-16.0 https://github.com/LineageOS/android_packages_resources_devicesettings packages/resources/devicesettings
################		   
        if [ $SCRIPTROM = "aicp" ]; then
            buildin
		    source build/envsetup.sh
            brunch lavender
            buildfin		 
		
        elif [ $SCRIPTROM = "aex" ]; then		
            buildin
		    source build/envsetup.sh
            lunch aosp_lavender-userdebug
            mka aex -j4
            buildfin

       elif [ $SCRIPTROM = "altair" ]; then		
            buildin
		    source build/envsetup.sh
            breakfast lavender
            brunch lavender
            buildfin				
		
        elif [ $SCRIPTROM = "aokp" ]; then		
            buildin
		    source build/envsetup.sh
            lunch aokp_lavender-userdebug
            mka rainbowfarts
            buildfin			
        
        elif [ $SCRIPTROM = "aosip" ]; then
            buildin
		    source build/envsetup.sh
            lunch aosip_lavender-userdebug
            mka kronic
            buildfin

		elif [ $SCRIPTROM = "arrow" ]; then		
            buildin
		    source build/envsetup.sh
            brunch lavender
            buildfin
 
        elif [ $SCRIPTROM = "candy" ]; then		
            buildin
		    source build/envsetup.sh
            brunch lavender
            buildfin
		
        elif [ $SCRIPTROM = "carbon" ]; then		
            buildin
		    source build/envsetup.sh
            lunch carbon_lavender-user
            make carbon -j4
            buildfin
       				
		 elif [ $SCRIPTROM = "colt" ]; then
            buildin
		    source build/envsetup.sh
            lunch colt_lavender-userdebug
            make colt
            buildfin

         elif [ $SCRIPTROM = "corvus" ]; then
            buildin
		    source build/envsetup.sh
            lunch du_lavender-userdebug
            make corvus
            buildfin   

        elif [ $SCRIPTROM = "cosmic" ]; then		
            buildin
		    source build/envsetup.sh
            lunch cos_lavender-userdebug
            brunch lavender
            buildfin			
        
        elif [ $SCRIPTROM = "cosp" ]; then		
            buildin
		    source build/envsetup.sh
            lunch cosp_lavender-userdebug
            mka bacon
            buildfin

        elif [ $SCRIPTROM = "crdroid" ]; then		
            buildin
		    source build/envsetup.sh
            brunch lavender
            buildfin
			  
        elif [ $SCRIPTROM = "derpfest" ]; then
            buildin
		    source build/envsetup.sh
            lunch aosip_lavender-userdebug
            mka kronic
            buildfin

        elif [ $SCRIPTROM = "dot" ]; then
            buildin
		    source build/envsetup.sh
            lunch dot_lavender-userdebug
            make bacon
            buildfin
		 
		elif [ $SCRIPTROM = "floko" ]; then
            buildin
		    source build/envsetup.sh
            brunch lavender 
            buildfin
		
        elif [ $SCRIPTROM = "havoc" ]; then		
            buildin	
		    source build/envsetup.sh
            brunch lavender
            buildfin        
				 
        elif [ $SCRIPTROM = "ion" ]; then		
            buildin
		    source build/envsetup.sh
            lunch ion_lavender-user
            mka bacon -j4
            buildfin
		
        elif [ $SCRIPTROM = "lineage" ]; then		
            buildin
		    source build/envsetup.sh
            breakfast lavender
            brunch lavender
            buildfin
          
	   elif [ $SCRIPTROM = "lotus" ]; then		
            buildin
		    source build/envsetup.sh
            lunch lotus_lavender-userdebug
            make bacon -j4
            buildfin		  

        elif [ $SCRIPTROM = "nitrogen" ]; then
            buildin
		    source build/envsetup.sh
            lunch nitrogen_lavender-userdebug
            make -j4 otapackage
            buildgin
  
          elif [ $SCRIPTROM = "paranoid" ]; then
            buildin	
		    source 
              ./rom-build.sh lavender
            buildfin

        elif [ $SCRIPTROM = "reloaded" ]; then		
            buildin
		    source build/envsetup.sh
            lunch reloaded_lavender-userdebug
            make reloaded
            buildfin

        elif [ $SCRIPTROM = "renouveau" ]; then		
            buildin
		    source build/envsetup.sh
            brunch lavender
            buildfin

        elif [ $SCRIPTROM = "revenge" ]; then
            buildin
		    source build/envsetup.sh
            lunch revengeos_lavender-userdebug
            make -j4 bacon
            buildfin
		
        elif [ $SCRIPTROM = "resurrectionremix" ]; then		
            buildin
		    source build/envsetup.sh
            brunch lavender
            buildfin
		
        elif [ $SCRIPTROM = "stag" ]; then
            buildin	
		    source build/envsetup.sh
            lunch stag_lavender-userdebug
            make stag
            buildfin

        elif [ $SCRIPTROM = "statix" ]; then
            buildin	
		    source build/envsetup.sh
            brunch statix_lavender-userdebug 
            buildfin

        elif [ $SCRIPTROM = "viper" ]; then
            buildin	
		    source build/envsetup.sh
            lunch viper_lavender-userdebug
            mka poison
            buildfin

		elif [ $SCRIPTROM = "xenon" ]; then
            buildin	
		    source build/envsetup.sh
            brunch lavender
            buildfin

        elif [ $SCRIPTROM = "xtended" ]; then	
            buildin
		    source build/envsetup.sh
            lunch xtended_lavender-userdebug
            make xtended
            buildfin    
    fi			
    elif [ $BUILDROM = "no" ]; then
            echo ""
		    echo "        ${orange}${bold}..................................O ${txtrst}"
			echo "        Skip Build ${orange}${bold}${ROM}${txtrst}" 
            echo ""      		
	
	else
	    echo ""
	    echo "        ${red}${bold} ................................../ ${txtrst}"
        echo "        You didn't entered a valid option"
        echo ""
		ending
#Finish with error
        exit 1
   
    fi
}      

# Upload ROM
function uploadrom() {

        if [[ -v UPLOADROM ]]; then
    echo ""
    else
		echo ""
		echo "         #####################################"
        echo ""
        echo "   ${bold}          Do you want upload the rom?  ${txtrst}"
		echo ""
        echo "               You could upload ${cyan}${bold}${ROM}${txtrst}" 
        echo "                to sourceforge"
        echo ""
		echo "         #####################################"
		echo ""
        echo "                 [${cyan}${bold}yes${txtrst}] Upload"
        echo "                 [${cyan}${bold}no${txtrst}]  Skip"
		echo ""
		read -p "          ${smul}${bold} Please, write your choise ${txtrst}: ${cyan}${bold}" UPLOADROM
        echo "${txtrst}"
    fi

    if [ $UPLOADROM = "yes" ]; then
        
              echo ""
			  echo "        ${green}${bold}................................../ ${txtrst}"
              echo "        Uploading ${green}${bold}${ROM}${txtrst}"
              echo ""			                  

##############################################Push telegram message############################################################
	DATE=$(date '+%d/%m/%Y')
    HOURS=$(date '+%H:%M min')
	MESSAGE="Uploading $ROM. Date: $DATE at $HOURS $INFOCLI"
	         telegrammsg
###############################################################################################################################	            
              scp ${TOOLROM}/${!ZOPO}   ${LINKUPL}${ROM}/			  
              echo ""
			  echo "        ${orange}${bold}..................................| ${txtrst}"
              echo "        Uploaded ${orange}${bold}${ROM}${txtrst}"
              echo ""
##############################################Push telegram message############################################################
    FILENAME=$(find ${TOOLROM}/${!ZOPO} | cut -d "/" -f 7)
	UPDATE_URL1="${LINKSOU}/${ROM}/$FILENAME/download"
	DATE=$(date '+%d/%m/%Y')
    HOURS=$(date '+%H:%M min')
	MESSAGE="Updated $ROM. Link:$UPDATE_URL1 Date: $DATE at $HOURS $INFOCLI"
	         telegrammsg
###############################################################################################################################	
            push_ota_json
      elif [ $UPLOADROM = "no" ]; then
	          echo ""
			  echo "        ${orange}${bold}..................................! ${txtrst}"
              echo "        Skip Upload ${orange}${bold}${ROM}${txtrst}"
              echo ""       		
      else
		      echo ""
			  echo "        ${red}${bold}.................................- ${txtrst}"
              echo "        You didn't entered a valid option"
              echo ""
	  ending
#Finish with error
        exit 1			

fi	
}

# Make clean
function romclean() {
    # You can export the ROM by running export SCRIPTROM="<text>". Example: export SCRIPTROM="lineage" (for LineageOS 16.0)
    if [[ -v ROMCLEAN ]]; then
    echo ""
    else
        echo ""
		echo ""
		echo "    ####################################################"
        echo ""
        echo "                   ${bold}   Final option  ${txtrst}"
        echo ""
        echo "     You could clean your old build or all folder build"
        echo "                       ${green}${bold}${ROM}${txtrst}"
        echo ""
		echo "    ####################################################"
		echo ""
        echo "               [${cyan}${bold}make${txtrst}]    Make Clean"
        echo "              [${cyan}${bold}delete${txtrst}]   Delete"
        echo "                [${cyan}${bold}no${txtrst}]     Nothing"
		echo ""
		echo ""
        read -p "        ${smul}${bold} Please, enter your choise ${txtrst}: ${cyan}${bold}"  ROMCLEAN
        echo "${txtrst}"
    fi
	
    if [ $ROMCLEAN = "make" ]; then
        echo ""
		echo "        ${green}${bold}................................../ ${txtrst}"
		echo "        Make clean ${green}${bold}${ROM}${txtrst} "
        echo ""
        cd $ROMDIR
        make clean
##############################################Push telegram message############################################################
	DATE=$(date '+%d/%m/%Y')
    HOURS=$(date '+%H:%M min')
	MESSAGE="Make Clean $ROM. Date: $DATE at $HOURS $INFOCLI"
	         telegrammsg
###############################################################################################################################	
				
    elif [ $ROMCLEAN = "delete" ]; then
	    echo ""
		echo "        ${green}${bold}................................../ ${txtrst}"
        echo "        Deleting all folder to ${cyan}${bold}${ROM}${txtrst}"
        echo ""
        rm -rf $ROMDIR
##############################################Push telegram message############################################################

	DATE=$(date '+%d/%m/%Y')
    HOURS=$(date '+%H:%M min')
	MESSAGE="Delete folder $ROM.  Date: $DATE at $HOURS $INFOCLI"
	         telegrammsg
		ending
###############################################################################################################################	
    elif [ $ROMCLEAN = "no" ]; then
	    echo ""
		echo "        ${orange}${bold}..................................O ${txtrst}"
        echo "        Nothing"
        echo ""
		ending
    else
	    echo ""
		echo "        ${red}${bold}.....................................- ${txtrst}"
        echo "        You didn't entered a valid option"
        echo ""
		ending
#Finish with error
        exit 1		

    fi
}

function ending() {
    sleep 3s
    echo ""
    echo "      ${bold} **********************************"
    echo ""
    echo "          ${smul}Thanks to use Script Build${txtrst}"  
    echo "" 
    echo ""  
	echo "        It was created for true ${cyan}${bold}BuildBot${txtrst}"	
    echo "" 	
    echo "      ${bold} **********************************"
    echo "                     * *" 	
    echo "                      *"	
    echo ""	
    echo "                 Contact:${txtrst}"
    echo ""		
    echo "      ${bold} My Telegram:${cyan}http://t.me/Jimgsey       ${txtrst}"		
    echo ""		
    echo "      ${bold} My Github:${cyan} https://github.com/jimgsey${txtrst}"
    echo ""
    echo "      ${bold} Source code:${cyan} https://github.com/jimgsey/Script_Build${txtrst}"
    echo ""	

}

# Main program
function main() {
echo ""
echo ""    
echo "          ${bold} *********************************${txtrst}"		
echo "                                          "		
echo "          ${bold}          𝕾𝖈𝖗𝖎𝖕𝖙 𝕭𝖚𝖎𝖑𝖉                "		
echo "                                 "		
echo "                         𝖇𝖞         ${txtrst}            "
echo "                                 "		
echo "           ${cyan}${bold}           𝕵𝖎𝖒𝖌𝖘𝖊𝖞        ${txtrst} "		
echo "                                "		
echo "          ${bold} *********************************${txtrst}"
echo ""	

    startfo
    romselect
    syncrom
    patchrom
	buildrom
    uploadrom
    romclean
}

#Execute the program
main
