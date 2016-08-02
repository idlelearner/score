import subprocess

def pushad(intent):
	p = subprocess.Popen('/home/pi/Nuance/wuw/ad %s' % intent, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
		print(line)
	retval = p.wait()

if __name__ == "__main__":
	pushad()
