<!-- 1. 这里是样式（只需在文件头部放一次） -->
<style>
.bookmark-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); 
  gap: 20px; 
  margin-top: 20px;
}
.bookmark-card { 
  border: 1px solid #eaecef; 
  border-radius: 8px; 
  padding: 16px; 
  transition: all 0.3s ease; 
  background: #fafbfc; 
}
.bookmark-card:hover { 
  box-shadow: 0 8px 15px rgba(0,0,0,0.1); 
  transform: translateY(-2px);
}
.bookmark-card a { 
  text-decoration: none; 
  color: #0366d6; 
  font-weight: 600; 
  font-size: 16px; 
  display: block; 
  margin-bottom: 8px; 
  border-bottom: none !important; /* 覆盖 docsify 默认的 a 标签下划线 */
}
.bookmark-card p { 
  font-size: 13px; 
  color: #586069; 
  margin: 0; 
  line-height: 1.5;
}
</style>

<!-- 2. 这里是书签内容（新增书签就复制这段 div） -->
<div class="bookmark-grid">

  <!-- 【改这里】：复制这个卡片结构来增加新书签 -->
  <div class="bookmark-card">
    <a href="https://github.com" target="_blank">🐙 GitHub</a>
    <p>全球最大的同性交友网站，代码托管平台。</p>
  </div>

  <div class="bookmark-card">
    <a href="https://v2ex.com" target="_blank">💬 V2EX</a>
    <p>程序员的日常摸鱼与交流社区。</p>
  </div>

</div>
