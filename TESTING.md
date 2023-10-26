# Testing
- [Testing](#testing)
  - [Code Validation](#code-validation)
    - [HTML Testing](#html-testing)
    - [Python Testing](#python-testing)
    - [JavaScript Testing](#javascript-testing)
    - [CSS Testing](#css-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Browser Compatibility](#browser-compatibility-1)
  - [Responsiveness Test](#responsiveness-test)
  - [Fixed Bugs](#fixed-bugs)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Additional Testing](#additional-testing)
    - [Lighthouse](#lighthouse)
    - [Results from Lighthouse](#results-from-lighthouse)
    - [Results from Lighthouse](#results-from-lighthouse-1)
    - [User Stories Testing](#user-stories-testing)
    - [Manual Testing](#manual-testing)

## Code Validation

[Back to top](#testing)
### HTML Testing
[Back to top](#testing)

### Python Testing
[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files which were created or edited by me.
[Back to top](#testing)

### JavaScript Testing
[Back to top](#testing)

### CSS Testing
## Browser Compatibility
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS file. External CSS for Bootstrap, provided by CDN was not tested. No errors were found.
[Back to top](#testing)

## Browser Compatibility
[Back to top](#testing)

## Responsiveness Test
[Back to top](#testing)

## Fixed Bugs

|                                        BUG                                       | WHERE |                                      HOW                                      |                   COMMIT                   |
|:--------------------------------------------------------------------------------:|:-----:|:-----------------------------------------------------------------------------:|:------------------------------------------:|
| The quantity of books in the shopping bag was not updating.| bag.html  | I had to take away the "href" element from the respective buttons.| [b3393b9](https://github.com/lucia2007/bookwormkid/commit/b3393b91866a5edf35f3e44bdd5cc408c3a815cb)  |
| The crispy_forms were not loading correctly | settings.py  | I had to correct a typo.| [af52cfe](https://github.com/lucia2007/bookwormkid/commit/af52cfe5f13c18af0ea7817c1164507551d9b475)  |
| The 404 page was not applying custom template | settings.py  | I had to move content from settings.py to urls.py| [af52cfe](https://github.com/lucia2007/bookwormkid/commit/f60afce6a6725faf30e0ae3b6ba7b95f1e5845df) and [3c048ce](https://github.com/lucia2007/bookwormkid/commit/3c048cebbd26b0f8a9c2ddeec379d0b1976da38c) |
| The 403 and 500 error pages were not applying custom template | views.py, urls.py  | I had made several messy commits trying to see if the error pages worked on the deployed app. In the end I reverted to the simplest option, just define error pages in the templates directory without any views.py or urls.py error code| [ and several previous commits](https://github.com/lucia2007/bookwormkid/commit/307f044cdbea30b665fed8fad6a2702213ab3aa5)
| My user registration and email sending for order confirmation stopped working | settings.py, gmail, heroku  | I'll provide a more detailed explanation below*. | [a960055](https://github.com/lucia2007/bookwormkid/commit/a960055f60ad0a04dc4192ae04a5a7e9c790ee9b) and [965c607](https://github.com/lucia2007/bookwormkid/commit/965c607c8a8115a25ff0d8d199aeccf2f7cf8f40)
| "Country" label was appearing twice in my checkout form | checkout/forms.py  | I had to correct the indentation error. | [1b653a2](https://github.com/lucia2007/bookwormkid/commit/1b653a2269432d69ce9bb975befc7c77253bb056)
| Wishlist items were rendering incorrectly | wishlist.html  | I had several indentation errors and wrong order of elements which I had to fix. | [d34b771](https://github.com/lucia2007/bookwormkid/commit/d34b7719ce77c698882f2e196511dd930ce3bb9c)
| My Wishlist context processor wasn't working due to inconsistencies in the code. | wishlist/contexts.py  | I had to correct the variable names in the file. | [81af4d7](https://github.com/lucia2007/bookwormkid/commit/81af4d793bc781c0e49183faaa7d9b322c0f5788)
| Noimage placeholder picture was not displaying for articles if no image provided. | article/models.py  | I had to get rid of default=placaholder for the image in the model. | [230333b](https://github.com/lucia2007/bookwormkid/commit/230333bfd2a23d9d75752c0d82a983e7785323ad) and [6a935d8](https://github.com/lucia2007/bookwormkid/commit/6a935d8f37bfcfdba8816842b5de491ed9f88f51)
| Adding a draft of an article would take me to a 404 page | article/views.py  | I had to update my views, espcially take away the status=1 condition from my detail views. | [692d357](https://github.com/lucia2007/bookwormkid/commit/692d357d724180422312cac204d2658e11846187)
| Article edit picture was not working - tip from tutor| article/views.py  | I had to add request.files to my view | [9728fc8](https://github.com/lucia2007/bookwormkid/commit/9728fc809f60383ea2b28eca683dde7bd342af25)
| Class "{%" duplicated| products.html  | products.html| I had change the place where I added the condition for filters** | [dccafb7](https://github.com/lucia2007/bookwormkid/commit/dccafb7b55aec72f89a381019eabd77c4caec305)
| Avoid anonymous user error for reviews  | product_detail.html, products/views.py| I had to switch the order of the conditions | [e9e9b23](https://github.com/lucia2007/bookwormkid/commit/e9e9b23a5b90202e3bc693b736833941e565847a)
| 'AnonymousUser' object is not iterable (max 1 review) and wrong rendering  | products.html, product_detail.html, products/views.py| I had to switch the order of the if conditions and add a @login_required decorator to my view| [59fc46d](https://github.com/lucia2007/bookwormkid/commit/59fc46daea23bf228de2c7288e244c4100fb96c6)



* My registration and email confirmation for orders stopped working for all users but admin. This was partly due to the fact, that I attempted to use aws ses functionality for sending emails for my contact form. I later found out that aws ses in the basic version would allow sending emails only to verified email addresses, which couldn't be done when a new user was being created, as his email address was new and not verified. I found out that if I used a "helping email address" success@simulator.amazonses.com, everything worked fine. If I wanted aws ses to send emails to nonverified email address, I would have to ask for a personal approval from Amazon. As it was proving quite complicated, I opted to revert back to the previous smtp functionality. Neverthless, the problem persisted even after that. With tutor support we were able to discover that my "app password" in my gmail account got deleted (without any action on my side) and thus the email functionality stopped working. When I created a new app and reset the password in Heroku, everything started working again. I hope this problem doesn't happen again, as it's completely out of my control if Google decided to delete my "app password" for some reason.
[Error due to deleted app password](/testing_images/smtp_error.png)

** There are quite a few commits around my product filters and highlighting of the chosen age segment, as I was trying to figure out ways how to do it more efficiently and more simply. There was a lot of back and forth, and some unnecessary or duplicated commits, and even though I know the code could still be refactored, I feel that at the moment it is finally easily legible and understandable.
## Unfixed Bugs

[Back to top](#testing)

## Additional Testing
### Lighthouse

The application was also tested using [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome Developer Tools. The following aspects were tested:

- Performance - reveals how the site performs during loading
- Accessibility - shows if the site if accessible for all users and suggests ways to improve it
- Best Practices - indicates if the site conforms to industry best practices
- SEO - Search Engine Optimisation - shows if the site is optimised for search engine result rankings

### Results from Lighthouse
| Page | Validation Results |
| ---- | ---------- |
| Home | [Home Page Score](./testing-images/lighthouse_homepage.png) |
| Contact Us | [Contact Us Score](./testing-images/lighthouse_contactus.png) |
| Products | [Products Score](./testing-images/lighthouse_products.png) |
| Product Details | [Product Details](./testing-images/lighthouse_product_detail.png) |
| Admin Dashboard | [Admin Dashboard](./testing-images/lighthouse_admin_dashboard.png) |
| Shopping Bag | [Shopping Bag Score](./testing-images/lighthouse_shopping_bag.png) |
| Checkout | [Checkout Score](./testing-images/lighthouse_checkout.png) |
| Articles | [Articles Score](./testing-images/lighthouse_articles.png) |
| Article Details | [Article Details](./testing-images/lighthouse_article_detail.png) |
| Wishlist | [Wishlist Score](./testing-images/lighthouse_wishlist.png) |
| Profile | [Profile Score](./testing-images/lighthouse_profile.png) |
| Enquiries | [Enquiries Score](./testing-images/lighthouse_enquiries.png) |
| Sign In | [Sign In Score](./testing-images/lighthouse_login.png) |
| Sign Up | [Sign Up Score](./testing-images/lighthouse_signup.png) |
| Sign Out | [Sign Out Score](./testing-images/lighthouse_logout.png) |

I continuously worked on improving the individual scores and tried to reflect on the warnings in the Lighthouse which lead to the score increase. For increasing accessibility I had to change many button names as I was not using their explicit description and for performance I used [tiny png](tinypng.com) and [convertio](convertio.co) and [i love img](https://www.iloveimg.com/) to decrease their size and change them to webp where possible. However, I couldn't do this for all of my images, espcially for the book covers, as sometimes I was not able to find a large enough image of a book I needed.

All of my scores for all of the pages were above 90, often close to 100. On a couple of pages the "SEO" score is slightly lower. This is due to the presence of a "back to top" button which has no href value and thus is not crawlable. I also got a lower score on Best Practices, due to [issues](./testing-images/stripe_cookies.png) which were logged into the console and have to do with using stripe cookies. Sometimes my scores for performance differed, probably due to current connection speed.


### Results from Lighthouse
| Page | Validation Results |
[Back to top](#testing)

### User Stories Testing
[Back to top](#testing)

### Manual Testing

[Back to top](#testing)