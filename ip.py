from ip2geotools.databases.noncommercial import DbIpCity

print("""
.___
|   |_____
|   \____ \
|   |  |_> >
|___|   __/
    |__|
""")

ip = input("enter ip")

response = DbIpCity.get(f'{ip}', api_key='free')
response.ip_address
print(response)
