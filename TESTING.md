# Testing

This is the TESTING file for the [Hair Hotty](https://app-hairhotty-9ddf6a2299e6.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## Validation

### HTML Validation

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.
Via the deployed Heroku app link, I was able to carry out the validation using the url method.

![html validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733494370/Showing-results-for-https-app-hairhotty-9ddf6a2299e6-herokuapp-com-Nu-Html-Checker-12-06-2024_03_05_PM_kzihnh.png)  

All HTML pages were validated and received a 'No errors or warning to show' result as shown above.

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the JavaScript code added to the project. External JS, for Bootstrap, jQuery and Fontawesome purposes were not validated through JSHint.

| Page | Screenshot | Errors |
| ---- | ---------- | ------ | -------- |
| bag | ![js from Bag page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500628/JSHint-bag_u7ggll.png) | none |
| blog - Comment js | ![js from post section](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500628/JSHint-comments-blog_blri1k.pngg) | none |
| Stripe JS | ![js from Stripe elements](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500628/JSHint-a-JavaScript-stripe_oyrfik.png) | none |
| Products Product quantitiyinput Script | ![js from product quantityinput script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500626/JSHint-a-JavaScript-quantityinput_haelbp.png) | none (code has been highlighted red at the top of the code block but no errors returned from JSHint and code functions as intended. I could not get a definitive answer on why JSHint colours these lines red.) |
| Products  | ![js from sortproducts script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500626/JSHint-a-JavaScript-sortproducts_houdhz.png) | none |
| Products Add and Edit Product Script | ![js from add and edit product page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500625/JSHint-a-JavaScript-add-products_vqifrh.png) | none |
| Products Productdetail Script | ![js from productdetail page](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500626/JSHint-a-JavaScript-productdetail_exlvow.png) | none |
| Profile| ![js myposts script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500625/JSHint-a-JavaScript-mypostsprofile_vkg0d9.png) | none |
| Review - Ratings Selector Script | ![js from ratings selector script](docs/testing_images/base_script_valid.png) | none |
| Base Script | ![js Sort Selector Script script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500626/JSHint-a-JavaScript-sortselectorproduct_mmq6xz.png) | none |
| Base Script | ![js mailchimp script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500625/JSHint-a-JavaScript-mailchimp_ddtl2s.png) | none |
| Base Script | ![js toast script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500628/JSHint-a-JavaScript-toast_bsjawq.png) | none |
| Base Script | ![js quantityinput script](https://res.cloudinary.com/dzesjeplp/image/upload/v1733500626/JSHint-a-JavaScript-quantityinputforstockcontrol_c4zd0z.png) | none |

<a href="#top">Back to the top.</a>

### Python Validation

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files that were created or edited by myself. No issues presented and line lengths were double checked. I have included some screenshots with the results below. none = no issues present.

| Feature | admin | forms | models | urls | views | extra |
|---------|----------|----------|-----------|---------|----------|-------|
| bag  | n/a | n/a | n/a | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733510719/CI-Python-Linter-urlsbag_n6eg8u.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512156/CI-Python-Linter-bagviews_fknnha.png) | contexts ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733510719/CI-Python-Linter-bagcontexts_lx7vlb.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733510719/CI-Python-Linter-bagutils_gwbtlc.png) |
| blog | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512429/CI-Python-Linter-adminblog_pe1zxz.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512430/CI-Python-Linter-blogforms_mfq4kl.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512430/CI-Python-Linter-blogmodels_xhwggp.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512431/CI-Python-Linter-blogurls_kggm96.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733515136/CI-Python-Linter-blognewviews_xvwhsa.png) | n/a |
| Checkout | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512593/CI-Python-Linter-checkoutadmin_k7f4kw.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512594/CI-Python-Linter-checkoutforms_me2jcn.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512596/CI-Python-Linter-chheckoutmodels_tqugaf.png) | none | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512595/CI-Python-Linter-checkouturls_iqyzmb.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512596/CI-Python-Linter-checkoutviews_dbmaiy.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512595/CI-Python-Linter-checkoututility_ahxmqh.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512594/CI-Python-Linter-checkoutsignals_qfk07w.png)|
| Home | n/a | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512942/CI-Python-Linter-homeforms_ya81p7.png)| n/a |none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512942/CI-Python-Linter-homeurls_iedc23.png)| none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733512942/CI-Python-Linter-homeviews_fv8q4z.png) | n/a |
| Products | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513124/CI-Python-Linter-productsadmin_fppzrq.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513125/CI-Python-Linter-productsforms_ucxbmh.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513125/CI-Python-Linter-productsmodel_oqvigt.png) | none![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513126/CI-Python-Linter-productsurls_fq70b0.png)| none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513127/CI-Python-Linter-productsviews_nqf0uf.png) | none |none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513126/CI-Python-Linter-productsutils_j09leh.png) | none |
| Profiles | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513347/CI-Python-Linter-profilesadmin_si7b2n.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513347/CI-Python-Linter-profilesforms_iezoxf.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513348/CI-Python-Linter-profilesmodels_pgkwob.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513349/CI-Python-Linter-profilesurls_aoeemv.png)| none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513349/CI-Python-Linter-profilesviews_kjqgqf.png) | n/a |
| Reviews | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513594/CI-Python-Linter-reviewsadmin_y4yotd.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513595/CI-Python-Linter-reviewsforms_yau10a.png) | none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513595/CI-Python-Linter-reviewsmodels_xmsmqh.png)| none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513596/CI-Python-Linter-reviewsurls_s1xag2.png)| none ![python validation](https://res.cloudinary.com/dzesjeplp/image/upload/v1733513597/CI-Python-Linter-reviewsviews_rdtjiu.png) | n/a |

<a href="#top">Back to the top.</a>

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

![WAVE Report](https://res.cloudinary.com/dzesjeplp/image/upload/v1733498867/WAVE-Report-of-Hair-Hotty_o5azwo.png)  
*WAVE Report for Hair Hotty*

<a href="#top">Back to the top.</a>

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

![Hair Hotty Desktop/Mobile Home]()  
*Hair Hotty Desktop/Mobile Home Responsive Views*

![Hair Hotty Desktop/Mobile Products]()  
*Hair Hotty Desktop/Mobile Products Responsive Views*

![Hair Hotty Desktop/Mobile posts]()  
*Hair Hotty Desktop/Mobile posts Responsive Views*

![Hair Hotty Desktop/Mobile Bag]()  
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

<a href="#top">Back to the top.</a>