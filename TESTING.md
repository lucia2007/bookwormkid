# Testing
- [Testing](#testing)
  - [Code Validation](#code-validation)
    - [HTML Testing](#html-testing)
    - [Python Testing](#python-testing)
    - [JavaScript Testing](#javascript-testing)
    - [CSS Testing](#css-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Responsiveness Test](#responsiveness-test)
  - [Fixed Bugs](#fixed-bugs)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Additional Testing](#additional-testing)
    - [Lighthouse](#lighthouse)
    - [Results from Lighthouse](#results-from-lighthouse)
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
* My registration and email confirmation for orders stopped working for all users but admin. This was partly due to the fact, that I attempted to use aws ses functionality for sending emails for my contact form. I later found out that aws ses in the basic version would allow sending emails only to verified email addresses, which couldn't be done when a new user was being created, as his email address was new and not verified. I found out that if I used a "helping email address" success@simulator.amazonses.com, everything worked fine. If I wanted aws ses to send emails to nonverified email address, I would have to ask for a personal approval from Amazon. As it was proving quite complicated, I opted to revert back to the previous smtp functionality. Neverthless, the problem persisted even after that. With tutor support we were able to discover that my "app password" in my gmail account got deleted (without any action on my side) and thus the email functionality stopped working. When I created a new app and reset the password in Heroku, everything started working again. I hope this problem doesn't happen again, as it's completely out of my control if Google decided to delete my "app password" for some reason.
[Error due to deleted app password](/testing_images/smtp_error.png)
## Unfixed Bugs

[Back to top](#testing)

## Additional Testing
### Lighthouse

### Results from Lighthouse
| Page | Validation Results |
[Back to top](#testing)

### User Stories Testing
[Back to top](#testing)

### Manual Testing

[Back to top](#testing)