import re

FILE_PATH = "index.html"

def update_html():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # (Selector Regex Pattern, Target Old Value, New Value)
    rules = [
        # --- Section Grid Total Rows (98 -> 92) ---
        (r"(\.fe-69ce755a669fb30b44b29aa0[\s\S]*?grid-template-rows:\s*repeat\()98(,\s*minmax\(24px,\s*auto\)\);)", r"\g<1>92\g<2>", "Features Total Rows (98 -> 92)"),

        # =========================================================================
        # MOBILE RULES (Fixing the taller heights and gaps on Cards 3, 4, 5, and 6)
        # =========================================================================
        (r"(\.fe-block-725f6e8f25d6b448d52d[\s\S]*?grid-area:\s*)45/2/51/10;", r"\g<1>45/2/49/10;", "F3 Mobile Desc (45/2/51/10 -> 45/2/49/10)"),
        (r"(\.fe-block-b134066995f8da6ff411[\s\S]*?grid-area:\s*)52/2/58/10;", r"\g<1>50/2/56/10;", "F4 Mobile Image (52/2/58/10 -> 50/2/56/10)"),
        (r"(\.fe-block-280cae7bd4d4837c8ca8[\s\S]*?grid-area:\s*)59/2/61/10;", r"\g<1>57/2/59/10;", "F4 Mobile Title (59/2/61/10 -> 57/2/59/10)"),
        (r"(\.fe-block-cb7a3085718e7ff2ed28[\s\S]*?grid-area:\s*)61/2/66/10;", r"\g<1>59/2/63/10;", "F4 Mobile Desc (61/2/66/10 -> 59/2/63/10)"),
        (r"(\.fe-block-9c015c8174478e059770[\s\S]*?grid-area:\s*)68/2/74/10;", r"\g<1>64/2/70/10;", "F5 Mobile Image (68/2/74/10 -> 64/2/70/10)"),
        (r"(\.fe-block-3b795d859a58f347aa55[\s\S]*?grid-area:\s*)75/2/77/10;", r"\g<1>71/2/73/10;", "F5 Mobile Title (75/2/77/10 -> 71/2/73/10)"),
        (r"(\.fe-block-efe9facd55710c990c53[\s\S]*?grid-area:\s*)77/2/81/10;", r"\g<1>73/2/77/10;", "F5 Mobile Desc (77/2/81/10 -> 73/2/77/10)"),
        (r"(\.fe-block-6b1511cf48d846dc8e91[\s\S]*?grid-area:\s*)82/2/88/10;", r"\g<1>78/2/84/10;", "F6 Mobile Image (82/2/88/10 -> 78/2/84/10)"),
        (r"(\.fe-block-f8cff77a9c3217fdba08[\s\S]*?grid-area:\s*)89/2/91/10;", r"\g<1>85/2/87/10;", "F6 Mobile Title (89/2/91/10 -> 85/2/87/10)"),
        (r"(\.fe-block-528db57d7ad2adb7d089[\s\S]*?grid-area:\s*)91/2/97/10;", r"\g<1>87/2/91/10;", "F6 Mobile Desc (91/2/97/10 -> 87/2/91/10)"),

        # =========================================================================
        # DESKTOP RULES (Standardizing all 6 cards to 8 columns and 2/3 row text)
        # =========================================================================
        (r"(\.fe-block-yui_3_17_2_1_1775138039932_8239[\s\S]*?grid-area:\s*)10/15/11/23;", r"\g<1>10/15/12/23;", "F1 Desktop Title (2 rows)"),
        (r"(\.fe-block-f4d81ecf9c90d1c62159[\s\S]*?grid-area:\s*)12/15/14/23;", r"\g<1>12/15/15/23;", "F1 Desktop Desc (3 rows)"),
        (r"(\.fe-block-f5b5ef044a289650fe14[\s\S]*?grid-area:\s*)19/5/20/13;", r"\g<1>19/5/21/13;", "F2 Desktop Title (2 rows)"),
        (r"(\.fe-block-04e6ebacbf2d93a8af48[\s\S]*?grid-area:\s*)21/5/23/13;", r"\g<1>21/5/24/13;", "F2 Desktop Desc (3 rows)"),
        (r"(\.fe-block-c9dbdc05ed7e4a81c3c4[\s\S]*?grid-area:\s*)28/15/29/23;", r"\g<1>28/15/30/23;", "F3 Desktop Title (2 rows)"),
        (r"(\.fe-block-280cae7bd4d4837c8ca8[\s\S]*?grid-area:\s*)37/5/38/13;", r"\g<1>37/5/39/13;", "F4 Desktop Title (2 rows)"),
        (r"(\.fe-block-3b795d859a58f347aa55[\s\S]*?grid-area:\s*)46/15/47/23;", r"\g<1>46/15/48/23;", "F5 Desktop Title (2 rows)"),
        (r"(\.fe-block-efe9facd55710c990c53[\s\S]*?grid-area:\s*)48/15/50/23;", r"\g<1>48/15/51/23;", "F5 Desktop Desc (3 rows)"),
        (r"(\.fe-block-6b1511cf48d846dc8e91[\s\S]*?grid-area:\s*)53/14/63/27;", r"\g<1>53/14/62/27;", "F6 Desktop Image (9 rows)"),
        (r"(\.fe-block-f8cff77a9c3217fdba08[\s\S]*?grid-area:\s*)55/5/56/13;", r"\g<1>55/5/57/13;", "F6 Desktop Title (2 rows)"),
    ]

    updated_count = 0
    for pattern, replacement, label in rules:
        new_content, count = re.subn(pattern, replacement, content, count=1)
        if count > 0:
            content = new_content
            updated_count += 1
            print(f"  ✓ Replaced: {label}")
        else:
            print(f"  ⚠️ Skipped/Not found: {label}")

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Total rules successfully updated: {updated_count} / {len(rules)}")

if __name__ == "__main__":
    update_html()
