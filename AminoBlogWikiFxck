import amino
import asyncio
import pyfiglet
import terminal_banner
from aminoblogwikifxckconfigs import aminoblogwikifxckfunctions
from colored import fore, back, style, attr
attr(0)
print(fore.RED_3A + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminoblogwikifxck", font="small"))
aminoblogwikifxckfunctions.mainmenu()
select = input("Select >> ")

if select == "1":
	asyncio.get_event_loop().run_until_complete(aminoblogwikifxckfunctions.spampost())

elif select =="2":
	asyncio.get_event_loop().run_until_complete(aminoblogwikifxckfunctions.spamwiki())
