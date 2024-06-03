#!/bin/bash
backup_dir="/caminho/para/backup"
source_dir="/caminho/para/fonte"
timestamp=$(date +"%Y%m%d%H%M%S")
tar -czf "$backup_dir/backup_$timestamp.tar.gz" "$source_dir"
