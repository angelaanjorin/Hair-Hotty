# Testing

This is the TESTING file for the [Hair Hotty](https://app-hairhotty-9ddf6a2299e6.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## Testing Contents  
  
- [Testing](#testing)
  - [Testing Contents](#testing-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Score](#wave-accessibility-score)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Responsiveness](#responsiveness)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
    - [Unresolved/Known Bugs](#unresolvedknown-bugs)


## Validation

### HTML Validation

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.
Via the deployed Heroku app link, I was able to carry out the validation using the url method.

![html validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733494370/Showing-results-for-https-app-hairhotty-9ddf6a2299e6-herokuapp-com-Nu-Html-Checker-12-06-2024_03_05_PM_kzihnh.png)  

All HTML pages were validated and received a 'No errors or warning to show' result as shown above.

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the JavaScript code added to the project. External JS, for Bootstrap, jQuery and Fontawesome purposes were not validated through JSHint.

| Page | Screenshot | Errors | Warnings |
| ---- | ---------- | ------ | -------- |
| bag | ![js from Bag page](docs/testing_images/home_script.png) | none | none |
| blog - Comment js | ![js from post section](docs/testing_images/post_js_valid.png) | none | none |
| Stripe JS | ![js from Stripe elements](docs/testing_images/stripe_js.png) | none | none |
| Products Product Detail Script | ![js from product detail script](docs/testing_images/quantity_input_script_js.png) | none (code has been highlighted red at the top of the code block but no errors returned from JSHint and code functions as intended. I could not get a definitive answer on why JSHint colours these lines red.) | none |
| Products Sort Selector Script | ![js from sort selector script](docs/testing_images/product_script.png) | none | none |
| Products Add Product Script | ![js from add product page](docs/testing_images/product_script.png) | none | none |
| Products Edit Product Script | ![js from edit product page](docs/testing_images/product_script.png) | none | none |
| Review - Ratings Selector Script | ![js from ratings selector script](docs/testing_images/base_script_valid.png) | none | none |
| Base Script | ![js from base script](docs/testing_images/base_script_valid.png) | none | none |

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files that were created or edited by myself. No issues presented and line lengths were double checked. I have included some screenshots with the results below. none = no issues present.

| Feature | admin | forms | models | urls | views | extra |
|---------|----------|----------|-----------|---------|----------|-------|
| bag | none ![python validation](docs/testing_images/a_admin.png) | none ![python validation](docs/testing_images/a_forms.png) | none ![python validation](docs/testing_images/a_models.png) | none ![python validation](docs/testing_images/a_urls.png) | none ![python validation](docs/testing_images/a_views.png) | n/a |
| blog  | n/a | n/a | n/a | none | none ![python validation](docs/testing_images/b_views.png) | contexts ![python validation](docs/testing_images/b_contexts.png) |
| Checkout | none ![python validation](docs/testing_images/c_admin.png) | none ![python validation](docs/testing_images/c_forms.png) | none ![python validation](docs/testing_images/c_models.png) | none | none ![python validation](docs/testing_images/c_views.png) | none ![python validation](docs/testing_images/c_webh.png) | n/a |
| Home | none | none | none | none | none ![python validation](docs/testing_images/h_views.png) | n/a |
| Products | none ![python validation](docs/testing_images/p_admin.png) | none ![python validation](docs/testing_images/p_forms.png) | none ![python validation](docs/testing_images/p_models.png) | none | none ![python validation](docs/testing_images/p_views.png) | none |
| Profiles | none | none ![python validation](docs/testing_images/pro_forms.png) | none ![python validation](docs/testing_images/pro_models.png) | none | none ![python validation](docs/testing_images/pro_views.png) | n/a |
| Reviews | none | none | none | none | none ![python validation](docs/testing_images/wish_views.png) | none |

### CSS Validation

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS files. External CSS for Bootstrap, provided by [CDN](https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css) was not tested.

I used the url of the deployed Heroku to carry out the validation. Results were good as shown below.
![css validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733494370/W3C-CSS-Validator-results-for-https-app-hairhotty-9ddf6a2299e6-herokuapp-com-CSS-level-3-SVG--12-06-2024_03_07_PM_anlvsa.png)


### Lighthouse Scores

### Lighthouse
Lighthouse was used to test Performance, Best Practices, Accessibility, and SEO on Desktop.

##### Desktop Results:
![Lighthouse Desktop Result](https://res.cloudinary.com/dzesjeplp/image/upload/v1733494370/Lighthouse-Report-Viewer-12-06-2024_02_14_PM_qgngib.png).

###### Mobile Results:
![Lighthouse Mobile Result](https://res.cloudinary.com/dzesjeplp/image/upload/v1733494370/Lighthouse-Report-Viewer-12-06-2024_02_18_PM_m0ygdz.png).


### Wave Accessibility Score

Accessibility was included in every planning stage for Hair Hotty, through the use of the WAVE report tool I could ensure that any necessary changes were made to make the website as accessible as it could be. Only 2 issues persisted with form labels. Form label was assigned to the newsletter field with hidden visibility styling applied in the CSS file, as it affected the form field positioning, but error persisted. No other issues, contrast or structural issues.

![WAVE Report](docs/testing_images/wave_report.png)  
*WAVE Report for Hair Hotty*

## Manual Testing

### User Input/Form Validation

Testing was carried out on desktop using a Chrome browser to ensure all forms take the intended input and process appropriately.

| Feature                    | Tested?  | User Input Required | User Feedback Provided     | Pass/Fail | Fix |
|----------------------------|----------|---------------------|----------------------------|-----------|-----|
| Navbar Logo and Icons      | Yes      | Click Links bring user to correct destination    | Text Colour Change/Icon Animation/Dropdowns | Pass | N/A |
| Home Page                  | Yes      | Hover/Click interactive features | Carousel moves, Accordion FAQ section | Pass | N/A |
| Register Page              | Yes      | Text Input/Click Links | Form field highlight/Font weight change on hover/Toast message | Pass | N/A |
| Email Validate             | Yes      | Click Links | Button animation/Toast message | Pass | N/A |
| Forgot Password            | Yes      | Text Input/Click Links | Form field highlight/Button animation/Toast message | Pass | N/A |
| Log In Page                | Yes      | Text Input/Click Links | Form field highlight/Font weight on hover/Toast message | Pass | N/A |
| Log Out Page               | Yes      | Click Links bring user to correct destination | Button animation/Font color change/Toast message | Pass | N/A |
| Account - Edit Address     | Yes      | Text Input/Click to Save | Form field highlight/Button animation/Toast message | Pass | N/A |
| Search                     | Yes      | Text Input/Click to Search | Pop up Modal/Form field highlight/Button Animation | Pass | N/A |
| Event                      | Yes      | Text Input/Click to Search | Pop up Modal/Form field highlight/Button Animation | Pass | N/A |
| Contact Us Form            | Yes      | Text Input/Click to Save | Pop up Modal/Form field highlight/Button animation | Pass | N/A |
| Blog index                 | Yes      | Text Input/Click to Search | Pop up Modal/Form field highlight/Button Animation | Pass | N/A |
| Blog detail                | Yes      | Text Input/Click to Search | Pop up Modal/Form field highlight/Button Animation | Pass | N/A |
| Newsletter Sign Up         | Yes      | Text Input/ Click to Subscribe | Button animation/New tab subscription confirmation | Pass | N/A |
| Products                   | Yes      | Click product brings user to product description | Pointer change on hover of products | Pass | N/A |
| Add Product                | Yes      | Navigated to Admin Dashboard, clicked 'Add Product', Completed form, Form submits correctly to display the product. | Form field highlight/Button animation/Toast message, new product uploaded. | Pass | N/A |
| Edit Product               | Yes      | Navigated to Admin Dashboard, clicked 'Edit Product', Completed form, Form submits correctly to display the edited product. | Form field highlight/Button animation/Toast message, product updated. | Pass | N/a |
| Add post                | Yes      | Navigated to Account for registered, clicked 'Add post', Completed form, Form submits correctly to display the post. | Form field highlight/Button animation/Toast message, new post uploaded. | Pass | N/A |
| Edit post               | Yes      | Navigated to Profile, my posts, clicked 'Edit post', Completed form, Form submits correctly to display the edited post. | Form field highlight/Button animation/Toast message, post edited and uploaded. | Pass | N/A |
| Product Quantity           | Yes      | Click increment/decrement | Colour change on hover/product quantity successfully changed | Pass | N/A |
| Product Sizes              | Yes      | Click dropdown/Click to select | Form field highlight/Size highlight | Pass | N/A |
| Checkout                   | Yes      | Click 'Secure Checkout', correct products in bag, entered delivery and payment details, submitted form to process payment. | Form field highlight/Button animation/Toast message, Loading spinner when processing order, order processed saved to account and email sent. | Pass | N/A |
| Footer                     | Yes      | Click Link brings user to FAQ section on Home Page | Font colour change on hover | Pass | N/A |
| Delivery Banner            | Yes      | Click dropdown to reveal banner | Dropdown arrow resize on hover/banner dropdown | Pass | N/A |

### Browser Compatibility

Hair Hotty was tested on the following browsers, purchases were made, post/products added/edited/deleted, error pages, all features were accessible and working as intended:

- Chrome v117.0.5938.92
- Firefox v114.0.2
- Edge v114.0.1823.79
- Safari v16.5.1

| Browser | Issue | Functionality |
|---------|-------|---------------|
| Firefox | None  | All Intact    |
| Edge    | None  | All Intact    |
| Safari (iPad Pro) | None | All Intact  |
| Chrome (Main browser used in development) | None | All Intact |

### Responsiveness

Using the Bootstrap framework allowed a more rapid development of a responsive website. Starting with mobile first, Hair Hotty was created to ensure the customer has an unhindered, positive experience when shopping. Hair Hotty was regularly tested during development using Dev Tools to check for display issues on iPhone4 -> iPhone 12/Samsung Galaxy S20, iPad/iPad Pro and laptop/desktop screen sizes. Once deployed to Heroku, Hair Hotty was tested on real world devices. No major issues were detected, changes were made to the checkout view to remove the product image on smaller screens and only display important product information. There were no major differences between desktop and tablet views thanks to the Bootstrap Grid system of columns. A selection of the screen size view differences are displayed below:

![Hair Hotty Desktop/Mobile Home](docs/testing_images/dt_mob_home_resp.png)  
*Hair Hotty Desktop/Mobile Home Responsive Views*

![Hair Hotty Desktop/Mobile Products](docs/testing_images/dt_mob_prod_resp.png)  
*Hair Hotty Desktop/Mobile Products Responsive Views*

![Hair Hotty Desktop/Mobile posts](docs/testing_images/dt_mob_art_resp.png)  
*Hair Hotty Desktop/Mobile posts Responsive Views*

![Hair Hotty Desktop/Mobile Bag](docs/testing_images/dt_mob_bag_resp.png)  
*Hair Hotty Desktop/Mobile Bag Responsive Views*

### Dev Tools/Real World Device Testing

Responsiveness testing was carried out using Google Dev Tools on the devices detailed within the below table. Responsiveness was evident on all features throughout all tested devices.

**Dev Tools Device Testing - all features tested, issues noted below**
| Device  | Feature    | Issue  | Fix  |
| ------- | ---------- | ------ |------|
| iPhone 4 | Order History table | Content overflow on y-axis | Separate media query created for screens max-width: 350px to cope with iPhone4 320px screen width, font-size reduced for order history table |
| iPhone12 Pro | All features | None | None  |
| Samsung Galaxy S20 | All features | None | None  |
| iPad Pro | All features | All features | None | None |

**Real World Device Testing**
| Device      | Feature    | Issue  | Fix  |
| ------------| ---------- | ------ |------|
| OPPO Reno 8 Lite |   All features    | No issues | None needed |
| iPhone XR | All features |  No issues  | None needed |
| iPhone 12  | All features | No issues | None needed |
| Samsung Galaxy S21 | All features | No issues | None needed |
| iPad Pro 2021 |    All features      |    No issues    |  None needed |
| Acer Aspire 3 2019 laptop | All features | No issues | None needed |


## Bugs

| No. | Bug | Solved | Fix | Solution Credit | Commit no. |
| --- | ---------------- | ---- | ------------- | -------------- | ------------|
| 1   | JavaScript dropdown menu fix | Yes | moving the mouseleave function outside of the main code seems to fix the 'dropdown menu randomly not appearing on hover' issue, This did not fix it, 2nd fix was to update to Bootstrap 4.6 and add 'ease' to menu hover transitions. Currently working consistently, 'pb-2' added to'all' fully fixed it | Investigating the CSS myself | e27b7a5/2aab065 |
| 2   | UnboundLocalError:Local variable 'categories' referenced before assignment & navbar active item styling. 'All' products option not displaying due to category = None when it was necessary for it to be categories. | Yes | Changed to categories = [] to initialize as empty list and added 'not request.GET.category' to 'all' nav-item li tag to remove bold styling when other product categories selected. | Stackoverflow <https://tinyurl.com/26a5ksrd> & CareerKarma <https://tinyurl.com/yc847kb7> | 76e8ef8 |
| 3   | Checkout form info not saving to Profile/Account form on checkout success. The 'save_info' section of checkout_success did not save the changed user info to the user's profile. | Yes | I considered that I may have caused an issue with my Wishlist app signals/contexts but after debugging there was no issue. Debugging with print statements to the terminal showed that the checkout form data was not being saved. I tried several fixes. First was to clear the site data via Dev Tools->Application->Clear Site Data and restart the server. No positive fix. I then backtracked to some earlier commits and removed the 'full_name' field that I had added to my UserProfile models and changed the '_' in checkout.html name='save_info' to name='save-info'. Tested my code with superuser and created a new user to find the issue resolved and no issue with Wishlist app. | Fix credit -> Gemma from Tutor Support for helping me to confirm my debugging process was correct and the 'Clear SiteData' tip, and a strong coffee for the second pass at spotting and fixing the bug. | 7659ada |
| 4  | Email Confirmation for order displaying multiple zeros at the end of the totals. | Yes | Fixed with 'floatformat:2' in confirmation_email.txt | Fixed by developer | 5774e14 |
| 5  | Bag 'Remove' removes all items with same id but different sizes, if I wanted to remove a medium black tshirt and leave the small black tshirt, code was removing both black tshirts. | Yes | Fixed in quantity_update_script, removed `'size':size` and replaced with `'product_size`:size as per the product models. | Fixed by developer | 3115569 |
| 6 | Sizes not showing in Checkout Success/Order History | Yes | Fixed by changing products.size to products_size | Fixed by developer, typo | b5f04cb |


### Unresolved/Known Bugs

