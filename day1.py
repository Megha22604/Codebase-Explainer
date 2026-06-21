from github import Github
from dotenv import load_dotenv 
import os

load_dotenv()

g=Github(os.getenv("GITHUB_TOKEN"))

repo_url=input("ENter ur github repo here")

parts=repo_url.strip("/").split("/")
repo_name=f"{parts[-2]}/{parts[-1]}"

repo=g.get_repo(repo_name)

print(f"\n📦 Repo: {repo.name}")
print(f"📝 Description: {repo.description}")
print(f"⭐ Stars: {repo.stargazers_count}")
print("\n📁 Files found:\n")


def print_files(path=""):
    contents = repo.get_contents(path)
    file_count = 0
    folder_count = 0
    py_count = 0
    html_count = 0

    for item in contents:
        if item.type == "dir":
            folder_count += 1
            sub_files, sub_folders, sub_py, sub_html = print_files(item.path)
            file_count += sub_files
            folder_count += sub_folders
            py_count += sub_py
            html_count += sub_html
        else:
            print(f" {item.path}")
            file_count += 1
            if item.name.lower().endswith(".py"):
                py_count += 1
            elif item.name.lower().endswith(".html"):
                html_count += 1

    return file_count, folder_count, py_count, html_count

repo_files=[]
count, total, pyc, htmc = print_files()
print(f"The number of files are: {count}")
print(f"The number of folders are: {total}")
print(f"Python files: {pyc}")
print(f"HTML files: {htmc}")

print("Hellooooooooooooooooooooooooooooooooooooooo")
