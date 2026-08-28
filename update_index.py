import os
import re

FILES = ["index.html", "cliniq.html"]

# 1. Exact Mobile Grid Targets (all 6 cards: 6-row image, 2-row title, 4-row desc)
mobile_targets = {
    # Feature 1 (Rows 8 to 21)
    "fe-block-yui_3_17_2_1_1775138039932_4763": "8/2/14/10",
    "fe-block-yui_3_17_2_1_1775138039932_8239": "15/2/17/10",
    "fe-block-f4d81ecf9c90d1c62159": "17/2/21/10",
    # Feature 2 (Rows 22 to 35)
    "fe-block-7c49df910906813b390b": "22/2/28/10",
    "fe-block-f5b5ef044a289650fe14": "29/2/31/10",
    "fe-block-04e6ebacbf2d93a8af48": "31/2/35/10",
    # Feature 3 (Rows 36 to 49)
    "fe-block-38dea569df7454d90d82": "36/2/42/10",
    "fe-block-c9dbdc05ed7e4a81c3c4": "43/2/45/10",
    "fe-block-725f6e8f25d6b448d52d": "45/2/49/10",
    # Feature 4 (Rows 50 to 63)
    "fe-block-b134066995f8da6ff411": "50/2/56/10",
    "fe-block-280cae7bd4d4837c8ca8": "57/2/59/10",
    "fe-block-cb7a3085718e7ff2ed28": "59/2/63/10",
    # Feature 5 (Rows 64 to 77)
    "fe-block-9c015c8174478e059770": "64/2/70/10",
    "fe-block-3b795d859a58f347aa55": "71/2/73/10",
    "fe-block-efe9facd55710c990c53": "73/2/77/10",
    # Feature 6 (Rows 78 to 91)
    "fe-block-6b1511cf48d846dc8e91": "78/2/84/10",
    "fe-block-f8cff77a9c3217fdba08": "85/2/87/10",
    "fe-block-528db57d7ad2adb7d089": "87/2/91/10",
}

# 2. Exact Desktop Grid Targets (all 6 cards: 9-row image, 2-row title, 3-row desc, 8 cols wide)
desktop_targets = {
    # Feature 1
    "fe-block-yui_3_17_2_1_1775138039932_4763": "8/1/17/14",
    "fe-block-yui_3_17_2_1_1775138039932_8239": "10/15/12/23",
    "fe-block-f4d81ecf9c90d1c62159": "12/15/15/23",
    # Feature 2
    "fe-block-7c49df910906813b390b": "17/14/26/27",
    "fe-block-f5b5ef044a289650fe14": "19/5/21/13",
    "fe-block-04e6ebacbf2d93a8af48": "21/5/24/13",
    # Feature 3
    "fe-block-38dea569df7454d90d82": "26/1/35/14",
    "fe-block-c9dbdc05ed7e4a81c3c4": "28/15/30/23",
    "fe-block-725f6e8f25d6b448d52d": "30/15/33/23",
    # Feature 4
    "fe-block-b134066995f8da6ff411": "35/14/44/27",
    "fe-block-280cae7bd4d4837c8ca8": "37/5/39/13",
    "fe-block-cb7a3085718e7ff2ed28": "39/5/42/13",
    # Feature 5
    "fe-block-9c015c8174478e059770": "44/1/53/14",
    "fe-block-3b795d859a58f347aa55": "46/15/48/23",
    "fe-block-efe9facd55710c990c53": "48/15/51/23",
    # Feature 6
    "fe-block-6b1511cf48d846dc8e91": "53/14/62/27",
    "fe-block-f8cff77a9c3217fdba08": "55/5/57/13",
    "fe-block-528db57d7ad2adb7d089": "57/5/60/13",
}

def update_file(filename):
    if not os.path.exists(filename):
        print(f"⚠️ File '{filename}' not found. Skipping.")
        return

    print(f"\n📄 Processing: {filename}")
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    new_lines = []
    current_block = None
    seen_counts = {}
    updated_count = 0

    for line in lines:
        # Total row count update on mobile
        if "repeat(98,minmax(24px, auto))" in line:
            line = line.replace("repeat(98,minmax(24px, auto))", "repeat(92,minmax(24px, auto))")
            print("  ✓ [Total Rows] 98 -> 92")
            updated_count += 1

        # Detect block selector
        block_match = re.search(r'\.(fe-block-[a-zA-Z0-9_]+)\s*\{', line)
        if block_match:
            current_block = block_match.group(1)

        # Detect and replace grid-area line
        if "grid-area:" in line and current_block:
            occurrence = seen_counts.get(current_block, 0)

            # 1st occurrence in CSS = Mobile
            if occurrence == 0 and current_block in mobile_targets:
                target = mobile_targets[current_block]
                line = re.sub(r'grid-area:\s*[^;]+;', f'grid-area: {target};', line)
                print(f"  ✓ [Mobile]  {current_block} -> {target}")
                updated_count += 1

            # 2nd occurrence in CSS = Desktop
            elif occurrence == 1 and current_block in desktop_targets:
                target = desktop_targets[current_block]
                line = re.sub(r'grid-area:\s*[^;]+;', f'grid-area: {target};', line)
                print(f"  ✓ [Desktop] {current_block} -> {target}")
                updated_count += 1

            seen_counts[current_block] = occurrence + 1

        new_lines.append(line)

    with open(filename, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(new_lines) + "\n")

    print(f"  --> Updated {updated_count} rules in {filename}")

def main():
    for file in FILES:
        update_file(file)
    print("\n✅ All files processed successfully!")

if __name__ == "__main__":
    main()
