"""
File Explaining:
    Constant Variables and General Using
"""
DATABASE_INFO = {
    "DATABASE_NAME": "postgres",
    "DATABASE_USER_NAME": "postgres",
    "DATABASE_PASSWORD": "postgresql090816",
    "DATABASE_HOST": "localhost",
}

MAIN_MONITOR = """
********************************************************
                                                        *
                    Welcome to FastBank                 *
                                                        *
                  Please Insert Your Card               *
                                                        *
*********************************************************
"""

CARD_BEING_MESSAGE = "Your card is being identified, please wait."
CLIENT_INFO_QUERY = "SELECT id AS record_id," \
                    "card_id AS card_password," \
                    "balance AS account_balance " \
                    "FROM user_bank_info " \
                    "WHERE card_id = %s "

INCORRECT_PASSWORD_MESSAGE = "Password Incorrect"
CARD_BLOCKED_MESSAGE = "The card password was entered incorrectly 3 times. \n " \
                       "Please contact your bank branch for your card retrieve."
ATM_PROCESS = """
    Main Menu
    Please Press 1 For Show Balance
    Please Press 2 For Withdrawal Money
    Please Press 3 For Deposit Money
    Please Press 4 For Return Card
"""
OPTION_ONE = "1"
OPTION_TWO = "2"
OPTION_THREE = "3"
OPTION_FOUR = "4"

RETURN_CARD_MESSAGE = "We wish you a nice day.\n Please wait whilst your card is Returned..."

SHOW_BALANCE_QUERY = "SELECT balance AS account_balance " \
                     "FROM user_bank_info " \
                     "WHERE id = %s "

UPDATE_MONEY_QUERY = "UPDATE user_bank_info " \
                     "SET balance = %s " \
                     "WHERE id = %s "

SHOW_BALANCE_MESSAGE = "Your Account Balance: {balance}"
ENOUGH_BALANCE_MESSAGE = "Your Account Balance Is Not Enough"
SUCCESS_WITHDRAWAL_MESSAGE = "Withdrawal Success, New Balance: {new_balance} \n Don't Forget Your Card"
SUCCESS_DEPOSIT_MESSAGE = "Deposit Success, New Balance: {new_balance} \n Don't Forget Your Card"
BLANK_SPACE_ENTRY_MESSAGE = "Please Enter a Valid Amount"
WARNING_MESSAGE = "An Error Occurred. Please Try Later"
