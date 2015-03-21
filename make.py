
import os
import shutil
import markdown2

web_src = """
<html>
    <head>
        <title>Meta Github Pages</title>
        <link rel="stylesheet" href="bootstrap.min.css">
        <link rel="stylesheet" href="github_markdown.css">
        <link rel="stylesheet" href="github_pygments.css">
    </head>
    <body class="markdown-body">
        <div class="container">
            {inner_content}
        </div>
    </body>
</html>
"""

directory = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(directory, 'README.md'), 'r') as f:
    markdown_content = f.read()

inner_content = markdown2.markdown(markdown_content, extras=['fenced-code-blocks', 'code-friendly'])
html_content = web_src.format(inner_content=inner_content)

with open(os.path.join(directory, 'web_output', 'index.html'), 'w') as f:
    f.write(html_content)

shutil.copy(os.path.join(directory, 'github_markdown.css'), os.path.join(directory, 'web_output'))
shutil.copy(os.path.join(directory, 'github_pygments.css'), os.path.join(directory, 'web_output'))
shutil.copy(os.path.join(directory, 'bootstrap.min.css'), os.path.join(directory, 'web_output'))
