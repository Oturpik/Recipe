#!/bin/bash

# Backup directory
backup_dir="/home/users/Azubi"

# Source file to be backed up
source_file="/home/users/Azubi/backuprecord.txt"

# Backup script
cp "$source_file" "$backup_dir/$(date +%Y%m%d%H%M%S)_personal_records.bak"
