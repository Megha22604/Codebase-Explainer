from github import Github,Auth
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

auth=Auth.Token(os.getenv("GITHUB_TOKEN"))
github_client=Github(auth=auth)
client_ai= genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SKIP_EXTENSIONS={'.png','.jpg','.gif','.svg','.ico','.zip','.pdf','.lock'}

#file contents ko collect karo

def collect_files(repo,path="",file_data={}):
    contents=repo.get_contents(path)
    for item in contents:
        if item.type=="dir":
            collect_files(repo,item.path,file_data)
        else:
            ext=os.path.splitext(item.name)[1].lower()
            if ext in SKIP_EXTENSIONS:
                continue
            try:
                content=item.decoded_content.decode("utf-8")
                file_data[item.path]=content
            except Exception as e:
                print(f"Skipped {item.path}: {e}")
    return file_data

#building prompts

def build_prompt(file_data):
    files_text=""
    for path,content in list(file_data.items())[:20]:
        files_text += f"\n### {path}\n```\n{content[:600]}\n```\n"

    prompt=f"""

You are a senior developer helping a new team member understand a codebase.
Here are the files from project:
{files_text}

Respond in exactly this format with this exact section headers 
##Project summary
Write 2-3 sentences about what this project does

##Tech Stack
List each technology on a new line starting with -

##File breakdown
For each important file write:
filename: what it does

#How to start
List 4-5 steps a new developer should follow to understand this codebase

##Gotchas
List any non-obvious things to watch out for

Keep the explanation begineer friendly and clear
"""
    return prompt



#send to gemini and get response

def ask_gemini(prompt):
    print("🤖 Sending to gemini API....")
    response=client_ai.models.generate_content(
          model="gemini-2.5-flash",
          contents=prompt
    )
    
    
    return response.text

# main kaam
def main():
    repo_url=input ("Enter ur repo url: ").strip()

    parts=repo_url.split("/")
    repo_name=f"{parts[-2]}/{parts[-1]}"

    print("📥 Fetching some data from github...")
    repo=github_client.get_repo(repo_name)
    file_data=collect_files(repo)
    print(f"✅Collected {len(file_data)} files")

    print("\n📝 Building prompt...")
    prompt = build_prompt(file_data)
    print(f"✅ Prompt ready ({len(prompt)} characters)")

    analysis = ask_gemini(prompt)

    print("\n" + "="*50)
    print("🧠 CLAUDE'S ANALYSIS")
    print("="*50)
    print(analysis)

main()
