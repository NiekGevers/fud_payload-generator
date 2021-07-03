# fud_payload-generator
A fully undetectable payload generator in python. working in 2021.

![alt text](https://i.ibb.co/DMs9xp0/virustotal-result.png)

## How to install

git clone https://github.com/NiekGevers/fud_payload-generator.git  
cd fud_payload-generator  
python fud_payload-generator.py

## How to use
When running you need to specify the listening host and port after this you can also
try to convert the .ps1 payload to exe with a program like ps2exe (if converting to exe there is a higher change your antivirus will detect it!).

Now you can set up a listener like netcat to recieve your connection.

## About the script
This script basically takes the payloads from the payloads folders and changes
certain things like the lhost and lport to make things easier.
You can now also add a custom fake msg box.

