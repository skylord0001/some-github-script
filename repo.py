import requests, json, time

usernames = []

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer ",
    "X-GitHub-Api-Version": "2022-11-28"
}

def get_stargazers_username(user, repository, maximum):
    with open("data.json", "w") as f:
        if f.tell() == 0:
            f.write("[\n")
        for username, repo in zip(user, repository):
            response = requests.get(f'https://api.github.com/repos/{username}/{repo}', headers=headers)
            resp = response.json()
            repo_stat = resp.get('stargazers_count')
            if not repo_stat:
                print(resp)
                print("closed")
                return
            time.sleep(1)
            start = 0
            if repo_stat > maximum:
                start = (repo_stat - maximum)//100
            for i in range(30):
                response = requests.get(f"https://api.github.com/repos/{username}/{repo}/stargazers?page={start+i}&per_page=100", headers=headers)
                stargazers = response.json()
                # print(stargazers)
                for user in stargazers:
                    json.dump(user["login"], f)
                    f.write(",\n")
                print(f"Got: {(i+1)*100}/maximum Page: {start + i} Repo: https://github.com/{username}/{repo}")
                if i%60 ==0:
                    time.sleep(11)
        f.seek(f.tell() - 3)
        f.write("\n]\n")
        f.close()

get_stargazers_username(['imputnet'], ['cobalt'], 5000)


