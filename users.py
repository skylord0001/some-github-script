import requests, json, time

usernames = []

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer ",
    "X-GitHub-Api-Version": "2022-11-28"
}
base_url = "https://api.github.com/search/users?q=language:Python+repos:1+type:users&sort=joined&page={}&per_page=100"

def fetch_usernames():
    total_gotten = 0
    with open("one.json", "w") as f:
        f.write("[\n")
        for page in range(1, 11):
            response = requests.get(base_url.format(page), headers=headers)
            users = response.json().get('items', [])
            if not users:
                break
            total_gotten += len(users)
            for user in users:
                json.dump(user["login"], f)
                f.write(",\n")
            print(f"Page {page}: Got {len(users)} users. Total: {total_gotten}")
            time.sleep(1)
        f.seek(f.tell() - 3)
        f.write("\n]\n")

fetch_usernames()
