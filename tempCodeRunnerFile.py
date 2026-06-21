#send to gemini and get response
# def ask_gemini(prompt):
#     print("🤖 Sending to gemini API....")
#     response=client_ai.models.generate_content(
#           model="gemini-1.5-flash-8b",
#           contents=prompt
#     )
    
       
    
#     return response.text

# # main kaam
# def main():
#     repo_url=input ("Enter ur repo url: ").strip()

#     parts=repo_url.split("/")
#     repo_name=f"{parts[-2]}/{parts[-1]}"

#     print("📥 Fetching some data from github...")
#     repo=github_client.get_repo(repo_name)
#     file_data=collect_files(repo)
#     print(f"✅Collected {len(file_data)} files")

#     print("\n📝 Building prompt...")
#     prompt = build_prompt(file_data)
#     print(f"✅ Prompt ready ({len(prompt)} characters)")

#     analysis = ask_gemini(prompt)

#     print("\n" + "="*50)
#     print("🧠 CLAUDE'S ANALYSIS")
#     print("="*50)
#     print(analysis)

# main()
# for model in client_ai.models.list():
#     print(model.name)