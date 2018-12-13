#!/usr/bin/env python3

from donor_models import DonorCollection


class MailroomCli():
    """
    MailroomCli: command line interface that interacts with DonorCollection
    """

    _exit_mail = False
    _dc = None

    def __init__(self):
        self._dc = DonorCollection()

    def exit_mail(self):
        self._exit_mail = True

    def print_menu(self):
        print("Object Oriented Mailroom Tasks:\n")
        print("[1] Send a Thank you to a single donor")
        print("[2] Send a Thank you to all donors (to stdout)")
        print("[3] Create a report")
        print("[4] Send letters to all donors")
        print("[9] Exit Mailroom\n")

    def prompt_donor(self):
        donor_name = input("Enter donor name ('list' for all donors) : ")
        if donor_name == 'list':
            namelist = self._dc.list_names()
            if len(namelist) > 1:
                print(namelist)
            donor_name = input("Enter donor name : ")
        while True:
            try:
                donor_amt = input("Enter donation value: ")
                try:
                    donor_amt = float(donor_amt)
                    break
                except ValueError:
                    print("Please enter a numeric donation value")
            except SyntaxError:
                print("Please enter a valid donation value")

        try:
            self._dc.add_new_donor(donor_name)
            self._dc.add_donation(donor_name, donor_amt)
        except ValueError:
            self._dc.add_donation(donor_name, donor_amt)

        return self._dc.get_donor(donor_name)

    def send_thankyou_single_donor_task(self):
        donor = self.prompt_donor()
        print(donor.generate_thankyou())

    def send_thankyou_multiple_donors_task(self):
        self._dc.generate_thankyou_all()

    def send_thankyou_multiple_donors_to_file_task(self):
        filenames = self._dc.generate_thankyou_all_to_file()
        return filenames

    def create_report_task(self):
        print(self._dc.generate_report_all())

    _task_dict = {
        9: exit_mail,
        4: send_thankyou_multiple_donors_to_file_task,
        3: create_report_task,
        2: send_thankyou_multiple_donors_task,
        1: send_thankyou_single_donor_task
        }

    def do_tasks(self):
        while not self._exit_mail:
            self.print_menu()
            response = input("Enter Mailroom Option: ")

            # Validate response
            try:
                response = int(response)
            except ValueError:
                print("Enter a number between 1-9")
                continue

            # Dispatch task based on response
            try:
                self._task_dict[response](self)
            except KeyError:
                print("Please enter a correct task number")
                continue


def main():
    cli = MailroomCli()
    cli.do_tasks()

if __name__ == "__main__":
    main()
