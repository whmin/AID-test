import re
import sys

def get_address(port):
    f=open('/Users/whm/Desktop/Tmooc/课件/re/1.txt')
    kv={}
   
    while True:
        data=''
        for line in f:
            if line!='\n':
                data+=line
            else:
                break
        # print('===========')
        # print(data)
        if not data:
            return 'Not found the port'
        PORT=re.split(r'\s+',data)[0]
        if PORT==port:
        
            # pattern=r'address is (\w{4}\.\w{4}\.\w{4})'
            pattern=r'Internet address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknown)'

            try:
                address=re.search(pattern,data).group(1)
                return(address)
            except:
                return('Not found the port')
        
    f.close()
    return kv
    



if __name__=='__main__':
    port=sys.argv[1]
    print(get_address(port))