#!/bin/bash
# Run this from the root of the "site" repo.
# Deletes files left over from the original Squarespace export that
# index.html and cart.html never actually load.
# Reduces the repo from ~20MB to roughly 12MB and removes ~55 dead files.

set -e

echo "Deleting unused JS files..."
rm -fv \
  "js/11365-af10a1016cd99959-min.en-us.js" \
  "js/12966-911558c03f24abc2-min.en-us.js" \
  "js/1480.6a039b1d3b8174bc9169.js" \
  "js/20641-6e097976b40cda35-min.en-us.js" \
  "js/20893-90e77cf4a67d86ca-min.en-us.js" \
  "js/21955-3ae2fbde27c25db8-min.en-us.js" \
  "js/28381-6eeb9be5f9a5650d-min.en-us.js" \
  "js/4150-5909853fcbc126f4-min.en-us.js" \
  "js/4533-99b4d4c8910c759d-min.en-us.js" \
  "js/45779-1b560e815538deda-min.en-us.js" \
  "js/48844-27ec400f5141e6f6-min.en-us.js" \
  "js/49484-9e48d5c3e4c2a05a-min.en-us.js" \
  "js/50785-5da795d97049b11f-min.en-us.js" \
  "js/5624-6de7e74933038745-min.en-us.js" \
  "js/59970-9c2cce5fbdc39394-min.en-us.js" \
  "js/60905-f4dca42d521f9cd9-min.en-us.js" \
  "js/64255-c44879529f42fe5f-min.en-us.js" \
  "js/66539-5025843b199c43ea-min.en-us.js" \
  "js/68506-6473509688c74fc1-min.en-us.js" \
  "js/82365-7f8bed8d727a2323-min.en-us.js" \
  "js/88124-98b8a9c74273d635-min.en-us.js" \
  "js/9000-5a686b1ad079101e-min.en-us.js" \
  "js/92732-75bfd823e49b80db-min.en-us.js" \
  "js/announcement-bar-d4678424f437df6d-min.en-us.js" \
  "js/api-b84474e915fb8e25a5cb4d08c9def42a8d817701.json" \
  "js/api-c333c2e0c72aace1fab49ccb0af4c60156e0060c.json" \
  "js/async-commerce-cart-page-093abf4fe6ad6924-min.en-us.js" \
  "js/async-commerce-cart-utils-b95e5c25201e0c59-min.en-us.js" \
  "js/async-editor-render-form-b26d521458ba1882-min.en-us.js" \
  "js/async-reserved-cart-bootstrap-cb36473b5ae5727e-min.en-us.js" \
  "js/audio-player-514542fb02d4df02-min.en-us.js" \
  "js/blog-collection-list-804d48b04f8cd8a1-min.en-us.js" \
  "js/calendar-block-renderer-f0e137ac37b7f0da-min.en-us.js" \
  "js/chartjs-helpers-09376c2f45ec20f7-min.en-us.js" \
  "js/comments-0735903c3390a85b-min.en-us.js" \
  "js/custom-css-popup-42e962b319f0f4b8-min.en-us.js" \
  "js/dialog-bd29ca2eee5f2e9b-min.en-us.js" \
  "js/events-collection-13c2437af94dafdd-min.en-us.js" \
  "js/floating-cart.333bd5aee1885e7af603.js" \
  "js/form-rendering-utils-8fe5c1b8f6959960-min.en-us.js" \
  "js/forms-0dcfd8c7776077c9-min.en-us.js" \
  "js/gallery-collection-list-7b9e3df420b8fb7f-min.en-us.js" \
  "js/image-zoom-8fb2d4ed417f5ff2-min.en-us.js" \
  "js/pinterest-968984184bd859b5-min.en-us.js" \
  "js/popup-overlay-e88a7350201cc845-min.en-us.js" \
  "js/product-quick-view-513b4e12764095c4-min.en-us.js" \
  "js/products-collection-item-v2-99be948a1d39ff28-min.en-us.js" \
  "js/products-collection-list-v2-776747e4add9de69-min.en-us.js" \
  "js/search-page-1721871070660031-min.en-us.js" \
  "js/search-preview-f97149f7780b93e3-min.en-us.js" \
  "js/simple-liking-69bfa10d1d97bade-min.en-us.js" \
  "js/social-buttons-e24c985bee0ba84a-min.en-us.js" \
  "js/tourdates-02b44412c18997bc-min.en-us.js" \
  "js/user-items-list-banner-slideshow.9f86135f51b7e996c126.js" \
  "js/website-overlays-manager-2c682d73aea4d0be-min.en-us.js"

