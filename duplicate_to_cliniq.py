cat << 'EOF' > duplicate_to_cliniq.py
import os
import re

target_dir = "cliniq"
os.makedirs(target_dir, exist_ok=True)

# 1. Read base index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 2. Fix relative asset paths
html = re.sub(r'(href|src)=["\'](css/|js/|images/)', r'\1="../\2', html)
html = re.sub(r'srcset=["\']images/', r'srcset="../images/', html)
html = re.sub(r',\s*images/', r', ../images/', html)
html = html.replace('&quot;css/', '&quot;../css/')
html = html.replace('&quot;js/', '&quot;../js/')

# 3. Update canonical and meta URLs
html = html.replace('href="https://appsheet.solutions"', 'href="https://appsheet.solutions/cliniq"')
html = html.replace('content="https://appsheet.solutions"', 'content="https://appsheet.solutions/cliniq"')

# 4. Embedded Cliniq New Section
new_section_code = """
<!-- START: Cliniq Features Section -->
<section
  data-test="page-section"
  data-section-theme="white"
  class="page-section full-bleed-section layout-engine-section background-width--full-bleed section-height--custom content-width--wide horizontal-alignment--center vertical-alignment--middle white"
  data-section-id="cliniq-features-section"
  data-controller="SectionWrapperController"
  data-fluid-engine-section
  data-sqsp-section="fluid-engine"
>
  <div class="section-border">
    <div class="section-background"></div>
  </div>
  <div class="content-wrapper" style="padding-top: calc(2vmax / 10); padding-bottom: calc(2vmax / 10);">
    <div class="content">
      <div data-fluid-engine="true">
        <style>
          .fe-688f21ea9705ee782c67264c {
            --grid-gutter: calc(var(--sqs-mobile-site-gutter, 6vw) - 11.0px);
            --cell-max-width: calc((var(--sqs-site-max-width, 1500px) - (11.0px * (8 - 1))) / 8);
            display: grid;
            position: relative;
            grid-area: 1/1/-1/-1;
            grid-template-rows: repeat(auto-fill, minmax(24px, auto));
            grid-template-columns: minmax(var(--grid-gutter), 1fr) repeat(8, minmax(0, var(--cell-max-width))) minmax(var(--grid-gutter), 1fr);
            row-gap: 11.0px;
            column-gap: 11.0px;
          }
          @media (min-width: 768px) {
            .fe-688f21ea9705ee782c67264c {
              --grid-gutter: calc(var(--sqs-site-gutter, 4vw) - 11.0px);
              --cell-max-width: calc((var(--sqs-site-max-width, 1500px) - (11.0px * (24 - 1))) / 24);
              --container-width: min(var(--sqs-site-max-width, 1500px), calc(100vw - var(--sqs-site-gutter, 4vw) * 2));
              grid-template-columns: minmax(var(--grid-gutter), 1fr) repeat(24, minmax(0, var(--cell-max-width))) minmax(var(--grid-gutter), 1fr);
            }
          }
        </style>

        <div class="fluid-engine fe-688f21ea9705ee782c67264c" id="yui_3_17_2_1_1787894412453_626">
          
          <!-- Block: Title -->
          <div class="fe-block fe-block-yui_3_17_2_1_1754209547092_60034" style="grid-column: 2 / -2;">
            <div class="sqs-block website-component-block sqs-block-website-component sqs-block-html html-block" data-block-css='["../css/website.components.html.styles.css"]' data-block-scripts='["../js/website.components.html.visitor.js"]' data-block-type="1337" id="block-yui_3_17_2_1_1754209547092_60034">
              <div class="sqs-block-content">
                <div class="sqs-text-block-container">
                  <div class="sqs-html-content">
                    <h2 style="text-align:center;white-space:pre-wrap;">Everything You Need to Run a Modern Clinic</h2>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Feature 1: Comprehensive EMR -->
          <div class="fe-block fe-block-1ffaf85b22bfbee0f92b" style="grid-column: 2 / span 4;">
            <div class="sqs-block website-component-block sqs-block-website-component sqs-block-image image-block" data-block-css='["../css/website.components.imagefluid.styles.css"]' data-block-scripts='["../js/2513.js","../js/8018.js","../js/9882.js","../js/website.components.imagefluid.visitor.js"]' data-block-type="1337" id="block-1ffaf85b22bfbee0f92b">
              <div class="sqs-block-content">
                <div class="fluid-image-component-root image-block-outer-wrapper design-layout-fluid">
                  <div class="fluid-image-container visitor-mode" style="border-top-left-radius: 20px; border-radius: 10px; overflow: hidden;">
                    <img src="https://images.squarespace-cdn.com/content/v1/66332f216494c206f73b6e07/dda8a90e-2880-4e57-bd38-fe25a838c069/Screenshot+from+2025-08-03+21-03-12.png" alt="EMR Preview" style="width: 100%; display:block;" loading="lazy">
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="fe-block fe-block-a8c0d58cd9300651c808" style="grid-column: 6 / span 4;">
            <div class="sqs-block website-component-block sqs-block-website-component sqs-block-html html-block sqs-background-enabled" data-block-css='["../css/website.components.html.styles.css"]' data-block-scripts='["../js/website.components.html.visitor.js"]' data-block-type="1337" id="block-a8c0d58cd9300651c808">
              <div class="sqs-block-content">
                <div class="sqs-text-block-container" style="background: hsla(var(--accent-hsl), 1); padding: 20px; border-radius: 8px;">
                  <div class="sqs-html-content">
                    <p style="text-align:center;white-space:pre-wrap;"><u><strong>Comprehensive EMR</strong></u></p>
                    <p style="text-align:center;white-space:pre-wrap;" class="sqsrte-small">Maintain a complete, legible, and secure digital history for every patient. Instantly access personal details, consultation notes, medical history, and prescriptions with just a single click.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Feature 2: Appointment & Booking -->
          <div class="fe-block fe-block-bda17992f4bd4975fd54" style="grid-column: 2 / span 4;">
            <div class="sqs-block website-component-block sqs-block-website-component sqs-block-image image-block" data-block-css='["../css/website.components.imagefluid.styles.css"]' data-block-scripts='["../js/2513.js","../js/8018.js","../js/9882.js","../js/website.components.imagefluid.visitor.js"]' data-block-type="1337" id="block-bda17992f4bd4975fd54">
              <div class="sqs-block-content">
                <div class="fluid-image-component-root image-block-outer-wrapper design-layout-fluid">
                  <div class="fluid-image-container visitor-mode" style="border-radius: 10px; overflow: hidden;">
                    <img src="https://images.squarespace-cdn.com/content/v1/66332f216494c206f73b6e07/ad704e51-866f-45e6-9124-f7f103d45a81/Screenshot+from+2025-07-30+20-36-11.png" alt="Booking Preview" style="width: 100%; display:block;" loading="lazy">
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="fe-block fe-block-b90bbb00b4be9eb2a5b0" style="grid-column: 6 / span 4;">
            <div class="sqs-block website-component-block sqs-block-website-component sqs-block-html html-block sqs-background-enabled" data-block-css='["../css/website.components.html.styles.css"]' data-block-scripts='["../js/website.components.html.visitor.js"]' data-block-type="1337" id="block-b90bbb00b4be9eb2a5b0">
              <div class="sqs-block-content">
                <div class="sqs-text-block-container" style="background: hsla(184.39, 67%, 76%, 1); padding: 20px; border-radius: 8px;">
                  <div class="sqs-html-content">
                    <p style="text-align:center;white-space:pre-wrap;"><u><strong>Clinic Appointment &amp; Booking System</strong></u></p>
                    <p style="text-align:center;white-space:pre-wrap;" class="sqsrte-small">Effortlessly schedule appointments with our smart calendar. Use daily, weekly, or monthly views to prevent double-bookings, optimize your time, and reduce overall patient wait times.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Feature 3: Infrastructure / Cloud / Compliance Badges -->
          <div class="fe-block fe-block-82100d85891728a0de1a" style="grid-column: 2 / span 4;">
            <div class="sqs-block website-component-block sqs-block-website-component sqs-block-html html-block sqs-background-enabled" data-block-css='["../css/website.components.html.styles.css"]' data-block-scripts='["../js/website.components.html.visitor.js"]' data-block-type="1337" id="block-82100d85891728a0de1a">
              <div class="sqs-block-content">
                <div class="sqs-text-block-container" style="background: hsla(0, 59%, 40%, 1); padding: 20px; border-radius: 8px;">
                  <div class="sqs-html-content">
                    <p style="text-align:center;white-space:pre-wrap;"><u><span class="sqsrte-text-color--white"><strong>Built on Google Cloud</strong></span></u></p>
                    <p style="text-align:center;white-space:pre-wrap;" class="sqsrte-small"><span class="sqsrte-text-color--white">Built on the secure and reliable Google Cloud Platform, Cliniq gives you the flexibility to manage your practice securely from any device, anywhere, anytime.</span></p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="fe-block fe-block-b4d595237abbc0bcfeb9" style="grid-column: 6 / span 4;">
            <div class="sqs-block website-component-block sqs-block-html html-block sqs-background-enabled" data-block-css='["../css/website.components.html.styles.css"]' data-block-scripts='["../js/website.components.html.visitor.js"]' data-block-type="1337" id="block-b4d595237abbc0bcfeb9">
              <div class="sqs-block-content">
                <div class="sqs-text-block-container" style="background: hsla(0, 59%, 40%, 1); padding: 20px; border-radius: 8px;">
                  <div class="sqs-html-content">
                    <p style="text-align:center;white-space:pre-wrap;"><u><span class="sqsrte-text-color--white"><strong>HIPAA &amp; DPA Ready</strong></span></u></p>
                    <p style="text-align:center;white-space:pre-wrap;" class="sqsrte-small"><span class="sqsrte-text-color--white">Our platform is covered by a Google Workspace Business Associate Amendment (BAA) and is designed to meet the technical requirements of the Philippine Data Privacy Act.</span></p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Feature 4: Billing & Printables -->
          <div class="fe-block fe-block-59a246b20403e0a409a9" style="grid-column: 2 / span 4;">
            <div class="sqs-block website-component-block sqs-block-website-component sqs-block-image image-block" data-block-css='["../css/website.components.imagefluid.styles.css"]' data-block-scripts='["../js/2513.js","../js/8018.js","../js/9882.js","../js/website.components.imagefluid.visitor.js"]' data-block-type="1337" id="block-59a246b20403e0a409a9">
              <div class="sqs-block-content">
                <div class="fluid-image-component-root image-block-outer-wrapper design-layout-fluid">
                  <div class="fluid-image-container visitor-mode" style="border-radius: 10px; overflow: hidden;">
                    <img src="https://images.squarespace-cdn.com/content/v1/66332f216494c206f73b6e07/9c31f7cf-ced3-4dae-bd99-9dd5750392fd/Screenshot+from+2025-08-03+21-01-50.png" alt="Prescription and Records" style="width: 100%; display:block;" loading="lazy">
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="fe-block fe-block-7a7819fa5de177d08289" style="grid-column: 6 / span 4;">
            <div class="sqs-block website-component-block sqs-block-html html-block sqs-background-enabled" data-block-css='["../css/website.components.html.styles.css"]' data-block-scripts='["../js/website.components.html.visitor.js"]' data-block-type="1337" id="block-7a7819fa5de177d08289">
              <div class="sqs-block-content">
                <div class="sqs-text-block-container" style="background: hsla(184.44, 67%, 76%, 1); padding: 20px; border-radius: 8px;">
                  <div class="sqs-html-content">
                    <p style="text-align:center;white-space:pre-wrap;"><u><strong>Streamlined Billing &amp; Payment</strong></u></p>
                    <p style="text-align:center;white-space:pre-wrap;" class="sqsrte-small">Simplify finances by generating bills directly from appointments. Bills instantly appear on a centralised Payment tab for your staff to collect, eliminating lost charges and tedious manual tracking.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Feature 5: Clinical Co-Pilot -->
          <div class="fe-block fe-block-0bf13faa8d6170d90721" style="grid-column: 2 / -2; margin-top: 30px;">
            <div class="sqs-block website-component-block sqs-block-website-component sqs-block-html html-block" data-block-css='["../css/website.components.html.styles.css"]' data-block-scripts='["../js/website.components.html.visitor.js"]' data-block-type="1337" id="block-0bf13faa8d6170d90721">
              <div class="sqs-block-content">
                <div class="sqs-text-block-container">
                  <div class="sqs-html-content">
                    <h2 style="text-align:center;white-space:pre-wrap;">Your Clinical Co-Pilot</h2>
                    <p style="text-align:center;white-space:pre-wrap; max-width: 800px; margin: 10px auto;">Supplement your clinical judgement with a groundbreaking decision-support tool. Our AI analyses your consultation notes to provide potential differential diagnoses, offering an extra layer of confidence in your practice.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="fe-block fe-block-yui_3_17_2_1_1754214541128_38056" style="grid-column: 2 / -2;">
            <div class="sqs-block website-component-block sqs-block-image image-block" data-block-css='["../css/website.components.imagefluid.styles.css"]' data-block-scripts='["../js/2513.js","../js/8018.js","../js/9882.js","../js/website.components.imagefluid.visitor.js"]' data-block-type="1337" id="block-yui_3_17_2_1_1754214541128_38056">
              <div class="sqs-block-content">
                <div class="fluid-image-component-root image-block-outer-wrapper design-layout-fluid">
                  <div class="fluid-image-container visitor-mode" style="border-radius: 10px; overflow: hidden; max-width: 1000px; margin: 0 auto;">
                    <img src="https://images.squarespace-cdn.com/content/v1/66332f216494c206f73b6e07/e19e6b34-4996-4997-b081-30f0f6c76adc/Screenshot+from+2025-07-30+20-38-52.png" alt="Clinical AI Co-pilot Preview" style="width: 100%; display:block;" loading="lazy">
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Feature 6: Privacy Policy Call-to-action -->
          <div class="fe-block fe-block-3e70ccc251fd9eebdf20" style="grid-column: 2 / -2; margin-top: 30px;">
            <div class="sqs-block website-component-block sqs-block-html html-block" data-block-css='["../css/website.components.html.styles.css"]' data-block-scripts='["../js/website.components.html.visitor.js"]' data-block-type="1337" id="block-3e70ccc251fd9eebdf20">
              <div class="sqs-block-content">
                <div class="sqs-text-block-container">
                  <div class="sqs-html-content">
                    <h2 style="text-align:center;white-space:pre-wrap;">Your Patients, Your Data, Your Trust</h2>
                    <p style="text-align:center;white-space:pre-wrap; max-width: 800px; margin: 10px auto;">The trust between you and your patient is sacred. We built Cliniq to honour and protect that relationship. We will never sell your patient data, use it for advertising, or train external AI models with it.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="fe-block fe-block-yui_3_17_2_1_1755588790590_4398" style="grid-column: 2 / -2; text-align: center; margin: 20px 0;">
            <div class="sqs-block website-component-block sqs-block-button button-block" data-block-css='["../css/website.components.form.styles.css"]' data-block-type="1337" id="block-yui_3_17_2_1_1755588790590_4398">
              <div class="sqs-block-content">
                <div class="sqs-block-button-container sqs-block-button-container--center">
                  <a href="/cliniq/privacy" class="btn btn--border theme-btn--primary-inverse sqs-button-element--secondary" target="_blank" style="padding: 12px 28px; text-decoration: none; display: inline-block;">
                    Privacy Policy
                  </a>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</section>
<!-- END: Cliniq Features Section -->
"""

# 5. Insert section after the first section (Section ID 69ce5dcc6352dc7767a288c3)
html = re.sub(
    r'(<section[^>]*data-section-id="69ce5dcc6352dc7767a288c3"[^>]*>[\s\S]*?</section>)',
    r'\1\n\n' + new_section_code,
    html
)

# 6. Save output
with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: /cliniq/index.html created!")
EOF
