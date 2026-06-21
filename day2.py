from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

g = Github(os.getenv("GITHUB_TOKEN"))

repo_url = input("Enter GitHub repo URL: ")
parts = repo_url.strip("/").split("/")
repo_name = f"{parts[-2]}/{parts[-1]}"

repo = g.get_repo(repo_name)

# Files to skip (binary files will crash if decoded)
SKIP_EXTENSIONS = {'.png', '.jpg', '.gif', '.svg',
                   '.ico', '.zip', '.pdf', '.lock'}

def read_files(path=""):
    contents = repo.get_contents(path)
    for item in contents:
        if item.type == "dir":
            read_files(item.path)        # recursion — same as Day 1
        else:
            ext = os.path.splitext(item.name)[1].lower()
            if ext in SKIP_EXTENSIONS:
                print(f"\n⏭️  Skipping: {item.path}")
                continue                 # skip binary files

            try:
                content = item.decoded_content.decode("utf-8")
                print(f"\n{'='*50}")
                print(f"📄 FILE: {item.path}")
                print(f"{'='*50}")
                print(content[:500])     # print first 500 chars only
                print(f"... ({len(content)} total characters)")
            except Exception as e:
                print(f"❌ Could not read {item.path}: {e}")

read_files()