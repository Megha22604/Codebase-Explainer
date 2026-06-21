from github import Github,Auth
from dotenv import load_dotenv
from google import genai
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
import os

load_dotenv()

console=Console()

auth=Auth.Token(os.getenv("GITHUB_TOKEN"))
github_client=Github(auth=auth)
client_ai=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SKIP_EXTENSIONS = {'.png', '.jpg', '.gif', '.svg','.ico', '.zip', '.pdf', '.lock'}

def collect_files(repo, path="", file_data={}):
    contents = repo.get_contents(path)
    for item in contents:
        if item.type == "dir":
            collect_files(repo, item.path, file_data)
        else:
            ext = os.path.splitext(item.name)[1].lower()
            if ext in SKIP_EXTENSIONS:
                continue
            try:
                content = item.decoded_content.decode("utf-8")
                file_data[item.path] = content
            except Exception as e:
                print(f"⏭️  Skipped {item.path}: {e}")
    return file_data


# Updated prompt — forces structured response
def build_prompt(file_data):
    files_text = ""
    for path, content in list(file_data.items())[:20]:
        files_text += f"\n### {path}\n```\n{content[:600]}\n```\n"

    prompt = f"""
You are a senior developer helping a new team member understand a codebase.

Here are the files from the project:
{files_text}

Respond in EXACTLY this format with these exact section headers:

## PROJECT SUMMARY
Write 2-3 sentences about what this project does.

## TECH STACK
List each technology on a new line starting with -

## FILE BREAKDOWN
For each important file write:
filename: what it does

## HOW TO START
List 3-5 steps a new developer should follow to understand this codebase.

## GOTCHAS
List any non-obvious things to watch out for.
"""
    return prompt

 # Send to Gemini
def ask_gemini(prompt):
    console.print("\n[bold cyan]🤖 Sending to Gemini API...[/bold cyan]")
    response = client_ai.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def parse_response(text):
    sections = {}
    current_section = None
    current_content = []

    for line in text.splitlines():       # ← handles \r\n and \n both
        stripped = line.strip()          # ← removes hidden spaces/chars
        if stripped.startswith("## "):
            if current_section:
                sections[current_section] = "\n".join(current_content).strip()
            current_section = stripped.replace("## ", "").strip()
            current_content = []
        else:
            current_content.append(line)

    if current_section:
        sections[current_section] = "\n".join(current_content).strip()

    return sections

# NEW — Display sections beautifully
def display_report(sections, repo_url):
    console.print(f"\n[bold green]{'='*55}[/bold green]")
    console.print(f"[bold white]  🧭 CODEBASE ONBOARDING GUIDE[/bold white]")
    console.print(f"[dim]  {repo_url}[/dim]")
    console.print(f"[bold green]{'='*55}[/bold green]\n")

    icons = {
        "PROJECT SUMMARY": "📌",
        "TECH STACK": "🧰",
        "FILE BREAKDOWN": "📁",
        "HOW TO START": "🚀",
        "GOTCHAS": "⚠️"
    }

    for section, content in sections.items():
        icon = icons.get(section, "📄")
        console.print(Panel(
            Markdown(content),
            title=f"{icon} {section}",
            border_style="cyan",
            padding=(1, 2)
        ))

# Main flow
def main():
    repo_url = input("🔗 Enter GitHub repo URL: ").strip()

    parts = repo_url.strip("/").split("/")
    repo_name = f"{parts[-2]}/{parts[-1]}"

    console.print("\n[bold cyan]📥 Fetching files from GitHub...[/bold cyan]")
    repo = github_client.get_repo(repo_name)
    file_data = collect_files(repo)
    console.print(f"[green]✅ Collected {len(file_data)} files[/green]")

    console.print("[bold cyan]📝 Building prompt...[/bold cyan]")
    prompt = build_prompt(file_data)
    console.print(f"[green]✅ Prompt ready ({len(prompt)} characters)[/green]")

    raw_response = ask_gemini(prompt)
    
    console.print("[bold cyan]🔍 Parsing response...[/bold cyan]")
    sections = parse_response(raw_response)
    console.print(f"[green]✅ Found {len(sections)} sections[/green]")
    
    print("\nRAW RESPONSE:")
    print(raw_response)
    print("\nSECTIONS FOUND:", len(sections))

    display_report(sections, repo_url)

main()

