sudo apt update
sudo apt install bash-completion
sudo apt-get install auditd
sudo chmod -R u+rw /var/log/audit
sudo chmod -R u+rw /etc/audit
poetry install