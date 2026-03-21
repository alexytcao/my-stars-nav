import urllib.request
import json
import os

# ==========================================
# 仅需修改以下变量
GITHUB_USERNAME = "alexytcao" # 改这里：比如 "torvalds"
# ==========================================

TOKEN = os.environ.get("MY_GITHUB_TOKEN")

def fetch_stars():
    # 默认拉取最近的 150 个 Star（为了轻量，不做全量深度遍历）
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/starred?per_page=150"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {TOKEN}" if TOKEN else "",
        "User-Agent": "Auto-Star-Sync"
    }
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            stars = json.loads(response.read().decode())
            
        # 生成 Markdown 表格
        md = "# 🤖 自动同步的近期 Star 列表\n\n"
        md += "> 每天自动从 GitHub 拉取最新的 150 个 Star 项目，供筛选参考。\n\n"
        md += "| 项目名称 | 一句话描述 | Star 数量 | 语言 |\n"
        md += "| :--- | :--- | :---: | :---: |\n"
        
        for repo in stars:
            name = repo.get("name", "")
            url = repo.get("html_url", "")
            desc = repo.get("description", "") or "无描述"
            desc = desc.replace("\n", " ") # 防止换行破坏表格结构
            stargazers = repo.get("stargazers_count", 0)
            lang = repo.get("language", "") or "未知"
            
            md += f"| [{name}]({url}) | {desc} | ⭐ {stargazers} | {lang} |\n"
            
        # 写入相对路径下的 docs 目录
        os.makedirs("./docs", exist_ok=True)
        with open("./docs/auto_stars.md", "w", encoding="utf-8") as f:
            f.write(md)
        print("✅ Star 列表拉取并生成 MD 成功！")
        
    except Exception as e:
        print(f"❌ 运行失败: {e}")

if __name__ == "__main__":
    fetch_stars()
