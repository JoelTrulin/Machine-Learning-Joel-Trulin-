#!/bin/bash
sudo mkfs -t ext4  /dev/nvme0n1

sudo mount /dev/nvme0n1 /my-byte

echo "In progress" > /my-byte/status.txt

python3 usr/local/bin/joel_git.py

python3 usr/local/bin/joel_template.py

sudo pip cache purge

chown -R azureuser:azureuser /my-byte

echo "Done" > /my-byte/status.txt
