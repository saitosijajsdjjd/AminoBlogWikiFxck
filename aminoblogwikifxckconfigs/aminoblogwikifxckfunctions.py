import amino
import asyncio
import terminal_banner

def mainmenu():
	print(terminal_banner.Banner("""
[1] Spam Blog
[2] Spam Wiki
"""))

async def spampost():
	print("Selected Spam Blog")
	client = amino.Client()
	email = input("Email >> ")
	password = input("Password >> ")
	await client.login(email=email, password=password)
	clients = await client.sub_clients(start=0, size=1000)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	communityid = clients.comId[int(input("Select the community >> "))-1]
	sub_client = await amino.SubClient(comId=communityid, profile=client.profile)
	posttitle = input("Blog Title >> ")
	postcontent = input("Blog Content >> ")
	while True:
		try:
			await sub_client.post_blog(title=posttitle, content=postcontent, backgroundColor="#000000")
			print("Created Blog")
		except amino.lib.util.exceptions.VerificationRequired as e:
			print(f"VerificationRequired")
			link = e.args[0]['url']
			print(link)
			verify = input("Waiting for verification >> ")
		except Exception as e:
			print(e)
		except:
			print("Don't Created Post")
			pass

async def spamwiki():
	print("Selected Spam Wiki")
	client = amino.Client()    
	email = input("Email >> ")
	password = input("Password >> ")
	await client.login(email=email, password=password)
	clients = await client.sub_clients(start=0, size=1000)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	communityid = clients.comId[int(input("Select the community >> "))-1]
	sub_client = await amino.SubClient(comId=communityid, profile=client.profile)
	wikititle = input("Wiki Title >> ")
	wikicontent = input("Wiki Content >> ")
	while True:
		try:
			await sub_client.post_wiki(title=wikititle, content=wikicontent, backgroundColor="#000000")
			print("Created Wiki")
		except amino.lib.util.exceptions.VerificationRequired as e:
			print(f"VerificationRequired")
			link = e.args[0]['url']
			print(link)
			verify = input("Waiting for verification >> ")
		except Exception as e:
			print(e)
		except:
			print("Don't Created wiki")
			pass
