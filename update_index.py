import os

# Define the specific file path
file_path = os.path.join("docs", "index.html")

# Define the original and replacement HTML snippets
original_html_snippet = '<a href="_sources/index.rst.txt" rel="nofollow"> View page source</a>'
replacement_html_snippet = '''
<a href="_sources/index.rst.txt" rel="nofollow"> View page source</a>
<div id="language-switcher" style="text-align: right; margin-top: 10px;">
  <a href="../en/index.html">English</a> | <a href="../de/index.html">Deutsch</a>
</div>
'''

# Check if the target file exists
if os.path.exists(file_path):
    # Read the file content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the original snippet with the replacement
    updated_content = content.replace(original_html_snippet, replacement_html_snippet)
    
    # Write the updated content back to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)
    
    print(f"File '{file_path}' updated successfully!")
else:
    print(f"File '{file_path}' does not exist!")
