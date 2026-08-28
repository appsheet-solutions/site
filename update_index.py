import re

FILE_PATH = "index.html"

def update_html():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Features Section Row Count (Scoped strictly to .fe-69ce755a669fb30b44a3d7a0)
    content = re.sub(
        r"(\.fe-69ce755a669fb30b44a3d7a0\s*\{[\s\S]*?grid-template-rows:\s*)repeat\(98,minmax\(24px, auto\)\);",
        r"\g<1>repeat(92,minmax(24px, auto));",
        content
    )

    # 2. Block-Specific CSS Replacements (Scoped strictly by block class)
    block_replacements = [
        # --- Feature 1: Comprehensive EMR ---
        (
            r"(\.fe-block-yui_3_17_2_1_1775138039932_8239\s*\{\s*grid-area:\s*)10/15/11/23;",
            r"\g<1>10/15/12/23;"
        ),
        (
            r"(\.fe-block-f4d81ecf9c90d1c62159\s*\{\s*grid-area:\s*)12/15/14/23;",
            r"\g<1>12/15/15/23;"
        ),

        # --- Feature 2: Clinic Appointment & Booking System ---
        (
            r"(\.fe-block-f5b5ef044a289650fe14\s*\{\s*grid-area:\s*)19/5/20/13;",
            r"\g<1>19/5/21/13;"
        ),
        (
            r"(\.fe-block-04e6ebacbf2d93a8af48\s*\{\s*grid-area:\s*)21/5/23/13;",
            r"\g<1>21/5/24/13;"
        ),

        # --- Feature 3: Built on Google Cloud ---
        (
            r"(\.fe-block-c9dbdc05ed7e4a81c3c4\s*\{\s*grid-area:\s*)28/15/29/23;",
            r"\g<1>28/15/30/23;"
        ),
        (
            r"(\.fe-block-725f6e8f25d6b448d52d\s*\{\s*grid-area:\s*)45/2/51/10;",
            r"\g<1>45/2/49/10;"  # Mobile desc height
        ),

        # --- Feature 4: Printable Prescriptions ---
        (
            r"(\.fe-block-b134066995f8da6ff411\s*\{\s*grid-area:\s*)52/2/58/10;",
            r"\g<1>50/2/56/10;"  # Mobile image alignment
        ),
        (
            r"(\.fe-block-280cae7bd4d4837c8ca8\s*\{\s*grid-area:\s*)59/2/61/10;",
            r"\g<1>57/2/59/10;"  # Mobile title alignment
        ),
        (
            r"(\.fe-block-280cae7bd4d4837c8ca8\s*\{\s*grid-area:\s*)37/5/38/13;",
            r"\g<1>37/5/39/13;"  # Desktop title
        ),
        (
            r"(\.fe-block-cb7a3085718e7ff2ed28\s*\{\s*grid-area:\s*)61/2/66/10;",
            r"\g<1>59/2/63/10;"  # Mobile desc alignment
        ),

        # --- Feature 5: Streamlined Billing & Payment ---
        (
            r"(\.fe-block-9c015c8174478e059770\s*\{\s*grid-area:\s*)68/2/74/10;",
            r"\g<1>64/2/70/10;"  # Mobile image alignment
        ),
        (
            r"(\.fe-block-3b795d859a58f347aa55\s*\{\s*grid-area:\s*)75/2/77/10;",
            r"\g<1>71/2/73/10;"  # Mobile title alignment
        ),
        (
            r"(\.fe-block-3b795d859a58f347aa55\s*\{\s*grid-area:\s*)46/15/47/23;",
            r"\g<1>46/15/48/23;"  # Desktop title
        ),
        (
            r"(\.fe-block-efe9facd55710c990c53\s*\{\s*grid-area:\s*)77/2/81/10;",
            r"\g<1>73/2/77/10;"  # Mobile desc alignment
        ),
        (
            r"(\.fe-block-efe9facd55710c990c53\s*\{\s*grid-area:\s*)48/15/50/23;",
            r"\g<1>48/15/51/23;"  # Desktop desc
        ),

        # --- Feature 6: HIPAA & DPA Ready ---
        (
            r"(\.fe-block-6b1511cf48d846dc8e91\s*\{\s*grid-area:\s*)82/2/88/10;",
            r"\g<1>78/2/84/10;"  # Mobile image alignment
        ),
        (
            r"(\.fe-block-6b1511cf48d846dc8e91\s*\{\s*grid-area:\s*)53/14/63/27;",
            r"\g<1>53/14/62/27;"  # Desktop image alignment (9 rows)
        ),
        (
            r"(\.fe-block-f8cff77a9c3217fdba08\s*\{\s*grid-area:\s*)89/2/91/10;",
            r"\g<1>85/2/87/10;"  # Mobile title alignment
        ),
        (
            r"(\.fe-block-f8cff77a9c3217fdba08\s*\{\s*grid-area:\s*)55/5/56/13;",
            r"\g<1>55/5/57/13;"  # Desktop title
        ),
        (
            r"(\.fe-block-528db57d7ad2adb7d089\s*\{\s*grid-area:\s*)91/2/97/10;",
            r"\g<1>87/2/91/10;"  # Mobile desc alignment
        ),
    ]

    for pattern, replacement in block_replacements:
        content = re.sub(pattern, replacement, content)

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ Features section grid values safely updated!")

if __name__ == "__main__":
    update_html()
