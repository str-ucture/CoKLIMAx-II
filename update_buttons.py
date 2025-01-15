import os

# Define the directory containing the .html files
directory = r"./"
repo_name = f"CoKLIMAx-II"

# Traverse through all files in the directory
for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)

            # Read the file content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            original_html_snippet_en = f'View page source</a>'
            replacement_html_snippet_en = f"{original_html_snippet_en}\n<div id='language-switcher' style='text-align: right; margin-top: 10px;'>\n<a href='/{repo_name}/en/{file}''>English</a> | <a href='/{repo_name}/de/{file}''>Deutsch</a>\n</div>"

            original_html_snippet_de = f'Quelltext anzeigen</a>'
            replacement_html_snippet_de = f"{original_html_snippet_de}\n<div id='language-switcher' style='text-align: right; margin-top: 10px;'>\n<a href='/{repo_name}/en/{file}''>English</a> | <a href='/{repo_name}/de/{file}''>Deutsch</a>\n</div>"

            if original_html_snippet_en in content and 'language-switcher' not in content:
                print(file_path)
                print(replacement_html_snippet_en)
                updated_content = content.replace(original_html_snippet_en, replacement_html_snippet_en)
                print(f"Added Language switcher button to (en) {file_path}")
            elif original_html_snippet_de in content and 'language-switcher' not in content:
                print(file_path)
                print(replacement_html_snippet_de)
                updated_content = content.replace(original_html_snippet_de, replacement_html_snippet_de)
                print(f"Added Language switcher button to (de) {file_path}")
            else:
                # Skip files that do not match the expected pattern
                continue

            # Write the updated content back to the file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(updated_content)

print("Html files updated. Push the codes to Github to preview changes.")
print("Currently the buttons do not work on local machine and only works on Github Pages")