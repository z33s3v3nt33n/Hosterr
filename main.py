import requests


if __name__ == '__main__':

    hosts_file = open('HOSTS','r')
    valid = "Cloudflare"

    user_agent = {
	"User-Agent" : "Browser: Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36"
    }
    print("\n*** Creator : @z33s3v3nt33n_scr1pts [telegram channel] ***")
    print("\n[-] Starting.....")
    for host in hosts_file:
        host = host.strip('\n')
        host2 = host
        host = "http://check-host.net/ip-info?host=" + host
        response = requests.get(host,headers=user_agent,verify=False)
        if(valid in response.text):
            print(f'[-] Checking {host2} -> Valid Host ! {valid} Found In Response 🗸')
            with open("HOSTS_FOUND","a") as mano:
                mano.write(host2+"\n")
        else:
            print(f'[-] Checking {host2} -> Invalid Host !')
    print("\nPOSSIBLE HOSTS HAVE BEEN WRITTEN TO HOSTS_FOUND... GET TO TESTING")
