from faker import Faker
from datetime import datetime
fake = Faker()


def measure_function_execution_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        execution_time = (datetime.now() - start).microseconds / 1000000
        print(f"Function executed in {execution_time} seconds")
        return res
    return wrapper

class Contact:
    def __init__(self, name: str, surname: str, email: str):
        self.name = name
        self.surname = surname
        self.email = email


    @property
    def label_length(self) -> int:
        return len(self.name) + len(self.surname)

    

class BaseContact(Contact):

    def __init__(
            self, name: str, surname: str,
            personal_phone: int, email: str
    ):

        super(BaseContact(Contact), self).__init__(name, surname, email)
        self.personal_phone = personal_phone


    def contact(self) -> None:
        print(f"Я набираю {self.personal_phone} і телефоную {self.name} {self.surname} ")


class BusinessContact(Contact):
    def __init__(
            self, name: str, surname: str,
            personal_phone: int, email: str,
            job_title: str, company_name: str, business_phone: int
    ):
        super(BusinessContact, self).__init__(name, surname, email)
        self.job_title = job_title
        self.company_name = company_name
        self.business_phone = business_phone

    def contact(self) -> None:
        print(f"Я набираю {self.business_phone} і телефоную {self.name} {self.surname} ")


@measure_function_execution_time
def create_contacts(contact_type, create_amount):
    result_contacts = []
    sort = create_contacts(contact_type, create_amount)
    for i in sort :
        i.contact()
        print(sort)
    for _ in range(create_amount):
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()
        if contact_type is BaseContact:
            contact = contact_type(first_name, last_name, phone, email)
            result_contacts.append(contact)
        elif contact_type is BusinessContact:
            job_title = fake.job()
            company_name = fake.company()
            business_phone = fake.phone_number()
            business_contact = contact_type(
                first_name, last_name, phone,
                email, job_title, company_name, business_phone
            )
            result_contacts.append(business_contact)
        else:
            raise ValueError(f'Expected to receive BaseContact or BusinessContact classes, got {contact_type}')
    return result_contacts

if __name__ == '__main__':

    print("Створюємо 1000 BaseContact")
    contacts = create_contacts(BaseContact, 1000)

    print("Створюємо 1000 BusinessContact")
    create_contacts(BusinessContact, 1000)
