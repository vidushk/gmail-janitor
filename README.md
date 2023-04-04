## Gmail Janitor
### About
Gmail Janitor is a python script that is able to sort mail into filters and can automatically delete them if after a certain period of time, given the script is run routinely.
This is built this using Jeremy Ephron’s [simplegmail][1] python library that makes handling Gmail’s API a lot easier.
It uses Excel as a config to easily edit, add, or change filters.
**Note: This will only work for Gmail, as it uses the Gmail API and not IMAP.**
#### Optimal Usage
The most optimal way of using this script is having it automatically run on a schedule. The idea is that instead of constantly running the script manually, you use a scheduler (cron, launchd, Task Scheduler, etc.) to automatically run in the background so it will constantly be filtering and deleting old mail.
#### Getting Started and Installation
1. Here are the following python libraries you need for the script. 
##### Libraries
	beautifulsoup4==4.12.0
	bs4==0.0.1
	cachetools==5.3.0
	certifi==2022.12.7
	charset-normalizer==3.1.0
	et-xmlfile==1.1.0
	google-api-core==2.11.0
	google-api-python-client==2.83.0
	google-auth==2.17.1
	google-auth-httplib2==0.1.0
	googleapis-common-protos==1.59.0
	httplib2==0.22.0
	idna==3.4
	lxml==4.9.2
	numpy==1.24.2
	oauth2client==4.1.3
	openpyxl==3.1.2
	pandas==1.5.2
	protobuf==4.22.1
	pyasn1==0.4.8
	pyasn1-modules==0.2.8
	pyparsing==3.0.9
	python-dateutil==2.8.2
	pytz==2023.3
	requests==2.28.2
	rsa==4.9
	simplegmail==4.0.4
	six==1.16.0
	soupsieve==2.4
	tzdata==2023.3
	uritemplate==4.1.1
	urllib3==1.26.15

2. First you need to download an OAuth 2.0 Client ID file to get access to the Gmail API. I’ve posted the tutorial from Jeremy Ephron’s readme but you can also access it [here][2].

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
> Click on the Credentials tab, then "Create Credentials" \> "OAuth
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
> Save this file as "client\_secret.json" and place it in the root
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
**Note: Sometimes, some emails you are trying to filter with sender will not be able to be filtered. In this case, try adding the sender with and without the “\<\>”.  **

[1]:	https://github.com/jeremyephron/simplegmail
[2]:	https://github.com/jeremyephron/simplegmail#getting-started