echo "Deleting unused CSS files..."
rm -fv \
  "css/35ebb88013744865-min.en-us.css" \
  "css/8308d1793f387442-min.en-us.css" \
  "css/audio-player-b05f5197a871c566-min.en-us.css" \
  "css/blog-collection-list-b4046463b72f34e2-min.en-us.css" \
  "css/calendar-block-renderer-c3fef2a497c8e56b-min.en-us.css" \
  "css/chartjs-helpers-96b256171ee039c1-min.en-us.css" \
  "css/comments-a36683985f50ad04-min.en-us.css" \
  "css/custom-css-popup-73960f21c0cb9638-min.en-us.css" \
  "css/dialog-86aacd645d83874c-min.en-us.css" \
  "css/events-collection-c3fef2a497c8e56b-min.en-us.css" \
  "css/ff4141f93023f219-min.en-us.css" \
  "css/forms-0afd3c6ac30bbab1-min.en-us.css" \
  "css/gallery-collection-list-b4046463b72f34e2-min.en-us.css" \
  "css/image-zoom-b4046463b72f34e2-min.en-us.css" \
  "css/pinterest-b4046463b72f34e2-min.en-us.css" \
  "css/popup-overlay-b742b752f5880972-min.en-us.css" \
  "css/product-quick-view-0afd3c6ac30bbab1-min.en-us.css" \
  "css/products-collection-item-v2-b4046463b72f34e2-min.en-us.css" \
  "css/products-collection-list-v2-b4046463b72f34e2-min.en-us.css" \
  "css/search-page-90a67fc09b9b32c6-min.en-us.css" \
  "css/simple-liking-701bf8bbc05ec6aa-min.en-us.css" \
  "css/social-buttons-95032e5fa98e47a5-min.en-us.css" \
  "css/tourdates-b4046463b72f34e2-min.en-us.css" \
  "css/website-overlays-manager-07ea5a4e004e6710-min.en-us.css"

echo "Deleting unused Squarespace editor images/icon fonts..."
rm -fv \
  "images/edit-aviary-light.png" \
  "images/edit-aviary-light-2x.png" \
  "images/edit-info-light.png" \
  "images/edit-info-light-2x.png" \
  "images/error-dark.png" \
  "images/error-dark-2x.png" \
  "images/getty-16-light.png" \
  "images/getty-32-light.png" \
  "images/icon-settings-16-light.png" \
  "images/icon-video-24-light-solid.png" \
  "images/icon_close_7_light.png" \
  "images/play-button.png" \
  "images/play-button-2x.png" \
  "images/shopping-cart-16-light.png" \
  "images/shopping-cart-32-light.png" \
  "images/trash-9-light.png" \
  "images/trash-9-light-2x.png" \
  "images/trash-9-red.png" \
  "images/trash-9-red-2x.png" \
  "images/social-icon-font.eot" \
  "images/social-icon-font.svg" \
  "images/social-icon-font.ttf" \
  "images/social-icon-font.woff" \
  "images/squarespace-ui-font.eot" \
  "images/squarespace-ui-font.svg" \
  "images/squarespace-ui-font.ttf" \
  "images/squarespace-ui-font.woff"

echo "Done. Review 'git status', then commit and push."

# ---------------------------------------------------------------------
# OPTIONAL — only run this once you've fixed/replaced the contact form
# and removed the cart icon link from index.html's nav. cart.html is a
# dead Squarespace e-commerce page; it has no products and, since this
# is now a static GitHub Pages site with no Squarespace backend, its
# checkout flow cannot work.
# ---------------------------------------------------------------------
# rm -fv cart.html
