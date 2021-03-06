---
title: Using OpenPGP in Mac OS X
---
# Using OpenPGP in Mac OS X

Greetings, Mac users! To get started, first you need to install `GPG`, and then you need to install and configure an email client. We recommend that you use Thunderbird because it's free and open source. However if you prefer to use proprietary software, you can also use Apple Mail. Instructions for both are below.

## Installing GnuPG

To install `GPG` in Mac OS X, you need to visit [gpgtools.org](https://gpgtools.org/) and download and install the GPG Suite. When you're done downloading the GPG Suite dmg, mount it.

![GPG Suite folder](../images/osx/gpgtools1.png)

Then install the suite of tools.

![GPG Suite installer](../images/osx/gpgtools2.png)

When you install the GPG Suite, you're getting a set of tools. Here's a brief description of what they are:

* **GPGMail** is a plugin for Apple Mail that integrates with GPG.
* **GPG Keychain Access** is a program that helps you manage all of your PGP keys. From here you can generate new keypairs, search key servers for public keys, sign keys, export keys to file, and all sorts of other key management things.
* **GPGServices** and **GPGPreferences** integrate GPG into Mac OS X.
* **MacGPG2** is the Mac OS X port of the base GnuPG software.

When installation is finished, GPG Keychain Access will automatically open, and you will be prompted to generate a new key.

## Generating Your First PGP Key

GPG Keychain Access is prompting you to generate a new keypair. Don't click Generate just yet. Let's look at the options first.

![GPG Keychain Access, generating keypair](../images/osx/gpgtools3.png)

PGP keys contain a name and an email address and some other settings. You're welcome to use a pseudonym. Whatever name you use is what others will see when they encrypt messages that only you can decrypt. It's important to enter the email address that you'll be using with this key to make it simpler for other people to send you encrypted messages. Check the "Upload public key after generation" box if you'd like to make it easier for others to get a copy of your public key so they can send you encrypted messages.

Before generating the key, expand "Advanced options". You can leave the comment blank, and leave the key type "RSA and RSA (default)". But make sure to change the Length field to `4096`. You can also choose an expiration date. When your key expires, you can always extend it's expiration date.

When you're ready, click the "Generate key" button. Before it generates it will prompt you for a passphrase. Type your passphrase and click OK, and re-type it and click OK again.

![GPG Keychain Access, typing passphrase](../images/osx/gpgtools4.png)

Then it will start generating your key. It shouldn't take any more than a couple of minutes to finish.

![GPG Keychain Access, collecting entropy](../images/osx/gpgtools5.png)

When you're done generation your key, you'll see your key listed in GPG Keychain Access. You can double-click on your key to see information about it, including it's "fingerprint" -- a unique way to identify your PGP key.

## Installing and Configuring Thunderbird and Enigmail (recommended)

I recommend that you use Thunderbird and Enigmail for email encryption because it's free and open source. If you prefer Apple Mail, you can skip down to the "Configuring Apple Mail" section.

First, download [Thunderbird](https://www.mozilla.org/thunderbird/) from https://www.mozilla.org/thunderbird/, mount the dmg file, and drag Thunderbird into Applications. When you open it for the first time it will ask if you want to set it as your default email client. Go ahead and click "Set as Default".

![Setting Thunderbird as default email client](../images/osx/thunderbird1.png)

Then you will see the first run wizard. To set up your existing email address, click "Skip this and use my existing email". Then enter your name, email address, and the password to your email account.

![Thunderbird's Account Setup](../images/osx/thunderbird2.png)

If you use popular free email services like Gmail, Thunderbird should be able to automatically detect your email settings when you click Continue. If it doesn't, you may need to manually configure your IMAP and SMTP settings. In this case, Thunderbird auto-detected my email settings:

![Thunderbird's Account Setup, autodetected settings](../images/osx/thunderbird3.png)

After you're done configuring Thunderbird to check your email, click Done. Then click on "Inbox" in the top left to load your emails.

Now that you've installed and configured Thunderbird to work with your email, you need to install [Enigmail](https://www.enigmail.net/home/index.php), the GPG add-on for Thunderbird. In Thunderbird, click the menu icon in the top-right, and choose Add-ons.

![Thunderbird open add-ons](../images/osx/thunderbird4.png)

Search for "enigmail" in the search box in the top right.

![Thunderbird install Enigmail](../images/osx/thunderbird5.png)

Click the Install button next to the Enigmail extension to download and install Enigmail. When it's done, click Restart Now to restart Thunderbird.

The first time you run Thunderbird with Enigmail enabled it opens the OpenPGP Setup Wizard. Click Cancel. We will manually configure Enigmail instead.

![Enigmail wizard](../images/osx/enigmail1.png)

Click the menu button, hover over Preferences, and choose Account Settings.

![Open Account Settings](../images/osx/thunderbird6.png)

Go to the OpenPGP Security tab. Make sure "Enable OpenPGP support (Enigmail) for this identity" is checked. "Use specific OpenPGP key ID" should be selected, and if your key isn't already selected you can click Select Key to select it.

You should also check "Sign non-encrypted message by default", "Sign encrypted messages by default", and "Use PGP/MIME by default", but not "Encrypt messages by default".

It would be ideal to encrypt all the emails you send, but remember that you can only send encrypted email to other people who use PGP, and you need to have their public keys in your keychain as well. Unless everyone you intend to email already uses PGP, it doesn't make sense to always encrypt by default. (You can manually choose to encrypt emails to people who you know use PGP.)

![Account Settings, OpenPGP Security](../images/osx/thunderbird7.png)

Then click OK to save all of the settings. Congratulations, you now have Thunderbird and Enigmail set up! Here are a couple of quick pointers.

You can click the menu button, hover over OpenPGP, and open Key Management to see the PGP key manager that's build-in to Enigmail. It's very similar to GPG Keychain Access, and it's your choice which you use.

When you're composing a new message, there are two icons in the bottom right corner of the window: a pen (digitally sign email) and a key (encrypt email). If the icons are gold it means they are selected, and if they're silver it means they're not selected. Click on them to toggle signing and encrypting the email you're writing.

![Email to Bruno](../images/osx/thunderbird8.png)

You can always sign your emails. Because digitally signing emails requires your secret key, Enigmail will pop up a window asking for your passphrase when you first sign an email. You can only encrypt emails if you have the public key of the person you're emailing. You can try searching for people's public keys from GPG Keychain Access or from Enigmail's Key Management, and you can import keys that people email you as well.

Try sending me an encrypted and signed email next!

## Configuring Apple Mail

When you first open Apple Mail, you'll see a first run wizard that helps you set up your email address. Fill out your name, email address, and your email password and click Create.

![Mail account setup wizard](../images/osx/applemail1.png)

If you use popular free email services like Gmail, Mail should be able to automatically detect your email settings when you click Continue. If it doesn't, you may need to manually configure your IMAP and SMTP settings. In this case, Mail auto-detected my email settings. You can optionally set up Calendar and Chat in this step as well.

![Mail account setup auto-detect](../images/osx/applemail2.png)

When you're composing a new message, there are two icons just beneath the Subject field. There's a padlock (encrypt email) and a star (digitally sign email). If the padlock is closed it means this email will be encrypted, and if the star has a check in it it means this email will be digitally signed.

![Email to Bruno](../images/osx/applemail3.png)

You can always sign your email. Because digitally signing emails requires your secret key, Mail will pop up a window asking for your passphrase when you first sign an email. You can only encrypt emails if you have the public key of the person you're emailing. If the encryption padlock icon is unlocked and greyed out so you can't click on it, this means you first need to import the recipient's public key. To manage your keys while using Mail, use the GPG Keychain Access app.

Try sending me an encrypted and signed email next!
