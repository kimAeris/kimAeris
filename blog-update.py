import feedparser

somjang_blog_rss_url = "https://ohzlsss.tistory.com/rss"
rss_feed = feedparser.parse(somjang_blog_rss_url)

MAX_POST_NUM = 5

latest_blog_post_list = ""

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """ ## 👩‍💻 Front-End Web Developer 
### Skils
<img src="https://img.shields.io/badge/HJTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white"/> <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white"/> <img src="https://img.shields.io/badge/Chart.js-FF6384?style=flat-square&logo=Chart.js&logoColor=white"/> <img src="https://img.shields.io/badge/ECharts-AA344D?style=flat-square&logo=ECharts&logoColor=white"/> <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/> 

### 
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=kimAeris&layout=compact&theme=buefy)

### Recent blog posts
"""

markdown_text_footer = """ 
---
<a href="https://ohzlsss.tistory.com"><img src="https://img.shields.io/badge/Tech%20Blog-20C997?style=flat-square&logo=storyblok&logoColor=white"/></a> <a href="https://ohzlsss.tistory.com"><img src="https://img.shields.io/badge/-Portfolio-000000?style=flat-square&logo=Notion&logoColor=white"/></a>  
"""

readme_text = f"{markdown_text}{latest_blog_post_list}{markdown_text_footer}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
