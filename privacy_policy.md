# Privacy Policy

**Effective Date:** 9 May 2026

## 1. Introduction

Welcome to **FareKeep**. This privacy policy explains how we collect, use, store, and protect your personal and tax-related information when you use our mobile application (the "App"). FareKeep is a tax record-keeping and logbook management tool designed primarily for users in **Australia**, including ride-source drivers and sole traders, as well as foreign individuals who pay tax or GST to the Australian Taxation Office (ATO).

By downloading, installing, or using the App, you agree to the collection and use of information in accordance with this policy. We are committed to ensuring that your privacy is protected and that your data is handled strictly in compliance with the Australian Privacy Act 1988, relevant ATO record-keeping guidelines, and the applicable App Store and Google Play Store policies.

*Disclaimer: FareKeep is a record-keeping tool only. It does not provide tax advice. While the App is built to assist in maintaining records that are compatible with ATO rules and regulations, the accuracy of the data entered and the final tax lodgement remains the sole responsibility of the user. Consult a registered tax agent for tax advice. For more information on ATO compliance, please visit the [official ATO website](https://www.ato.gov.au).*

## 2. Information We Collect

We collect information to provide better services to our users. The type of information we gather depends on your use of the App:

### 2.1 Information You Provide

- **Business Profile Information:** Business name, Australian Business Number (ABN), GST registration status, and optional business logo image.
- **Vehicle Information:** Vehicle registration, make, model, year, type, engine capacity, and descriptive notes.
- **Logbook & Trip Data:** Logbook start/end dates, odometer readings, logbook mode (open-ended or fixed-period), individual trip records including dates, distances, business/personal classification, and trip purpose descriptions.
- **Transaction Data:** Income and expense records including dates, amounts, descriptions, expense categories, payment methods, GST amounts, claimable percentages, and claimable method (manual or automatic based on logbook data).
- **Receipt & Document Attachments:** Images captured via the device camera or native document scanner, photos selected from the device gallery, and PDF files picked from device storage. These attachments are compressed and stored locally on your device.
- **Google Account Information:** When you sign in via Google Sign-In for the backup feature, we access your Google account name and email address solely to authenticate with Google Drive.

### 2.2 App Preferences & Settings

- **Theme & Display Preferences:** App theme mode (light, dark, or system), colour palette selection, and BAS/GST lodgement reminder frequency.
- **Notification Preferences:** Your chosen notification schedule for GST/BAS lodgement reminders.

These preferences are stored locally on your device using SharedPreferences and are never transmitted to any external server.

### 2.3 Automatically Collected Data

- **ATO Tax Configuration Data:** The App uses Firebase Remote Config to fetch current ATO-related rates (GST rate, cents-per-kilometre rate, maximum kilometre cap) based on the relevant Australian Financial Year. This service communicates with Firebase servers to ensure tax calculation parameters remain current. No personally identifiable information is sent during this process.
- **App Version Information:** The App checks for available updates via the Apple App Store or Google Play Store to ensure you are running the latest version. No personal data is transmitted during this check.

## 3. How We Use Your Data

We use the information we collect strictly to operate, maintain, and provide the features of the App, including:

- **Tax & ATO Compliance Record-Keeping:** To maintain accurate records of income, expenses, trip distances, and logbooks that align with Australian Taxation Office (ATO) standards for ride-sourcing, sole traders, and GST-registered businesses.
- **GST & Tax Report Generation:** To generate detailed GST reports (PDF), GST spreadsheets (Excel), and annual tax summary reports based on your recorded transactions, aligned with Australian Financial Year quarters (Q1–Q4).
- **Logbook-Based Expense Calculations:** To automatically calculate business-use percentages for vehicle expenses based on linked logbook trip data, with per-vehicle mileage capping as required by ATO rules.
- **Multi-Business Management:** To allow you to maintain separate business profiles, each with their own vehicles, transactions, logbooks, and master data.
- **Backup & Restore:** To securely back up your complete database and attachments to your personal Google Drive account (in a dedicated `FareKeepApp/Backups` folder), so you never lose your tax records.
- **Financial Year Archiving:** To archive completed financial years, including exporting transaction data to CSV, bundling receipt attachments and generated reports into a ZIP archive, and optionally uploading the archive to your Google Drive (in a dedicated `FareKeepApp/Archives` folder). You may also delete local attachment copies after archiving to free device storage.
- **Receipt & Document Management:** To capture, scan, crop, compress, and store receipt images and PDF documents as evidence for your tax records.
- **GST/BAS Lodgement Reminders:** To schedule local notifications on your device reminding you of upcoming BAS due dates based on your chosen lodgement frequency (quarterly, monthly, or yearly).
- **Sharing & Export:** To allow you to share generated reports and receipt attachments via your device's native sharing functionality.

## 4. Device Permissions

The App requests the following device permissions, each for a specific purpose:

| Permission | Platform | Purpose |
|---|---|---|
| **Camera** | iOS, Android | Capturing receipt photos and scanning documents using the built-in document scanner with automatic edge detection. |
| **Photo Library / Gallery** | iOS | Selecting existing receipt images from your photo library to attach to transactions. |
| **Notifications** | iOS, Android | Scheduling local GST/BAS lodgement reminder notifications. You can disable these at any time from the App's settings. |
| **Exact Alarm / Boot Completed** | Android | Ensuring scheduled GST reminder notifications are delivered at the correct time, including after device restarts. |

All permissions are requested at the point of use with a clear explanation. You may revoke any permission at any time through your device's system settings.

## 5. Third-Party Services

Our App integrates the following third-party services. Each provider has their own privacy policy governing how they handle data:

- **Google Sign-In:** Used for secure user authentication when connecting to Google Drive for backup and archive features. [Google Privacy Policy](https://policies.google.com/privacy).
- **Google Drive API:** Used exclusively for the App's user-initiated data backup and financial year archive features. The App only accesses the specific `FareKeepApp` folder and its sub-folders (`Backups`, `Archives`) that it creates in your personal Google Drive. We use the `drive.file` scope, which restricts access to files created by the App only. [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).
- **Firebase Remote Config:** Used to fetch current ATO tax parameters (GST rates, cents-per-km rates, mileage caps) so that tax calculations remain accurate across financial years without requiring an app update. No personal data is collected or transmitted. [Firebase Privacy Policy](https://firebase.google.com/support/privacy).
- **Google Fonts:** The App may download font files from Google's servers to render text. No personal data is sent. [Google Fonts Privacy](https://developers.google.com/fonts/faq/privacy).
- **Google Play Services / Apple App Store:** Used for app distribution and update availability checks. [Google Play Terms](https://play.google.com/about/play-terms/) | [Apple Privacy Policy](https://www.apple.com/legal/privacy/).

## 6. Data Storage & Retention

- **Local Device Storage:** All sensitive tax data, logbook records, business profiles, and receipt attachments are stored locally on your device in a secure SQLite database and the app's private document directory. This data never leaves your device unless you explicitly initiate a backup or archive upload.
- **App Preferences:** Non-sensitive settings (theme mode, colour selection, notification frequency, onboarding state) are stored locally using SharedPreferences.
- **Cloud Storage (User-Initiated Only):** If you choose to use the backup or archive feature, your data is compressed into a ZIP file and uploaded directly to your personal Google Drive. **We do not operate any external servers and do not store, process, or have access to your data on any server we control.** The data flows directly between your device and your personal Google Drive account.
- **Generated Reports:** PDF and Excel reports are generated and stored locally on your device. They are only shared externally if you explicitly choose to share or export them.

## 7. Data Deletion

You have full control over your data at all times:

- **Delete Individual Records:** Remove specific transactions, trips, logbook entries, or attachments through the App's interface.
- **Reset Business Data:** Clear all transactions, trips, and business-specific master data for a specific business profile via **Settings → Advanced Settings → Reset Business Data**.
- **Delete Business Profile:** Permanently remove an entire business profile and all its associated data via **Settings → Advanced Settings → Delete Business Profile**.
- **Delete Backup Files:** Remove backup files from your Google Drive directly through the App's **Backup & Restore** screen.
- **Delete Archive Files:** Remove archived financial year data from Google Drive through the App's **Archives** screen.
- **Uninstall the App:** Removing the App from your device will delete all locally stored data, including the database and all receipt attachments.

## 8. Data Security

We value your trust in providing us your information and implement the following security measures:

- **Local-First Architecture:** Your data is stored primarily on your device and is never transmitted to our servers (we do not operate any data servers).
- **Secure Communication:** All cloud communication (Google Sign-In, Google Drive API, Firebase Remote Config) uses industry-standard HTTPS/TLS encryption and OAuth 2.0 authentication.
- **Image Compression:** Receipt images are compressed to WebP format and PDFs are optimised before storage, reducing the sensitive data footprint on your device.
- **Scoped API Access:** Google Drive access uses the restricted `drive.file` scope, limiting the App's access to only the files and folders it creates.

However, please remember that no method of electronic storage or transmission over the internet is 100% secure. We encourage you to keep your device and Google account secured with strong passwords and biometric authentication.

## 9. Children's Privacy

FareKeep is a business and tax record-keeping tool designed for use by adults. We do not knowingly collect personal information from children under the age of 18. If you are a parent or guardian and believe your child has provided information through the App, please contact us so we can take appropriate action.

## 10. Changes to This Privacy Policy

We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "Effective Date" at the top. For substantial changes to our data handling practices, we may also notify you via in-app alerts or forced update prompts. You are advised to review this Privacy Policy periodically.

## 11. Contact Us

If you have any questions, suggestions, or concerns regarding your privacy, our data collection practices, or specific ATO compliance features within the App, please do not hesitate to contact us at:

**Email:** [amila.champlnx@gmail.com](mailto:amila.champlnx@gmail.com)
