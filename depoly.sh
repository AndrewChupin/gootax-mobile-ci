USERNAME_BITBUCKET = sargeras55
PASSWORD_BITBUCKET = *********


##########################################
echo PARAMS WITH PATH AND PASSWORDS DELETED FOR OPEN VERSION. PLEASE, ATTEND!
echo PARAMS WITH PATH AND PASSWORDS DELETED FOR OPEN VERSION. PLEASE, ATTEND!
echo PARAMS WITH PATH AND PASSWORDS DELETED FOR OPEN VERSION. PLEASE, ATTEND!
##########################################


##########################################
##########. PREPARE. #####################
##########################################
echo "======================================================"
echo "Create bash_profile."
# Create bash profile
touch .bash_profile
echo "======================================================"

# Install HOMEBREW | Need password | NEED ADD KEYCHAIN TO ENV
echo "Start installing Homebrew."
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
echo "======================================================"
echo "Finished prepare."



##########################################
##########. INSTALL PROGRAM TOOLS. ######
##########################################
echo "======================================================"
# Install PYTHON 3
echo "Start installing Python 3."
brew install python3

# Install GIT
echo "Start installing Git."
brew install git
echo "======================================================"
echo "Finished installing program tools."



##########################################
#############. INSTALL XCODE. ############
##########################################
# Remove the options from the positional parameters
shift $(( OPTIND - 1 ))

# Get the parameters for paths, xcode name
DOWNLOADED_DMG_PATH="${1}" # location of the downloaded DMG
XCODE_INSTALL_NAME="${2}" # what the .app bundle should be named

# If no install name is supplied, default to the name of the DMG
if [[ -z "${XCODE_INSTALL_NAME}" ]]; then
    XCODE_INSTALL_NAME=`find ${DOWNLOADED_DMG_PATH} -maxdepth 1 -exec basename {} \; | rev | cut -f 2- -d '.' | rev`".app"
fi

XCODE_INSTALL_LOCATION="${3}" # where Xcode should be installed

# If no custom install location is supplied, default to /Applications
if [[ -z "${XCODE_INSTALL_LOCATION}" ]]; then
    XCODE_INSTALL_LOCATION="/Applications"
fi

XCODE_INSTALL_PATH="${XCODE_INSTALL_LOCATION}/${XCODE_INSTALL_NAME}"
echo "DOWNLOADED_DMG_PATH=${DOWNLOADED_DMG_PATH}"
echo "XCODE_INSTALL_NAME=${XCODE_INSTALL_NAME}"
echo "XCODE_INSTALL_LOCATION=${XCODE_INSTALL_LOCATION}"
echo "XCODE_INSTALL_PATH=${XCODE_INSTALL_PATH}"
echo "======================================================"

# Mount the disk image
echo "hdiutil attach \"${DOWNLOADED_DMG_PATH}\""
hdiutil attach "${DOWNLOADED_DMG_PATH}"
echo "======================================================"

# Prepare install destination if it doesn’t exist
echo "mkdir \"${XCODE_INSTALL_LOCATION}\""
mkdir "${XCODE_INSTALL_LOCATION}"
echo "======================================================"

# Get the canonical path to the Xcode app bundle in the DMG
echo "XCODE_BUNDLE_PATH=\`find /Volumes/Xcode -maxdepth 1 -name \"Xcode*.app\"\`"
XCODE_BUNDLE_PATH=`find /Volumes/Xcode -maxdepth 1 -name "Xcode*.app"`
echo "XCODE_BUNDLE_PATH=${XCODE_BUNDLE_PATH}"
echo "======================================================"

# Copy the app bundle to the install location
echo "cp -R \"${XCODE_BUNDLE_PATH}\" \"${XCODE_INSTALL_PATH}\""
cp -R "${XCODE_BUNDLE_PATH}" "${XCODE_INSTALL_PATH}"
echo "======================================================"

# Unmount the DMG
echo "hdiutil detach /Volumes/Xcode"
hdiutil detach /Volumes/Xcode
echo "======================================================"

# Set new xcode as the preferred toolchain
echo "xcode-select -s \"${XCODE_INSTALL_PATH}\""
xcode-select -s "${XCODE_INSTALL_PATH}"
echo "======================================================"

# Accept the user license agreement
echo "xcodebuild -license accept"
xcodebuild -license accept
echo "======================================================"

# Install command line tools
echo "\"${XCODE_INSTALL_PATH}\" -installComponents"
"${XCODE_INSTALL_PATH}/Contents/MacOS/Xcode" -installComponents
echo "======================================================"
echo "Finished installing Xcode."



##########################################
#############. INSTALL TOOLS. ############
##########################################
echo "======================================================"
# Install Java
echo "Start installing Java."
brew cask install java
echo "======================================================"

# Install Android SDK
echo "Start installing Android SDK."
brew cask install android-sdk
echo 'export ANDROID_HOME=/usr/local/share/android-sdk' >>~/.bash_profile
source ~/.bash_profile
echo "======================================================"

# Install RVM
echo "Start installing RVM."
\curl -sSL https://get.rvm.io | bash -s stable --ruby
echo "======================================================"

# Install Fastlane
echo "Start installing Fastlane."
brew cask install fastlane
echo 'export PATH="$HOME/.fastlane/bin:$PATH"' >>~/.bash_profile
source ~/.bash_profile
echo "======================================================"

# Install RabbitMQ
echo "Start installing RabbitMQ."
brew install rabbitmq
echo 'export PATH=$PATH:/usr/local/sbin:$PATH' >>~/.bash_profile
source ~/.bash_profile
echo "======================================================"
# rabbitmq-server start
echo "Finished installing Tools."



##########################################
##########. INSTALL BUILDER. #############
##########################################
echo "======================================================"
# Create path to Script
echo "Start creating path to Script"
mkdir -p Code/Python/MobileScript
cd Code/Python/MobileScript
echo "======================================================"

# Clone Script
echo "Start clone Builder"
git clone https://$USERNAME_BITBUCKET:$PASSWORD_BITBUCKET@bitbucket.org/sargeras55/python-build-script.git
cd
echo "======================================================"

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
echo "======================================================"
echo "Finished installing Builder."
