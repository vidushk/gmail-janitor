## Gmail Janitor
### About
Gmail Janitor is a python script that is able to sort mail into filters and can automatically delete them if after a certain period of time, given the script is run routinely.
This is built this using Jeremy Ephron’s [simplegmail](https://github.com/jeremyephron/simplegmail) python library that makes handling Gmail’s API a lot easier.
It uses Excel as a config to easily edit, add, or change filters.
**Note: This will only work for Gmail, as it uses the Gmail API and not IMAP.**
#### Optimal Usage
The most optimal way of using this script is having it automatically run on a schedule. The idea is that instead of constantly running the script manually, you use a scheduler (cron, launchd, Task Scheduler, etc.) to automatically run in the background so it will constantly be filtering and deleting old mail.
#### Getting Started and Installation
1. Here are the following python libraries you need for the script. To install them:
##### Pandas
    pip3 install pandas
##### simplegmail
    pip3 install simplegmail

2. First you need to download an OAuth 2.0 Client ID file to get access to the Gmail API. I’ve posted the tutorial from Jeremy Ephron’s readme but you can also access it [here](https://github.com/jeremyephron/simplegmail#getting-started).

> The only setup required is to download an OAuth 2.0 Client ID file
> from Google that will authorize your application.
> 
> This can be done at:
> https://console.developers.google.com/apis/credentials. For those who
> haven't created a credential for Google's API, after clicking the link
> above (and logging in to the appropriate account),
> 
> Select/create the project that this authentication is for (if creating
> a new project make sure to configure the OAuth consent screen; you
> only need to set an Application name)
> 
> Click on the "Dashboard" tab, then "Enable APIs and Services". Search
> for Gmail and enable.
> 
> Click on the Credentials tab, then "Create Credentials" > "OAuth
> client ID".
> 
> Select what kind of application this is for, and give it a memorable
> name. Fill out all necessary information for the credential (e.g., if
> choosing "Web Application" make sure to add an Authorized Redirect
> URI. See https://developers.google.com/identity/protocols/oauth2 for
> more infomation).
> 
> Back on the credentials screen, click the download icon next to the
> credential you just created to download it as a JSON object.
> 
> Save this file as "client_secret.json" and place it in the root
> directory of your application. (The Gmail class takes in an argument
> for the name of this file if you choose to name it otherwise.)
> 
> The first time you create a new instance of the Gmail class, a browser
> window will open, and you'll be asked to give permissions to the
> application. This will save an access token in a file named
> "gmail-token.json", and only needs to occur once.
> 
> You are now good to go!
> 
> Note about authentication method: I have opted not to use a
> username-password authentication (through imap/smtp), since using
> Google's authorization is both significantly safer and avoids clashing
> with Google's many security measures.

3. Git pull or download Gmail Janitor as a zip.
### Filters.xlsx
To set up filters, fill in the appropriate cells in the excel. **Make sure to create the labels in Gmail as well.**
**Note: Sometimes, some emails you are trying to filter with sender will not be able to be filtered. In this case, try adding the sender with and without the “<>”.  **
