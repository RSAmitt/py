# !/bin/bash
sudo apt update && apt upgrade -y
sudo apt install git && apt install tree -y
mkdir github
cd github
touch f1 f2
git init
git add .
git commit -m "shell file run "
git log 
git add origin https://github.com/RSAmitt/py.git
git clone https://github.com/RSAmitt/py.git

