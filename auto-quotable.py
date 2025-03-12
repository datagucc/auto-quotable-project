import os
# Change the working directory to your Git repository
os.chdir('/Users/focus_profond/GIT_repo/auto-quotable-project')
import requests
import datetime
import subprocess

API_URL = "https://v2.jokeapi.dev/joke/Any?type=single"

def fetch_joke():
    """Retrieves a joke from the API."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return data["joke"]
    else:
        return "Impossible to recover a joke."

def update_file():
    """Updates the joke.txt file with a new joke."""
    joke = fetch_joke()
    with open("joke.txt", "w") as file:
        file.write(joke)
    return joke

def git_commit_push():
    """Adds, commits and pushes changes to GitHub."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    now = datetime.datetime.now()
    subprocess.run(["git", "add", "joke.txt"])
    subprocess.run(["git", "commit", "-m", f"Update joke {today}, {now}"])
    subprocess.run(["git", "push", "origin", "main"])

if __name__ == "__main__":
    update_file()
    git_commit_push()
    #print('it worked')
