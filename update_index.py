import re

FILE_PATH = "index.html"

# Exact target grid-areas per block ID
mobile_targets = {
    "fe-block-725f6e8f25d6b448d52d": "45/2/49/10",  # F3 Desc: 4 rows (was 6)
    "fe-block-b134066995f8da6ff411": "50/2/56/10",  # F4 Image: shifted to 50
    "fe-block-280cae7bd4d4837c8ca8": "57/2/59/10",  # F4 Title: shifted to 57
    "fe-block-cb7a3085718e7ff2ed28": "59/2/63/10",  # F4 Desc: 4 rows (was 5)
    "fe-block-9c015c8174478e059770": "64/2/70/10",  # F5 Image: shifted to 64
    "fe-block-3b795d859a58f347aa55": "71/2/73/10",  # F5 Title: shifted to 71
    "fe-block-efe9facd55710c990c53": "73/2/77/10",  # F5 Desc: shifted to 73
    "fe-block-6b1511cf48d846dc8e91": "78/2/84/10",  # F6 Image: shifted to 78
    "fe-block-f8cff77a9c3217fdba08": "85/2/87/10",  # F6 Title: shifted to 85
    "fe-block-528db57d7ad2adb7d089": "87/2/91/10",  # F6 Desc: 4 rows (was 6)
}

desktop_targets = {
    "fe-block-yui_3_17_2_1_1775138039932_8239": "10/15/12/23",  # F1 Title: 2 rows
    "fe-block-f4d81ecf9c90d1c62159": "12/15/15/23",            # F1 Desc: 3 rows
    "fe-block-f5b5ef044a289650fe14": "19/5/21/13",             # F2 Title: 2 rows
    "fe-block-04e6ebacbf2d93a8af48": "21/5/24/13",             # F2 Desc: 3 rows
    "fe-block-c9dbdc05ed7e4a81c3c4": "28/15/30/23",            # F3 Title: 2 rows
    "fe-block-280cae7bd4d4837c8ca8": "37/5/39/13",             # F4 Title: 2 rows
    "fe-block-3b795d859a58f347aa55": "46/15/48/23",            # F5 Title: 2 rows
    "fe-block-efe9facd55710c990c53": "48/15/51/23",            # F5 Desc: 3 rows
    "fe-block-6b1511cf48d846dc8e91": "53/14/62/27",            # F6 Image: 9 rows
    "fe-block-f8cff77a9c3217fdba08": "55/5/57/13",             # F6 Title: 2 rows
}

def update_html():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    current_block = None
    depth = 0
    desktop_depth = -1
    updated_count = 0

    for line in lines:
        # 1. Total row count update (line regex)
        if "repeat(98,minmax(24px, auto))" in line:
            line = line.replace("repeat(98,minmax(24px, auto))", "repeat(92,minmax(24px, auto))")
            print("  ✓ [Total Rows] Updated 98 -> 92")
            updated_count += 1

        # 2. Track Media Queries
        if "@media (min-width: 768px)" in line:
            desktop_depth = depth

        # 3. Track Current Block ID
        block_match = re.search(r'\.(fe-block-[a-zA-Z0-9_]+)\s*\{', line)
        if block_match:
            current_block = block_match.group(1)

        is_desktop = (desktop_depth != -1 and depth >= desktop_depth)

        # 4. Perform line-by-line regex replacement
        if "grid-area:" in line and current_block:
            if is_desktop and current_block in desktop_targets:
                new_val = desktop_targets[current_block]
                line = re.sub(r'grid-area:\s*[^;]+;', f'grid-area: {new_val};', line)
                print(f"  ✓ [Desktop] {current_block} -> {new_val}")
                updated_count += 1
            elif not is_desktop and current_block in mobile_targets:
                new_val = mobile_targets[current_block]
                line = re.sub(r'grid-area:\s*[^;]+;', f'grid-area: {new_val};', line)
                print(f"  ✓ [Mobile]  {current_block} -> {new_val}")
                updated_count += 1

        # Track brace nesting depth
        depth += line.count('{') - line.count('}')
        if desktop_depth != -1 and depth <= desktop_depth:
            desktop_depth = -1

        new_lines.append(line)

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"\n✅ Total replacements applied: {updated_count} / 21")

if __name__ == "__main__":
    update_html()
