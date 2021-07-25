
#Модель :

from enum import Enum


class Newsletter(Enum):
    yourStoreName = 1
    testStore = 2


class Gender:
    male = 1
    female = 2


class ManagerVendor(Enum):
    notaVendor = 1
    vendor_1 = 2
    vendor_2 = 3


class CustomerRole(Enum):
    guests = 1
    administrators = 2
    forum_Moderators = 3
    vendors = 4
    registered = 5


class UserData:

    firstName = str
    secondName = str
    gender = Gender
    dateofBirth = str
    newsletter = Newsletter
    managerofVendor = ManagerVendor
    adminComment = str
    email = str
    password = str
    companyName = str
    customerRole = CustomerRole

