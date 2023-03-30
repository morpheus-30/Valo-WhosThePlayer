import requests
import urllib.request


def BasicplayerData(Username, region="ap"):
    name = ""
    tag = ""
    name = Username.split("#")[0]
    tag = Username.split("#")[1]
    # print(name)
    # print(tag)
    PLAYERdata = requests.get(
        "https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}".format(name=name, tag=tag))
    # print(PLAYERdata.json())
    MMRdata = requests.get(
        "https://api.henrikdev.xyz/valorant/v1/mmr/{region}/{name}/{tag}".format(name=name, tag=tag, region=region))
    # print(MMRdata.json())
    if(PLAYERdata.json()["status"] == 200):
        PLAYERdatasorted = {
            "name": PLAYERdata.json()["data"]["name"],
            "tag": PLAYERdata.json()["data"]["tag"],
            "rank": (MMRdata.json()["data"]["currenttierpatched"] if MMRdata.json()["data"]["currenttierpatched"] != None else "Unranked"),
            "RR": (MMRdata.json()["data"]["ranking_in_tier"] if MMRdata.json()["data"]["ranking_in_tier"] != None else 0),
            "account_level": PLAYERdata.json()["data"]["account_level"],
            "region": PLAYERdata.json()["data"]["region"],
            "cardURL": PLAYERdata.json()["data"]["card"]["large"],
            "lastONLINE": PLAYERdata.json()["data"]["last_update"],
            "cardURLs": PLAYERdata.json()["data"]["card"],
            "rankImage": (MMRdata.json()["data"]["images"]["small"] if MMRdata.json()["data"]["images"] != None else "Not Found"),
        }
        

    else:
        PLAYERdatasorted = {
            "name": "Not Found",
            "tag": "Not Found",
            "rank": "Not Found",
            "RR": 0,
            "account_level": 0,
            "region": "Not Found",
            "cardURL": "Not Found",
            "lastONLINE": "Not Found",
            "cardURLs": {
                "large": "Not Found",
                "small": "Not Found",
                "wide": "Not Found",
            },
            "rankImage": "Not Found",
        }

    return PLAYERdatasorted


def MatchHistoryData(Username, filter=""):
    name = ""
    tag = ""
    name = Username.split("#")[0]
    tag = Username.split("#")[1]
    isFilter = filter if filter == "" else "?filter={filter}".format(
        filter=filter)
    MatchData = requests.get(
        "https://api.henrikdev.xyz/valorant/v3/matches/ap/{name}/{tag}{filter}".format(name=name, tag=tag, filter=isFilter))
    print(MatchData.json())
    if MatchData.json()["status"] == 200:
        MatchDatasorted = map(lambda x: {
            "map": x["metadata"]["map"],
            "gameStart": x["metadata"]["game_start_patched"],
            "mode": x["metadata"]["mode"],
            "server": x["metadata"]["cluster"],
            "teamPlayers": list(map(lambda y: {
                "name": y["name"],
                "tag": y["tag"],
            }, x["players"]["blue"])),
            "isWin": x["teams"]["blue"]["has_won"],
        }, MatchData.json()["data"])
    else:
        MatchDatasorted = []
    return list(MatchDatasorted)
