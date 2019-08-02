USERNAME_BITBUCKET = sargeras55
PASSWORD_BITBUCKET = *********



##########################################
##########. PREPARE. #####################
##########################################
# Create bash profile
touch .bash_profile

# Install HOMEBREW | Need password | NEED ADD KEYCHAIN TO ENV
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"



##########################################
##########. INSTALL PROGRAMM TOOLS. ######
##########################################
# Install PYTHON 3
brew install python3

# Install GIT
brew install git



##########################################
#############. INSTALL XCODE. ############
##########################################
while getopts ":hv" option; do
    case $option in
        h) echo "usage: $0 [-h] [-v] ~/path/to/.../Xcode.dmg ~/path/to/.../install/app/bundle/ final-name-of-Xcode.app"; exit ;;
        v) VERBOSE=true ;;
        ?) echo "error: invalid option -$OPTARG"; exit ;;
    esac
done

# remove the options from the positional parameters
shift $(( OPTIND - 1 ))

# get the parameters for paths, xcode name
DOWNLOADED_DMG_PATH="${1}" # location of the downloaded DMG
XCODE_INSTALL_NAME="${2}" # what the .app bundle should be named

# if no install name is supplied, default to the name of the DMG
if [[ -z "${XCODE_INSTALL_NAME}" ]]; then
    XCODE_INSTALL_NAME=`find ${DOWNLOADED_DMG_PATH} -maxdepth 1 -exec basename {} \; | rev | cut -f 2- -d '.' | rev`".app"
fi

XCODE_INSTALL_LOCATION="${3}" # where Xcode should be installed

# if no custom install location is supplied, default to /Applications
if [[ -z "${XCODE_INSTALL_LOCATION}" ]]; then
    XCODE_INSTALL_LOCATION="/Applications"
fi

XCODE_INSTALL_PATH="${XCODE_INSTALL_LOCATION}/${XCODE_INSTALL_NAME}"
echo "DOWNLOADED_DMG_PATH=${DOWNLOADED_DMG_PATH}"
echo "XCODE_INSTALL_NAME=${XCODE_INSTALL_NAME}"
echo "XCODE_INSTALL_LOCATION=${XCODE_INSTALL_LOCATION}"
echo "XCODE_INSTALL_PATH=${XCODE_INSTALL_PATH}"
echo "======================================================"

# mount the disk image
echo "hdiutil attach \"${DOWNLOADED_DMG_PATH}\""
hdiutil attach "${DOWNLOADED_DMG_PATH}"
echo "======================================================"

# prepare install destination if it doesn’t exist
echo "mkdir \"${XCODE_INSTALL_LOCATION}\""
mkdir "${XCODE_INSTALL_LOCATION}"
echo "======================================================"

# get the canonical path to the Xcode app bundle in the DMG
echo "XCODE_BUNDLE_PATH=\`find /Volumes/Xcode -maxdepth 1 -name \"Xcode*.app\"\`"
XCODE_BUNDLE_PATH=`find /Volumes/Xcode -maxdepth 1 -name "Xcode*.app"`
echo "XCODE_BUNDLE_PATH=${XCODE_BUNDLE_PATH}"
echo "======================================================"

# copy the app bundle to the install location
echo "cp -R \"${XCODE_BUNDLE_PATH}\" \"${XCODE_INSTALL_PATH}\""
cp -R "${XCODE_BUNDLE_PATH}" "${XCODE_INSTALL_PATH}"
echo "======================================================"

# unmount the DMG
echo "hdiutil detach /Volumes/Xcode"
hdiutil detach /Volumes/Xcode
echo "======================================================"

# set new xcode as the preferred toolchain
echo "xcode-select -s \"${XCODE_INSTALL_PATH}\""
xcode-select -s "${XCODE_INSTALL_PATH}"
echo "======================================================"

# accept the user license agreement
echo "xcodebuild -license accept"
xcodebuild -license accept
echo "======================================================"

# install command line tools
echo "\"${XCODE_INSTALL_PATH}\" -installComponents"
"${XCODE_INSTALL_PATH}/Contents/MacOS/Xcode" -installComponents
echo "======================================================"
echo "Finished installing Xcode."



##########################################
#############. INSTALL TOOLS. ############
##########################################
# Install Java
echo "Start installing Java."
brew cask install java
echo "Finished installing Java."

# Install Android SDK
echo "Start installing Android SDK."
brew cask install android-sdk
echo 'export ANDROID_HOME=/usr/local/share/android-sdk' >>~/.bash_profile
source ~/.bash_profile
echo "Finished installing Android SDK."

# Install RVM
echo "Start installing RVM."
\curl -sSL https://get.rvm.io | bash -s stable --ruby
echo "Finished installing RVM."

# Install Fastlane
echo "Start installing Fastlane."
brew cask install fastlane
echo 'export PATH="$HOME/.fastlane/bin:$PATH"' >>~/.bash_profile
source ~/.bash_profile
echo "Finished installing Fastlane."

# Install RabbitMQ
echo "Start installing RabbitMQ."
brew install rabbitmq
echo 'export PATH=$PATH:/usr/local/sbin:$PATH' >>~/.bash_profile
source ~/.bash_profile
# rabbitmq-server start
echo "Finished installing RabbitMQ."



##########################################
##########. INSTALL BUILDER. #############
##########################################
# Create path to Script
echo "Start creating path to Script"
mkdir -p Code/Python/MobileScript
cd Code/Python/MobileScript
echo "Created path to Script"

# Clone Script
echo "Start clone Builder"
git clone https://$USERNAME_BITBUCKET:$PASSWORD_BITBUCKET@bitbucket.org/sargeras55/python-build-script.git
cd
echo "Finish clone Builder"

# Install PIP LIBS
echo "Install PIP LIBS"
pip3 install requests —upgrade
pip3 install python-telegram-bot --upgrade
pip3 install flask --upgrade
pip3 install sqlalchemy --upgrade
pip3 install pymysql --upgrade
pip3 install pika --upgrade
pip3 install pydrive --upgrade
pip3 install GitPython --upgrade
echo "Installed PIP LIBS"
