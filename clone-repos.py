import requests #library
import os

def clone_repositories(username, target_directory):
    response = requests.get(f"https://api.github.com/users/{username}/repos")

    if response.status_code == 200:
        for repo in response.json():
            os.system(f"git clone {repo['clone_url']} {target_directory}/{repo['name']}")
    else:
        print("No se pudo obtener la lista de repositorios.")

clone_repositories("Deyverson1",  "/home/valhalla/Documentos/Projects/")
                    #Username and destination directory