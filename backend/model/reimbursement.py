class Reimbursement:
    def __init__(self,
                 reimb_id,
                 amount,
                 submitted,
                 resolved,
                 status_id,
                 type_id,
                 description,
                 receipt,
                 author_id,
                 resolver_id):
        self.__reimb_id = reimb_id
        self.__amount = amount
        self.__submitted = submitted
        self.__resolved = resolved
        self.__status_id = status_id
        self.__type_id = type_id
        self.__description = description
        self.__receipt = receipt
        self.__author_id = author_id
        self.__resolver_id = resolver_id


    def get_reimb_id(self):
        return self.__reimb_id

    def get_type_id(self):
        return self.__type_id

    def get_status_id(self):
        return self.__status_id

    def get_amount(self):
        return self.__amount

    def get_submitted(self):
        return self.__submitted

    def get_resolved(self):
        return self.__resolved

    def get_description(self):
        return self.__description

    def get_receipt(self):
        return self.__receipt

    def get_author_id(self):
        return self.__author_id

    def get_resolver_id(self):
        return self.__resolver_id

    def set_type_id(self, value):
        self.__type_id = value

    def set_reimb_id(self, value):
        self.__reimb_id = value

    def set_status_id(self, value):
        self.__status_id = value

    def set_amount(self, value):
        self.__amount = value

    def set_submitted(self, value):
        self.__submitted = value

    def set_resolved(self, value):
        self.__resolved = value

    def set_description(self, value):
        self.__description = value

    def set_receipt(self, value):
        self.__receipt = value

    def set_author_id(self, value):
        self.__author_id = value

    def set_resolver_id(self, value):
        self.__resolver_id = value

    def to_dict(self):
        return {
            'reimb_id': self.get_reimb_id(),
            'amount': self.get_amount(),
            'submitted': self.get_submitted(),
            'resolved': self.get_resolved(),
            'status_id': self.get_status_id(),
            'type_id': self.get_type_id(),
            'description': self.get_description(),
            'receipt': self.get_receipt().decode(),
            'author_id': self.get_author_id(),
            'resolver_id': self.get_resolver_id()
        }
