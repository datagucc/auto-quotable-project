import os
import requests
import datetime
import subprocess

API_URL = "https://v2.jokeapi.dev/joke/Any?type=single"

def fetch_joke():
    """Récupère une blague depuis l'API."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return data["joke"]
    else:
        return "Impossible de récupérer une blague."

def update_file():
    """Met à jour le fichier joke.txt avec une nouvelle blague."""
    joke = fetch_joke()
    with open("joke.txt", "w") as file:
        file.write(joke)
    return joke

def git_commit_push():
    """Ajoute, commit et push les changements sur GitHub."""
    today = datetime.date.today().strftime("%Y-%m-%d")
    subprocess.run(["git", "add", "joke.txt"])
    subprocess.run(["git", "commit", "-m", f"Update joke {today}"])
    subprocess.run(["git", "push", "origin", "main"])

if __name__ == "__main__":
    update_file()
    git_commit_push()
    #print('it worked')
