import rsa

for i in range(10):
    (a, privkey) = rsa.newkeys(136)
    a = a.save_pkcs1().splitlines()[1:-1]
    address = a[0].decode('utf-8')

    print(len(address))