# Email-OTP-verification-System

The Email OTP Verification System is a simple Python-based command-line project that allows users to verify their identity via a One-Time Password (OTP) sent to their email.
This system demonstrates the concepts of OTP generation, email delivery using SMTP, and time-based validation.

# Features

Generate a 6-digit random OTP

Send OTP to the user via email using SMTP (Gmail)

Validate OTP with time-based expiry (default 60 seconds)

Command-line interface for simplicity

Error handling for invalid OTPs and email delivery issues



# Technologies Used

Python

smtplib (built-in Python library for sending emails)

EmailMessage class for composing emails

random module for OTP generation

time module for OTP expiration


# Code Flow

Generate OTP – random 6-digit code

Ask for user email – input from command line

Send OTP – via SMTP using Gmail

Ask user to enter OTP – input from command line

Verify OTP – check correctness and expiry

Display result – success or failure



