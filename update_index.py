FILE_PATH = "index.html"

# Exact line-by-line string replacements matching your index.html
REPLACEMENTS = [
    # 1. Total Section Grid Rows (98 -> 92)
    (
        "grid-template-rows: repeat(98,minmax(24px, auto));",
        "grid-template-rows: repeat(92,minmax(24px, auto));"
    ),

    # 2. Fix Google Cloud Card (Feature 3) - Shrink description from 6 rows to 4 rows
    (
        ".fe-block-725f6e8f25d6b448d52d {\n    grid-area: 45/2/51/10;",
        ".fe-block-725f6e8f25d6b448d52d {\n    grid-area: 45/2/49/10;"
    ),

    # 3. Fix Prescriptions Card (Feature 4) - Pull up Image, Title, and shrink Desc from 5 to 4 rows
    (
        ".fe-block-b134066995f8da6ff411 {\n    grid-area: 52/2/58/10;",
        ".fe-block-b134066995f8da6ff411 {\n    grid-area: 50/2/56/10;"
    ),
    (
        ".fe-block-280cae7bd4d4837c8ca8 {\n    grid-area: 59/2/61/10;",
        ".fe-block-280cae7bd4d4837c8ca8 {\n    grid-area: 57/2/59/10;"
    ),
    (
        ".fe-block-cb7a3085718e7ff2ed28 {\n    grid-area: 61/2/66/10;",
        ".fe-block-cb7a3085718e7ff2ed28 {\n    grid-area: 59/2/63/10;"
    ),

    # 4. Pull up Billing Card (Feature 5) to remove the gap
    (
        ".fe-block-9c015c8174478e059770 {\n    grid-area: 68/2/74/10;",
        ".fe-block-9c015c8174478e059770 {\n    grid-area: 64/2/70/10;"
    ),
    (
        ".fe-block-3b795d859a58f347aa55 {\n    grid-area: 75/2/77/10;",
        ".fe-block-3b795d859a58f347aa55 {\n    grid-area: 71/2/73/10;"
    ),
    (
        ".fe-block-efe9facd55710c990c53 {\n    grid-area: 77/2/81/10;",
        ".fe-block-efe9facd55710c990c53 {\n    grid-area: 73/2/77/10;"
    ),

    # 5. Pull up HIPAA & DPA Card (Feature 6) and shrink Desc from 6 rows to 4 rows
    (
        ".fe-block-6b1511cf48d846dc8e91 {\n    grid-area: 82/2/88/10;",
        ".fe-block-6b1511cf48d846dc8e91 {\n    grid-area: 78/2/84/10;"
    ),
    (
        ".fe-block-f8cff77a9c3217fdba08 {\n    grid-area: 89/2/91/10;",
        ".fe-block-f8cff77a9c3217fdba08 {\n    grid-area: 85/2/87/10;"
    ),
    (
        ".fe-block-528db57d7ad2adb7d089 {\n    grid-area: 91/2/97/10;",
        ".fe-block-528db57d7ad2adb7d089 {\n    grid-area: 87/2/91/10;"
    ),
]

def run():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    count = 0
    for old_str, new_str in REPLACEMENTS:
        if old_str in content:
            content = content.replace(old_str, new_str)
            count += 1
            print(f"  ✓ Replaced: {old_str.splitlines()[0]}")
        else:
            print(f"  ⚠️ Not found: {old_str.splitlines()[0]}")

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Total successfully updated: {count} / {len(REPLACEMENTS)}")

if __name__ == "__main__":
    run()
