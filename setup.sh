#!/bin/bash
# Auto Install Script for Sk Parvez SMS Bomber
# Run: bash <(curl -Ls https://raw.githubusercontent.com/skparvez/all_in_one_63/main/setup.sh)

RED='\033[0;91m'
GREEN='\033[0;92m'
YELLOW='\033[0;93m'
BLUE='\033[0;94m'
MAGENTA='\033[0;95m'
CYAN='\033[0;96m'
WHITE='\033[0;97m'
BOLD='\033[1m'
RESET='\033[0m'

clear

echo -e "${MAGENTA}${BOLD}"
cat << "EOF"
╔══════════════════════════════════════════════════╗
║                                                  ║
║    ║                                                  ║
║        █▀█ ▄▀█ █▀█ █░█ █▀▀ ▀█▀                   ║
║        █▀▀ █▀█ █▀▄ █▄█ ██▄ ░█░                   ║
║                                                  ║
║                 P A R V E Z                      ║
║                                                  ║            ░                 ║
║                                                  ║
║    ╔══════════════════════════════════════╗     ║
║    ║    SK PARVEZ SMS BOMBER INSTALLER    ║     ║
║    ╚══════════════════════════════════════╝     ║
║                                                  ║
║    Admin    : Sk Parvez                          ║
║    Telegram : @all_in_one_63                     ║
║    Version  : 3.0 Pro                            ║
║                                                  ║
╚══════════════════════════════════════════════════╝
EOF
echo -e "${RESET}"

echo -e "${GREEN}[*] Starting Installation...${RESET}"
sleep 2

# Update packages
echo -e "${YELLOW}[1] Updating Termux packages...${RESET}"
pkg update -y && pkg upgrade -y
pkg install python -y
pkg install git -y
pkg install curl -y
pkg install wget -y

# Install Python packages
echo -e "${YELLOW}[2] Installing Python modules...${RESET}"
pip install --upgrade pip
pip install requests
pip install colorama
pip install datetime

# Create directory
echo -e "${YELLOW}[3] Creating installation directory...${RESET}"
cd ~
rm -rf sk_parvez_bomber
mkdir sk_parvez_bomber
cd sk_parvez_bomber

# Download main bomber
echo -e "${YELLOW}[4] Downloading SMS Bomber...${RESET}"
curl -s -o bomber.py https://raw.githubusercontent.com/skparvez/all_in_one_63/main/bomber.py
curl -s -o config.json https://raw.githubusercontent.com/skparvez/all_in_one_63/main/config.json
curl -s -o admin_panel.py https://raw.githubusercontent.com/skparvez/all_in_one_63/main/admin_panel.py

# Make executable
chmod +x bomber.py
chmod +x admin_panel.py

# Create launcher
echo -e "${YELLOW}[5] Creating launcher...${RESET}"
cat > ~/sms.sh << EOL
#!/bin/bash
cd ~/sk_parvez_bomber
python bomber.py
EOL

chmod +x ~/sms.sh

# Create alias
echo -e "${YELLOW}[6] Creating command alias...${RESET}"
echo "alias sms='cd ~/sk_parvez_bomber && python bomber.py'" >> ~/.bashrc
echo "alias parvez-sms='cd ~/sk_parvez_bomber && python bomber.py'" >> ~/.bashrc
echo "alias bomber='cd ~/sk_parvez_bomber && python bomber.py'" >> ~/.bashrc

# Final message
clear
echo -e "${GREEN}${BOLD}"
cat << "EOF"
╔══════════════════════════════════════════════════╗
║                                                  ║
║         INSTALLATION COMPLETED SUCCESSFULLY!     ║
║                                                  ║
╚══════════════════════════════════════════════════╝
EOF
echo -e "${RESET}"

echo -e "${CYAN}${BOLD}"
echo "╔══════════════════════════════════════════════════╗"
echo "║             AVAILABLE COMMANDS                   ║"
echo "╠══════════════════════════════════════════════════╣"
echo "║                                                  ║"
echo "║  ${GREEN}sms${CYAN}              - Start SMS Bomber        ║"
echo "║  ${GREEN}parvez-sms${CYAN}       - Start SMS Bomber        ║"
echo "║  ${GREEN}bomber${CYAN}           - Start SMS Bomber        ║"
echo "║  ${GREEN}cd ~/sk_parvez_bomber${CYAN} - Go to bomber directory ║"
echo "║                                                  ║"
echo "║  ${YELLOW}Or simply run:${CYAN}                           ║"
echo "║  ${WHITE}python bomber.py${CYAN}                         ║"
echo "║                                                  ║"
echo "╚══════════════════════════════════════════════════╝"
echo -e "${RESET}"

echo -e "${MAGENTA}"
echo "Admin    : Sk Parvez"
echo "Telegram : @all_in_one_63"
echo "Password : Parvez"
echo -e "${RESET}"

echo -e "${YELLOW}[!] Please restart Termux or run:${RESET}"
echo -e "${WHITE}source ~/.bashrc${RESET}"
echo ""
echo -e "${GREEN}[*] To start, type: ${WHITE}sms${RESET}"
echo ""

# Load new alias
source ~/.bashrc 2>/dev/null

echo -e "${BLUE}[*] Installation completed! Enjoy bombing 😍${RESET}"