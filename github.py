import requests, json, time

url = "https://api.github.com/repos/blackstackhub/blackstackhub/issues/5/comments"
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer ",
    "X-GitHub-Api-Version": "2022-11-28"
}

with open('data.json', 'r') as file:
    data = json.load(file)
usernames = []
mentions = 0
for state, users in data.items():
    for user in users:
        username = f"@{(user['profile_url']).replace('https://github.com/', '')}"
        usernames.append(username)
        if len(usernames)%50 == 0:
            users = " ".join(usernames)
            comment = f"{users}\n\n\nHi all,\n\nYou're invited to join Black Stack Hub!\nDive into live projects, whether you're into backend, frontend, cloud, or just starting out. Build, grow, and innovate together with our vibrant community.\n\nJoin here: https://whatsapp.com/channel/0029Vay3l3F7dmejaNTEq82G \n\nBest regards,\nBlack Stack Hub"
            print(users)
            mentions +=len(usernames)
            response = requests.post(url, headers=headers, json={"body": comment})
            response = response.json()
            print(f"sending: {len(usernames)}, sent: {mentions}")
            print("<<<<<<<<<<<<<<<<<<<<<<===============================================================================>>>>>>>>>>>>>>>>>>>")
            print(response.get('url'))
            print("<<<<<<<<<<<<<<<<<<<<<<===============================================================================>>>>>>>>>>>>>>>>>>>")
            usernames.clear()
            time.sleep(10)

