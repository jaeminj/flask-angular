sudo apt-get -y remove npm
sudo apt-get -y remove node
sudo apt-get autoremove
sudo apt-get update
sudo apt-get -y install nodejs
sudo ln -s /usr/bin/nodejs /usr/bin/node
