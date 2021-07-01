"""
File Explaining:
    Class and Method File
"""
import logging
import random
import smtplib
import ssl

from cameralyze.helpers.database.postgre import DBHelper
from configs import *

logger = logging.getLogger(__name__)


class CreatUserProfile:
    """ This Class Creates New User Objects """

    def __init__(self):
        self.create_name = input("Your Name: ")
        self.create_surname = input("Your Surname: ")
        self.email = input("Your Email Address: ")
        self.password = " "
        self.user_info = [self.create_name, self.create_surname, self.email, self.password]
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

    def __send_verification_code(self, user_mail: str, message: str):
        """
        This Function Sends Verification Code For New User Record
        :param user_mail:
        :param message:
        :return:
        """
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_SSL_PORT)
            server.ehlo()
            server.starttls(context=self.context)
            server.login(SENDER_EMAIL_ADDRESS, PASSWORD_SENDER_EMAIL)
            server.sendmail(SENDER_EMAIL_ADDRESS, user_mail, message)

            return SUCCESSFUL_VERIFICATION_CODE_MASSAGE
        except Exception:
            return UNSUCCESSFUL_VERIFICATION_CODE_MASSAGE
        finally:
            server.quit()

    def get_control_user_info(self) -> bool:
        """
        This Function Checks The Correctness Of User Information.
        :return:
        """
        while True:
            create_password = input("Create Password: ")
            confirm_password = input("Confirm Password: ")

            self.user_info.extend([create_password, confirm_password])

            if all(self.user_info):
                if create_password != confirm_password:
                    print(INCOMPATIBLE_PASSWORD)
                else:
                    self.password = create_password

                    self.__send_verification_code(
                        user_mail=self.email,
                        message=VERIFICATION_MESSAGE.format(
                            name=self.create_name,
                            surname=self.create_surname,
                            verification_code=self.verification_code
                        )
                    )

                    while True:
                        entered_verification_code = input("Please Enter The Code Sent To Your E-mail Address: ")

                        if entered_verification_code != self.verification_code:
                            print(INCOMPATIBLE_VERIFICATION_CODE)
                        else:
                            return True
            else:
                print(WARNING_EMPTY_INPUT)
                CreatUserProfile()

    def create_new_user(self) -> str:
        """
        This Function Create New User In User Table
        :return:
        """
        if self.get_control_user_info:
            try:
                params = tuple(self.user_info[:4])
                self.database_connection.execute(USERS_TABLE_INSERT_QUERY, params)
                self.database_connection.fetchone()

                return SUCCESSFUL_USER_CREATION
            except Exception:
                print(GENERAL_WARNING)
        else:
            return UNSUCCESSFUL_USER_CREATION


new_user_1 = CreatUserProfile()
new_user_1.get_control_user_info()
new_user_1.create_new_user()

