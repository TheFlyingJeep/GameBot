import requests
from bs4 import BeautifulSoup
from threading import Thread
results = dict()


people = {
    "hiley": ["TheFlyingJeep", "5829"],
    "teky": ["Teky1", "NA1"],
    "grass": ["Grassias", "NA1"],
    "gavin": ["THR33ZZ", "8980"],
    "bran": ["briancell", "bran"]
}


async def get_all_peoples_ranks(ctx):
    threads = []
    for key in people:
        threads.append(Thread(target=get_rank, args=(key, people[key])))

    for i in threads:
        i.start()

    for i in threads:
        i.join()

    out = "```\n"
    for k in results:
        out += f"{k} is currently in {results[k]}\n"
    out += "```"
    await ctx.send(out)


def get_rank(name, ign):
    url = f"https://tracker.gg/valorant/profile/riot/{ign[0]}%23{ign[1]}/overview"
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    mydiv = soup.find_all("div", {"class": "value"})
    results[name] = mydiv[0].text.strip()


async def register(ctx, n, i, nick):
    data = requests.get(f"https://tracker.gg/valorant/profile/riot/{n}%23{i}/overview")
    if data == "<Response [404]>":
        await ctx.send("I can't find this valorant user")
        return
    people[nick] = []
    people[nick].append(n)
    people[nick].append(i)
    await ctx.send("User is registered")