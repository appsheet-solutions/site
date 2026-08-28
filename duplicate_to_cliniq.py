import os
import re

# 1. Ensure target directory exists
target_dir = "cliniq"
os.makedirs(target_dir, exist_ok=True)

# 2. Read base index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 3. Fix relative assets paths so they point to the root directory
# Handles href="...", src="...", and srcset="..."
html = re.sub(r'(href|src)=["\'](css/|js/|images/)', r'\1="../\2', html)
html = re.sub(r'srcset=["\']images/', r'srcset="../images/', html)
html = re.sub(r',\s*images/', r', ../images/', html)

# 4. Clean up Squarespace JSON script/css references inside data-block attributes
html = html.replace('&quot;css/', '&quot;../css/')
html = html.replace('&quot;js/', '&quot;../js/')

# 5. Clean up URLs for the /cliniq subfolder
html = html.replace('href="https://appsheet.solutions"', 'href="https://appsheet.solutions/cliniq"')
html = html.replace('content="https://appsheet.solutions"', 'content="https://appsheet.solutions/cliniq"')

# 6. Read and insert the new section after Section 1 (data-section-id="69ce5dcc6352dc7767a288c3")
# The section is inserted right after the closing tag of section 1.
with open("new_section.html", "r", encoding="utf-8") as f:
    new_section_code = f.read()

target_anchor = '</section>\n\n      \n    \n      \n        \n        \n\n\n  \n  \n\n\n\n\n\n\n\n\n\n\n\n<section\n  data-test="page-section"\n  \n  data-section-theme="white"\n  class=\'page-section \n    \n      full-bleed-section\n      layout-engine-section\n    \n    background-width--full-bleed\n    \n      section-height--medium\n    \n    \n      content-width--wide\n    \n    horizontal-alignment--center\n    vertical-alignment--middle\n    \n      \n    \n    \n    white\'\n  \n  data-section-id="69ce662ddd95dc70242ad20e"'

if target_anchor in html:
    html = html.replace(target_anchor, '</section>\n\n' + new_section_code + '\n\n<section\ndata-test="page-section"\n  \n  data-section-theme="white"\n  class=\'page-section \n    \n      full-bleed-section\n      layout-engine-section\n    \n    background-width--full-bleed\n    \n      section-height--medium\n    \n    \n      content-width--wide\n    \n    horizontal-alignment--center\n    vertical-alignment--middle\n    \n      \n    \n    \n    white\'\n  \n  data-section-id="69ce662ddd95dc70242ad20e"')
else:
    # Fallback regex insertion right after the first section tag ends
    html = re.sub(
        r'(<section[^>]*data-section-id="69ce5dcc6352dc7767a288c3"[^>]*>[\s\S]*?</section>)',
        r'\1\n\n' + new_section_code,
        html
    )

# 7. Write to /cliniq/index.html
with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully created /cliniq/index.html with updated assets and the new section!")
