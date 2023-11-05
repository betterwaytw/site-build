from jinja2 import Template, Environment, FileSystemLoader
import json
import os

env = Environment(loader=FileSystemLoader('.'))

# 讀取 JSON 檔案
with open("kptaipei.json", "r", encoding = "UTF-8") as f:
  data = json.load(f)
  
# 讀取 TEMPLATE 檔案
with open("template.html", "r", encoding = "UTF-8") as f:
  t = f.read()

# 生成一個模板
template = env.from_string(t)

# 渲染模板
html = template.render(**data)

# 輸出 HTML 檔案
with open("kptaipei.html", "w", encoding = "UTF-8") as f:
  f.write(html)


