import requests
import asyncio
import aiohttp

google_sub_dict = {}
possible_subdomain_list=[]
with open("subdomain.txt","r") as subdomain:
    for word in subdomain:
        word=word.strip()
        url="https://"+word+"."+"google.com"
        possible_subdomain_list.append(url)



async def check(session,url,google_sub_dict):
        try:
            async with session.get(url) as response:
                google_sub_dict[url]="it exists"
        except:
            google_sub_dict[url]="it doesnt exist"
async def mainn(possible_subdomain_list):


    async with aiohttp.ClientSession() as session:
        tasks=[]
        for url in possible_subdomain_list:
            tasks.append(asyncio.create_task(check(session,url,google_sub_dict)))
        await asyncio.gather(*tasks)
asyncio.run(mainn(possible_subdomain_list))
print(google_sub_dict)













