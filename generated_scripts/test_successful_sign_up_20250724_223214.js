Sure! Here's an example of a Playwright test script in JavaScript for testing a successful sign-up process on a website:

```javascript
const { test, expect } = require('@playwright/test');

test('Successful Sign Up Test', async ({ page }) => {
  // Navigate to the sign-up page
  await page.goto('https://example.com/signup');

  // Fill in the sign-up form
  await page.fill('input[name=username]', 'testuser');
  await page.fill('input[name=email]', 'testuser@example.com');
  await page.fill('input[name=password]', 'P@ssw0rd');
  
  // Submit the sign-up form
  await Promise.all([
    page.waitForNavigation(), // Wait for navigation after form submission
    page.click('button[type=submit]'),
  ]);

  // Assertion: Check if sign-up was successful by verifying the presence of a success message
  const successMessage = await page.waitForSelector('.success-message');
  expect(successMessage).not.toBeNull();
});
```

In this test script:
- The test navigates to the sign-up page of the website.
- It fills in the sign-up form with a username, email, and password.
- Submits the form and waits for the page navigation to complete.
- Asserts that a success message element is present on the page after successful sign-up.

You can customize this script by replacing the URL, form selectors, and success message selector with the actual elements on the website you are testing.