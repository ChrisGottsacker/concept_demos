import subprocess
exitStatus = subprocess.call('dir', shell = True)
if(exitStatus):	# call failed, so maybe this machine is running Linux
	subprocess.call('ls', shell = True)
