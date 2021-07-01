"""
File Explaining:
    Constant Variables and General Using
"""

DATABASE_INFO = {
    "DATABASE_NAME": "postgres",
    "DATABASE_USER_NAME": "postgres",
    "DATABASE_PASSWORD": "*** Your Database Password ***",
    "DATABASE_HOST": "localhost",
}

SMTP_SERVER = "smtp.gmail.com"
SMTP_SSL_PORT = 587
SENDER_EMAIL_ADDRESS = "*** Your E-mail ***"
PASSWORD_SENDER_EMAIL = "*** Your E-mail Password **"

VERIFICATION_MESSAGE = "Hello Dear {name} {surname} \n *** WELCOME TO YOUR NEW FAMILY *** \n " \
          "You Can Use This Code For Creation Profile \n Verification Code: {verification_code} \n " \
          "Don't Share This Message"

SUCCESSFUL_VERIFICATION_CODE_MASSAGE = "Your Verification Code Has Been Sent To Your Email Address."
UNSUCCESSFUL_VERIFICATION_CODE_MASSAGE = "Generate An Error Sending Verification Code."

WARNING_EMPTY_INPUT = "There Should Be No Blank Spaces In The User Information.Please Try Again."
INCOMPATIBLE_PASSWORD = "Your Password and Confirm Password Must Be Same!"
INCOMPATIBLE_VERIFICATION_CODE = "Your Entered Varification Code Is Not Same."

SUCCESSFUL_USER_CREATION = "Your Registration Has Been Successfully Done."
UNSUCCESSFUL_USER_CREATION = "An Error Occurred In Your Registration Process. Please Try Again."

GENERAL_WARNING = "An Error Occurred"

USERS_TABLE_INSERT_QUERY = "INSERT INTO users " \
                           "(name, surname, email, password) " \
                           "VALUES (%s, %s, %s, %s)"
