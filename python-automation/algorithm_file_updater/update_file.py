# Algorithm File Updater: Managing access control lists with Python

import_file = "allow_list.txt"
remove_list = ["192.168.1.105", "192.168.1.140"]

# Read the allowed IP addresses from the file
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert the string into a list of IP addresses
ip_list = ip_addresses.split()

# Remove IPs that are no longer authorized
for element in remove_list:
    if element in ip_list:
        ip_list.remove(element)

# Convert the updated list back into a string separated by newlines
updated_ip_addresses = "\n".join(ip_list)

# Overwrite the file with the updated list of allowed IPs
with open(import_file, "w") as file:
    file.write(updated_ip_addresses)

print("[+] Access control list successfully updated.")
