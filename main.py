# -*- coding: utf-8 -*- 
import sys, urllib, os

print "Administrator Rights Required "
print "Break the Wall \n"

def installation():
	# this is the url from where I get the hosts content
	# this url might be not accessible in the future
	url = "http://smartladder.googlecode.com/svn/hosts/pc/hosts"
	wp = urllib.urlopen(url)
	new_hosts_content = wp.read()

	os_name = os.name
	if os_name == "nt":
		print "Windows Operating System"
		folder_path = "C:\Windows\System32\drivers\etc"
		backup_file_name = folder_path + "\hosts_copy"
		hosts_file = folder_path + "\hosts"
	else:
		print ".Nix Operating System"
		folder_path = "/etc"
		backup_file_name = folder_path + "/hosts_copy"
		hosts_file = folder_path + "/hosts"

	if os.path.exists(backup_file_name):
		print "Backup already existed"
	else:
		print "Make Backup"
		# make backup
		orig = open(hosts_file) # open file
		content = orig.readlines() # get content
		orig.close() # close file

		backup = open(backup_file_name, "w")
		backup.writelines(content)
		backup.close()


		print "Finish Backup"

	f = open(hosts_file, "w") # open file
	f.writelines(new_hosts_content)
	f.close()

	print "Finish Changing hosts file"


def uninstallation():
	print "Begin to uninstall"
	os_name = os.name
	if os_name == "nt":
		print "Windows Operating System"
		folder_path = "C:\Windows\System32\drivers\etc"
		backup_file_name = folder_path + "\hosts_copy"
		hosts_file = folder_path + "\hosts"
	else:
		print ".Nix Operating System"
		folder_path = "/etc"
		backup_file_name = folder_path + "/hosts_copy"
		hosts_file = folder_path + "/hosts"

	if os.path.exists(backup_file_name):
 		backup = open(backup_file_name)
 		backup_content = backup.readlines()
 		backup.close()

 		f = open(hosts_file, "w")
 		f.writelines(backup_content)
 		f.close()
 	else:
 		pass 
 	print "Uninstall successfully"

print "###################"
print "Press 1 to install"
print "Press 2 to uninstall"

selection = int(input())
if selection == 1:
	print "Begin to install ;)"
 	installation()
 	print "Install successfully :)"
elif selection == 2:
 	uninstallation()
else:
 	print "Invalid command"
 	pass
