import uuid

def get_mac_address():
    mac = uuid.getnode()

    mac_address = ':'.join(
        f'{(mac >> i) & 0xff:02x}'
        for i in range(40, -1, -8)
    )

    return mac_address

print("MAC Address Finder")
print("------------------")

mac = get_mac_address()

print("MAC Address:", mac)