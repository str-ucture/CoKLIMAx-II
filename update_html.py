import os

# Define the directory containing the .html files
directory = "./docs"

# Traverse through all files in the directory
for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            
            # Read the file content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Construct the original and replacement HTML snippets dynamically
            original_html_snippet_en = f'<a href="_sources/{file[:-5]}.rst.txt" rel="nofollow"> View page source</a>'
            original_html_snippet_de = f'<a href="_sources/{file[:-5]}.rst.txt" rel="nofollow"> Quelltext anzeigen</a>'
            
            replacement_html_snippet_en = f'''
<a href="_sources/{file[:-5]}.rst.txt" rel="nofollow"> View page source</a>
<div id="language-switcher" style="text-align: right; margin-top: 10px;">
  <a href="/docs/en/{file}">English</a> | <a href="/docs/de/{file}">Deutsch</a>
</div>
'''

            replacement_html_snippet_de = f'''
<a href="_sources/{file[:-5]}.rst.txt" rel="nofollow"> Quelltext anzeigen</a>
<div id="language-switcher" style="text-align: right; margin-top: 10px;">
  <a href="/docs/en/{file}">English</a> | <a href="/docs/de/{file}">Deutsch</a>
</div>
'''
            
            # Check and replace based on the content
            if original_html_snippet_en in content:
                updated_content = content.replace(original_html_snippet_en, replacement_html_snippet_en)
            elif original_html_snippet_de in content:
                updated_content = content.replace(original_html_snippet_de, replacement_html_snippet_de)
            else:
                # Skip files that do not match the expected pattern
                continue
            
            # Write the updated content back to the file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)

print("HTML files updated successfully!")
