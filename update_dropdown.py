import os

# Define the directory containing the .html files
directory = r"./docs/"
# repo_name = f"./docs/" # Change to repo_name = f"./docs/" to test the i18n locally
repo_name = f"./CoKLIMAx-II/" # f"./CoKLIMAx-II/" to test on Github Pages

replacement_text_en = f"{repo_name}en/"
replacement_text_de = f"{repo_name}de/"
replacement_text = f"{repo_name}"

# Traverse through all files in the directory
for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "/en\\" not in file_path and '/de\\' not in file_path:
                print("Root, docs")
                file_path_en = file_path.replace(directory,replacement_text_en)
                file_path_de = file_path.replace(directory,replacement_text_de)
            elif "/en\\" in file_path:
                print("En, docs")
                file_path_en = file_path.replace(directory,replacement_text)
                file_path_de = file_path.replace(directory,replacement_text).replace("/en\\","/de\\")
            elif "/de\\" in file_path:
                print("De, docs")
                file_path_en = file_path.replace(directory,replacement_text).replace("/de\\","/en\\")
                file_path_de = file_path.replace(directory,replacement_text)

            # Search and replace
            original_html_snippet_en = f'View page source</a>'
            replacement_html_snippet_en = f"""{original_html_snippet_en}
<div id='language-switcher' style='text-align: right; margin-top: 10px;'>
    <select onchange="location = this.value;">
        <option value='/{file_path_en}' selected>EN</option>
        <option value='/{file_path_de}'>DE</option>
    </select>
</div>"""

            original_html_snippet_de = f'Quelltext anzeigen</a>'
            replacement_html_snippet_de = f"""{original_html_snippet_de}
<div id='language-switcher' style='text-align: right; margin-top: 10px;'>
    <select onchange="location = this.value;">
        <option value='/{file_path_en}'>EN</option>
        <option value='/{file_path_de}' selected>DE</option>
    </select>
</div>"""
            
            if original_html_snippet_en in content and 'language-switcher' not in content:
                print(file_path)
                print(replacement_html_snippet_en)
                updated_content = content.replace(original_html_snippet_en, replacement_html_snippet_en)
                print(f"Added Language switcher dropdown to (en) {file_path}")
            elif original_html_snippet_de in content and 'language-switcher' not in content:
                print(file_path)
                print(replacement_html_snippet_de)
                updated_content = content.replace(original_html_snippet_de, replacement_html_snippet_de)
                print(f"Added Language switcher dropdown to (de) {file_path}")
            else:
                # Skip files that do not match the expected pattern
                continue

            # Only write back to the file if there was a change
            if updated_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)

# print("Html files updated. Push the codes to Github to preview changes.")
# print("Currently the dropdown does not work on local machine and only works on Github Pages")