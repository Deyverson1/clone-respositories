import requests #library
import os

def clone_repositories(username, target_directory):
    response = requests.get(f"https://api.github.com/users/{username}/repos")

    if response.status_code == 200:
        for repo in response.json():
            repo_path = os.path.join(target_directory, repo['name'])
            os.system(f'git clone "{repo["clone_url"]}" "{repo_path}"')

            print("Done")
    else:
        print("No se pudo obtener la lista de repositorios.")

clone_repositories("Deyverson1", "C:/Users/Deyve/OneDrive/Documentos/Projects")
                    #Username and destination directory