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

I had to follow a different approach for validating my HTML for this project as the majority of my pages are developed using Jinja syntax such as '{% extends "base.html" %}' and '{{ form|crispy }}' and most require user authentication. The HTML validator will throw errors if I were to use my website's URL so I have had to follow the below approach for every page:

- Via the deployed Heroku app link, I navigated to each individual page.
- Right clicking on the screen/CTRL+U/⌘+U on Mac, allows a menu to appear, giving me the option to 'View page source'.
- The complete HTML code for the deployed page will appear, allowing me to select the entire code using CTRL+A/⌘+A on Mac.
- Paste the copied code into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, revalidate by following the above steps and record the results.

![html validation](docs/testing_images/html_validation.png)  

All HTML pages were validated and received a 'No errors or warning to show' for code that I had written, result as shown above.

| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- |
| Home | 0 | 0 |
| Log In | 0 | 0 |
| Register | 0 | 0 |
| Logout | 0 | 0 |
| Email Confirmation Sent | 0 | 0 |
| Email Confirmation | 0 | 0 |
| Account | 0 | 0 |
| Admin Project Management | 0 | 0 |
| Admin and User Add post | 0 | 0 |
| Admin Edit post | 0 | 0 |
| Admin Delete post | 0 | 0 |
| Admin Product Detail | 0 | 0 |
| Admin Add Product | ID error -> Errors/Warnings present as a result of Bootstraps form elements, not from the code that I have created. The name ID from the contact form html within the base.html is clashing with the name ID from the add product html. These ID elements are embedded within the Bootstrap forms and are inaccessible to me without breaking my code up and reconfiguring the code. This is the same for the `<p>` and `<strong>` error. This was double checked with the Assessment Team Oct'23 who confirmed that code not authored by myself, and is Bootstrap/CrispyForms rendering, would not be subject to assessment mark down as long as it is referenced in the README. I will reinvestigate and break into the code when my Diploma has been awarded to remove errors like these. ![html validation duplicate id bootstrap forms](docs/testing_images/add_prod_er.png) | As before |
| Admin Edit Product | 0 | 0 |
| Admin Delete Product | 0 | 0 |
| All Products | 0 | 0 |
| User Product Detail | 0 | 0 |
| Review Delete | 0 | 0 |
| Bag - Empty | 0 | 0 |
| Bag - Products | 0 | 0 |
| Checkout | Errors/Warnings present as a result of Bootstraps form elements, not from the code that I have created. The name/email ID from the contact form html within the base.html is clashing with the name/email ID from the checkout html. These ID elements are embedded within the Bootstrap forms and are inaccessible to me without breaking my code up and reconfiguring the code. This was double checked with the Assessment Team Oct'23 who confirmed that code not authored by myself, and is Bootstrap/CrispyForms rendering, would not be subject to assessment mark down as long as it is referenced in the README. I will reinvestigate and break into the code when my Diploma has been awarded to remove errors like these. ![html validation duplicate id bootstrap forms](docs/testing_images/contactus_form_id.png) ![html validation duplicate id bootstrap forms](docs/testing_images/contact_html_issue.png) | As before |
| Checkout Success | 0 | 0|
| Profile/Account | 0 | 0 |
| Order History | 0 | 0 |
| Wishlist | 0 | 0 |
| Blog | 0  | 0 |
| Blog Detail Page | 0  | 0 |
| Blog - Add a Post | 0 | 0 |
| Events | 0 | 0 |
| Contact | 0 | 0 |
| Footer - Returns | 0  | 0 |
| Footer - About us | 0 | 0 |
| Footer    | Privacy Policy | External link - N/A | External link - N/A |
| Footer - FAQ  | Outside of my control there are multiple errors present as this page contains HTML Content from [Termly.com](https://termly.io/products/terms-and-conditions-generator/) to display the Terms & Conditions for Hair Hotty. None of my templated code contains errors and I felt that attempting to correct all of the Termly errors would render the document incorrectly. I used Termly as they provided this content without personal cost to me. | As before. |
| Forgot Password | 0 | 0 |
| Error 403 | 0 | 0 |
| Error 404 | 0 | 0 |
| Error 500 | 0  | 0 |

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

To keep my document concise I have not included every screenshot of the CSS validations, as they are all the same, but the results are as follows.
![css validation](docs/testing_images/css_validation.png)

| CSS File | Errors | Warnings |
| ---- | ------ | -------- |
| blog | 0 | 0 |
| Checkout | 0 | 0 |
| Base CSS | 0 | 0 |

### Lighthouse Scores

Lighthouse testing was carried out in Incognito mode to achieve the best result. Images used in the site's design were saved in png format, and compressed using [tinypng](https://tinypng.com/) and [Convertio](https://www.convertio.co) to offer the best chance for a decent performance score.

| Page | Lighthouse Scores - Desktop | Notes |
| ---- | ----------------- | -------- |
| Home |   ![lighthouse home](docs/testing_images/home_lh.png)   |    ![best practise errors](docs/testing_images/home_lh_bp.png)  Score lower due to aspect ratio or images, not using webp images and Stripe Cookie    |
| All  |  ![lighthouse all](docs/testing_images/prod_lh.png)  |  None        |
| Read  | ![lighthouse post](docs/testing_images/post_lh.png)   |   None  |
| Account |  ![lighthouse account](docs/testing_images/profile_lh.png)              |    As before with Stripe Cookie  |
| Wishlist |  ![lighthouse wishlist](docs/testing_images/wishlist_lh.png)   |  As before with images rendering and Stripe Cookie   |

| Page | Lighthouse Scores - Mobile | Notes |
| ---- | ----------------- | -------- |
| Home |  ![lighthouse home](docs/testing_images/home_moblh.png) | ![performance errors](docs/testing_images/home_perform_mob_er.png) Score lower due to images not being webp and STripe/jQuery CDN. I will look into this for future versions to better understand how I can improve this score.  |
| All  | ![lighthouse all products mobile](docs/testing_images/all_moblh.png)   | As before  |
| Read |  ![lighthouse post mobile](docs/testing_images/read_moblh.png) |  As before  |
| Account | ![lighthouse account mobile](docs/testing_images/account_moblh.png)   |  As before  |
| Wishlist | ![lighthouse wishlist mobile](docs/testing_images/wishlist_moblh.png)  | As before   |

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
