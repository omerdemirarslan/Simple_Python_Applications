"""
File Explaining:
    Class and Method File
"""
import logging
import random
import smtplib
import ssl

from configs import *
from cameralyze.helpers.database.postgre import DBHelper

logger = logging.getLogger(__name__)
context = ssl.create_default_context()


class AutomaticTellerMachine:
    """ This Class Starts ATM APP """

    def __init__(self):
        self.selected_option = ""
        self.record_id = 0
        self.account_balance = 0
        self.database_connection = DBHelper(**self.__get_database_connection())
        self.verification_code = str(random.randint(100000, 999999))
        self.context = ssl.create_default_context()

    def __get_database_connection(self) -> dict:
        """
        This Function Connects To PostgreSQL Database
        :return:
        """
        return dict(
            user=DATABASE_INFO["DATABASE_USER_NAME"],
            host=DATABASE_INFO["DATABASE_HOST"],
            password=DATABASE_INFO["DATABASE_PASSWORD"],
            database=DATABASE_INFO["DATABASE_NAME"]
        )

    def get_client_info(self, card_password: int) -> bool:
        """
        This Function Controls Password Accuracy
        :param card_password:
        :return:
        """
        try:
            params = (card_password,)
            self.database_connection.execute(sql=CLIENT_INFO_QUERY, params=params)
            result = self.database_connection.fetchone()

            if str(card_password) == result[1]:
                self.record_id = result[0]
                self.account_balance = result[2]

                return True
            else:
                return False
        except Exception:
            print(WARNING_MESSAGE)

    def __show_balance(self, record_id: int):
        """
        This Function Returns Displays The Show Balance In The Account.
        :param record_id:
        :return:
        """
        try:
            params = (record_id,)
            self.database_connection.execute(sql=SHOW_BALANCE_QUERY, params=params)
            result = self.database_connection.fetchone()

            print(SHOW_BALANCE_MESSAGE.format(
                balance=self.account_balance)
            )

            return result[0]
        except Exception:
            print(WARNING_MESSAGE)

    def __withdrawal_money(self, record_id: int):
        """
        This Function Performs Withdrawal Money.
        :param record_id:
        :return:
        """
        withdrawal = int(input("How Much Would You Like to Withdrawal?:"))

        try:
            if withdrawal:
                new_balance = self.account_balance - withdrawal

                params = (new_balance, record_id,)
                self.database_connection.execute(sql=UPDATE_MONEY_QUERY, params=params)
                self.account_balance = new_balance

                print(SUCCESS_WITHDRAWAL_MESSAGE.format(
                    new_balance=new_balance)
                )
            else:
                print(ENOUGH_BALANCE_MESSAGE)
        except Exception:
            print(WARNING_MESSAGE)

    def __deposit_money(self, record_id: int):
        """
        This Function Performs The Deposit.
        :param record_id:
        :return:
        """
        deposit_money = int(input("How Much Would You Like to Deposit: "))

        try:
            if deposit_money:
                new_balance = self.account_balance + deposit_money

                params = (new_balance, record_id,)
                self.database_connection.execute(sql=UPDATE_MONEY_QUERY, params=params)
                self.account_balance = new_balance

                print(SUCCESS_DEPOSIT_MESSAGE.format(
                    new_balance=new_balance
                ))
            else:
                print(BLANK_SPACE_ENTRY_MESSAGE)
        except Exception:
            print(WARNING_MESSAGE)

    def start_atm_app(self):
        """
        This Function Starts ATM Options
        :return:
        """
        while True:
            print(MAIN_MONITOR)

            i = 0
            while i < 3:
                card_password = input("Please Enter Your 4 Digit Pin: ")
                print(CARD_BEING_MESSAGE, "\n")
                get_client_info = self.get_client_info(card_password=card_password)

                if card_password:
                    if get_client_info:
                        while True:
                            print(ATM_PROCESS)
                            self.selected_option = input("Please Select Your Option: ")

                            if self.selected_option == OPTION_ONE:
                                self.account_balance = self.__show_balance(record_id=self.record_id)
                            elif self.selected_option == OPTION_TWO:
                                self.__withdrawal_money(record_id=self.record_id)
                            elif self.selected_option == OPTION_THREE:
                                self.__deposit_money(record_id=self.record_id)
                            elif self.selected_option == OPTION_FOUR:
                                print(RETURN_CARD_MESSAGE)
                                break
                    elif get_client_info is not True:
                        print(INCORRECT_PASSWORD_MESSAGE)
                        i += 1
                    elif i == 3:
                        print(CARD_BLOCKED_MESSAGE)
                        break
                    else:
                        print(WARNING_MESSAGE)
                else:
                    print(BLANK_SPACE_ENTRY_MESSAGE)


client_1 = AutomaticTellerMachine()
client_1.start_atm_app()
