import re

FILE_PATH = "index.html"

# Mobile targets for Features section
mobile_targets = {
    "fe-block-725f6e8f25d6b448d52d": "45/2/49/10",  # F3 Desc: 4 rows (was 6)
    "fe-block-b134066995f8da6ff411": "50/2/56/10",  # F4 Image: shifted to row 50
    "fe-block-280cae7bd4d4837c8ca8": "57/2/59/10",  # F4 Title: shifted to row 57
    "fe-block-cb7a3085718e7ff2ed28": "59/2/63/10",  # F4 Desc: 4 rows (was 5)
    "fe-block-9c015c8174478e059770": "64/2/70/10",  # F5 Image: shifted to row 64
    "fe-block-3b795d859a58f347aa55": "71/2/73/10",  # F5 Title: shifted to row 71
    "fe-block-efe9facd55710c990c53": "73/2/77/10",  # F5 Desc: shifted to row 73
    "fe-block-6b1511cf48d846dc8e91": "78/2/84/10",  # F6 Image: shifted to row 78
    "fe-block-f8cff77a9c3217fdba08": "85/2/87/10",  # F6 Title: shifted to row 85
    "fe-block-528db57d7ad2adb7d089": "87/2/91/10",  # F6 Desc: 4 rows (was 6)
}

# Desktop targets for Features section
desktop_targets = {
    "fe-block-yui_3_17_2_1_1775138039932_8239": "10/15/12/23",
    "fe-block-f4d81ecf9c90d1c62159": "12/15/15/23",
    "fe-block-f5b5ef044a289650fe14": "19/5/21/13",
    "fe-block-04e6ebacbf2d93a8af48": "21/5/24/13",
    "fe-block-c9dbdc05ed7e4a81c3c4": "28/15/30/23",
    "fe-block-280cae7bd4d4837c8ca8": "37/5/39/13",
    "fe-block-3b795d859a58f347aa55": "46/15/48/23",
    "fe-block-efe9facd55710c990c53": "48/15/51/23",
    "fe-block-6b1511cf48d846dc8e91": "53/14/62/27",
    "fe-block-f8cff77a9c3217fdba08": "55/5/57/13",
}

def update_html():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    new_lines = []
    current_block = None
    seen_counts = {}
    updated_count = 0

    for line in lines:
        # 1. Total row count update
        if "repeat(98,minmax(24px, auto))" in line:
            line = line.replace("repeat(98,minmax(24px, auto))", "repeat(92,minmax(24px, auto))")
            print("  ✓ [Total Rows] 98 -> 92")
            updated_count += 1

        # 2. Track current block ID
        block_match = re.search(r'\.(fe-block-[a-zA-Z0-9_]+)\s*\{', line)
        if block_match:
            current_block = block_match.group(1)

        # 3. Check for grid-area line
        if "grid-area:" in line and current_block:
            occurrence = seen_counts.get(current_block, 0)
            
            # 1st occurrence = Mobile
            if occurrence == 0 and current_block in mobile_targets:
                target = mobile_targets[current_block]
                line = re.sub(r'grid-area:\s*[^;]+;', f'grid-area: {target};', line)
                print(f"  ✓ [Mobile]  {current_block} -> {target}")
                updated_count += 1
            
            # 2nd occurrence = Desktop (inside @media min-width: 768px)
            elif occurrence == 1 and current_block in desktop_targets:
                target = desktop_targets[current_block]
                line = re.sub(r'grid-area:\s*[^;]+;', f'grid-area: {target};', line)
                print(f"  ✓ [Desktop] {current_block} -> {target}")
                updated_count += 1

            seen_counts[current_block] = occurrence + 1

        new_lines.append(line)

    with open(FILE_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(new_lines) + "\n")

    print(f"\n✅ Total lines successfully updated: {updated_count}")

if __name__ == "__main__":
    update_html()
