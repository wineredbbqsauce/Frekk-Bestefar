#!/bin/bash

echo "======================================"
echo "Din Frekke Bestefar - Setup"
echo "======================================"
echo ""

# Colors for output
GREEN="\033[0;32m"
RED="\033[0;31m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"
MAGENTA="\033[0;35m"
CYAN="\033[0;36m"
NC="\033[0m" # No Colour

# Detect OS
echo "Detecting OS..."
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo -e "${BLUE}Detected:${NC} ${YELLOW}Linux${NC}"
    OS="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "${BLUE}Detected:${NC} ${YELLOW}macOS${NC}"
    OS="mac"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin"  ]]; then
    echo -e "${BLUE}Detected:${NC} ${YELLOW}Windows${NC}"
    OS="windows"
else
    echo -e "${RED}Unsupported OS"
    exit 1
fi

echo ""
echo "Sjekker om Python er installert"
if ! command  -v python3 &> /dev/null; then
    echo -e "${YELLOW}Python3 er ikke installert${NC}."
    echo -e "${CYAN}Installerer python3${NC}"

    if [ "$OS" == "linux" ]; then
        sudo apt update
        sudo apt install -y python3 python3-venv python3-pip
    elif [ "$OS" == "mac" ]; then
        if ! command -v brew &> /dev/null; then
            echo "Installerer Homebrew"
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        brew install python3
    elif [ "$OS" == "windows" ]; then
        echo -e "${RED}Please install Python3 from https://www.python.org${NC}"
        exit 1
    fi
    echo -e "${GREEN}✓  Python3 Installert${NC}"
else
    echo -e "${GREEN}✓  Python allerede installert: $(python3 --version)${NC}"
fi

echo ""


echo "Installerer .venv"
python3 -m venv .venv
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Installerte .venv${NC}"
else
    echo -e "${RED}Klarte ikke installere .venv${NC}"
    exit 1
fi

echo ""

echo "aktiverer .venv"
source .venv/bin/activate
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Aktiverte .venv${NC}"
else
    echo -e "${RED}Klarte ikke aktivere .venv${NC}"
    exit 1
fi

echo ""

echo "Installerer nødvendigheter"

echo ""
echo ""
echo ""

echo "Installerer discord"
pip install  discord==2.3.2
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Installerte discord${NC}"
else
    echo -e "${RED}Klarte ikke installere discord${NC}"
    exit 1
fi

echo ""

echo "Installerer python-dotenv"
pip install python-dotenv==1.0.0
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Installerte python-dotenv${NC}"
else
    echo -e "${RED}Klarte ikke installere python-dotenv${NC}"
    exit 1
fi

echo ""

echo "Installerer audioop-lts"
pip install audioop-lts
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Installerte audioop-lts${NC}"
else
    echo -e "${RED}Klarte ikke installere${NC}"
    exit 1
fi

echo ""

echo ""
echo -e "${GREEN}======================================"
echo "Alt installert! Vekker opp bestefar"
echo "======================================${NC}"
echo ""

python3 discord_bot.py