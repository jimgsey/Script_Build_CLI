### Telegram notification
ARG1=$1
ROM=$2
TOOLLOG=$3
ID=$4
TOKEN=$5
CLI="Link to CLI: http://jimgsei.github.io"
FILE="@/${TOOLLOG}/build-${ROM}.log"
inline_keyboard='{"inline_keyboard": [[{"text":"Server","url":"http://jimgsei.github.io"}]]}'
DATE=$(date '+%d/%m/%Y')
HOURS=$(date '+%H:%M min')
#######
    if [ $ARG1 == "sync1"  ]; then
        MESSAGE="Start sync $ROM Date: $DATE at $HOURS"
        curl  -X POST https://api.telegram.org/bot$TOKEN/sendMessage -d text="$MESSAGE" -d chat_id=-366792053 -d "reply_markup=$inline_keyboard" -H Content-Type=application/json
    elif [ $ARG1 == "sync2"  ]; then
        MESSAGE="Finish sync $ROM Date: $DATE at $HOURS"
        curl  -X POST https://api.telegram.org/bot$TOKEN/sendMessage -d text="$MESSAGE" -d chat_id=-366792053 -d "reply_markup=$inline_keyboard" -H Content-Type=application/json
    elif [ $ARG1 == "build1"  ]; then
        MESSAGE="Start build  $ROM. Date: $DATE at $HOURS"
        curl  -X POST https://api.telegram.org/bot$TOKEN/sendMessage -d text="$MESSAGE" -d chat_id=-366792053 -d "reply_markup=$inline_keyboard" -H Content-Type=application/json
    elif [ $ARG1 == "build2"  ]; then
        MESSAGE="Error compiling $ROM. Date: $DATE at $HOURS $CLI"
        curl -s -X POST https://api.telegram.org/bot$TOKEN/sendDocument -F chat_id=$ID -F caption="$MESSAGE" -F document="$FILE"
    elif [ $ARG1 == "build3"  ]; then
        MESSAGE="Finished build ${ROM}. Date: $DATE at $HOURS $CLI"
        curl -s -X POST https://api.telegram.org/bot$TOKEN/sendDocument -F chat_id=$ID -F caption="$MESSAGE" -F document="$FILE"
    elif [ $ARG1 == "upload1"  ]; then
        MESSAGE="Uploading $ROM. Date: $DATE at $HOURS"
        curl  -X POST https://api.telegram.org/bot$TOKEN/sendMessage -d text="$MESSAGE" -d chat_id=-366792053 -d "reply_markup=$inline_keyboard" -H Content-Type=application/json        
    else
        echo "Error"
    fi



