import requests, time
import json, sys

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer ",
    "X-GitHub-Api-Version": "2022-11-28"
}

repo_owner = "skylord0001"
repo_name = "some-github-script"
usernames_file = "three.json"

mentions = 0
usernames = []

with open(usernames_file, "r") as f:
    data = json.load(f)

for username in data:
    usernames.append(f"@{username}")
    if len(usernames)%50 == 0:
        
        # Create an issue
        issue_data = {"title": "Automated Issue (Come to Python)", "body": "![image](https://github.com/user-attachments/assets/3d4e72a2-8333-4f10-beef-14849bb600db)."}
        issue_response = requests.post(f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues", headers=headers, json=issue_data)
        issue = issue_response.json()
        issue_number = issue.get("number")
        if not issue_number:
            print(issue)
            print("Failed to create issue.")
            sys.exit()
        print("<<<<<<<<<<<<<<<<<<<<<<===============================================================================>>>>>>>>>>>>>>>>>>>")
        print(f"Issue #{issue_number} created and open")

        # Add comments to the issue
        users = " ".join(usernames)
        comment = f"{users}\n\n\nHi all,\n\n ![image](https://github.com/user-attachments/assets/3d4e72a2-8333-4f10-beef-14849bb600db)\n\nfeel free to check out some of my Python projects here: https://github.com/devfemibadmus and give them some stars if you find them interesting! :heart: :smile:"
        mentions += len(usernames)
        response = requests.post(f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}/comments", headers=headers, json={"body": comment})
        response = response.json()
        print("<<<<<<<<<<<<<<<<<<<<<<===============================================================================>>>>>>>>>>>>>>>>>>>")
        print(f"Adding comments: {response.get('url')}")
        usernames.clear()

        # Close and lock the issue
        requests.patch(f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}", headers=headers, json={"state": "closed"})
        requests.put(f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}/lock", headers=headers)
        print("<<<<<<<<<<<<<<<<<<<<<<===============================================================================>>>>>>>>>>>>>>>>>>>")
        print(f"Issue #{issue_number} closed and locked.")
        time.sleep(15)

