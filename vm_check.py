def vm_check():
	from getmac import get_mac_address as gma

	mac=gma()

	#print(mac)

	x = requests.get('https://api.macvendors.com/'+mac)

	#print(x.text)
	if x.text =='Microsoft Corporation' or x.text=='Xensource, Inc.' or x.text=='VMware, Inc.' :
	        print('Its a vm')
	        vm_test=1
	else:
	        print('Not a vm')
	        vm_test=0

	if vm_test==1:
		exit()
        
vm_check()