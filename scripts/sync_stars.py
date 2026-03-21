import urllib.request
import json
import os

# ==========================================
GITHUB_USERNAME = "alexytcao" # 我从你的截图中看到了你的用户名
# ==========================================

TOKEN = os.environ.get("MY_GITHUB_TOKEN")

def fetch_stars():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/starred?per_page=100"
    headers = {
        # 核心改动：必须用这个特殊的 Accept 头，API 才会返回你个人的 "收藏时间"
        "Accept": "application/vnd.github.star+json",
        "Authorization": f"token {TOKEN}" if TOKEN else "",
        "User-Agent": "Auto-Star-Sync"
    }
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            stars = json.loads(response.read().decode())
            
        md = "# 🤖 自动同步的近期 Star 列表\n\n"
        md += "> 每天自动从 GitHub 拉取最新的 100 个 Star 项目，包含收藏时间。\n\n"
        # 新增了“收藏时间”列
        md += "| 收藏时间 | 项目名称 | 一句话描述 | Star 数量 | 语言 |\n"
        md += "| :---: | :--- | :--- | :---: | :---: |\n"
        
        for item in stars:
            # 数据结构稍微变了，真正的项目信息在 'repo' 节点下
            repo = item.get("repo", {})
            
            # 提取并格式化收藏时间 (截取 YYYY-MM-DD)
            starred_date = item.get("starred_at", "未知")[:10] 
            
            name = repo.get("name", "")
            url = repo.get("html_url", "")
            desc = repo.get("description", "") or "无描述"
            
            # 核心修复：强力清洗描述文本，防止破坏 Markdown 表格结构
            desc = desc.replace("\n", " ").replace("\r", "") # 删掉所有换行
            desc = desc.replace("|", "\|") # 转义管道符
            
            stargazers = repo.get("stargazers_count", 0)
            lang = repo.get("language", "") or "未知"
            
            md += f"| {starred_date} | [{name}]({url}) | {desc} | ⭐ {stargazers} | {lang} |\n"
            
        os.makedirs("./docs", exist_ok=True)
        with open("./docs/auto_stars.md", "w", encoding="utf-8") as f:
            f.write(md)
        print("✅ Star 列表拉取成功！")
        
    except Exception as e:
        print(f"❌ 运行失败: {e}")

if __name__ == "__main__":
    fetch_stars()
