#!/usr/bin/env python3
'''Lab 3 Part 4 script - free disk space'''
# Author ID: 123964215

import subprocess

def free_space():
    try:
        
        df_process = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
        grep_process = subprocess.Popen(['grep', '/$'], stdin=df_process.stdout, stdout=subprocess.PIPE)
        awk_process = subprocess.Popen(['awk', '{print $4}'], stdin=grep_process.stdout, stdout=subprocess.PIPE)
        
        
        output, _ = awk_process.communicate()
        return output.decode('utf-8').strip()
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    print(free_space())
