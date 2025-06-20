import markdown
import os
from pathlib import Path
from pygments.formatters import HtmlFormatter

input_path = Path(__file__).parent.parent / 'PrivacyPolicy.md'
output_dir = Path(__file__).parent.parent / 'dist/policies'
output_path = output_dir / 'privacy.html'
css_path = Path(__file__).parent.parent / 'assets/md-style.css'

# 生成代码高亮CSS
code_css = HtmlFormatter(style='friendly').get_style_defs()

# 构建完整HTML模板
def build_html(md_content):
    return f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Privacy Policy</title>
    <link rel="stylesheet" href="{css_path.as_posix()}">
    <style>{code_css}</style>
</head>
<body class="markdown-content">
    {markdown.markdown(md_content, extensions=['fenced_code', 'tables', 'codehilite'])}
</body>
</html>
    '''

# 执行转换
if __name__ == "__main__":
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    html_content = build_html(content)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f'Successfully converted to {output_path}')