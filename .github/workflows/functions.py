import json
from re import split
import urllib.request

def get_latest_release_download(owner, repository):
    releaseData = json.loads(urllib.request.urlopen(f"https://api.github.com/repos/{owner}/{repository}/releases/latest").read())
    urls = ""

    for release in releaseData['assets']:
        urls += release['browser_download_url'] + " "
    
    return urls