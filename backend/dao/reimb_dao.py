from model.reimbursement import Reimbursement
from utility.db_connection import pool


class ReimbDao:

    def get_all_reimb(self, req_id):

        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT r.id, r.amount, r.submitted, est.status_name, ert.reimb_name, r.description, "
                            "r.receipt, CONCAT(eu.first_name , ' ', eu.last_name) AS employee_name "
                            "FROM ers_reimbursements r "
                            "JOIN ers_status_types est ON r.status_id = est.id "
                            "JOIN ers_reimbursement_types ert ON r.type_id = ert.id "
                            "JOIN ers_users eu ON r.author_id = eu.id "
                            "WHERE r.author_id <> %s AND r.status_id = 1 "
                            "ORDER BY r.submitted", (req_id.get("user_id"),))
                my_list_of_reimbursement_dicts = []
                for reimb in cur:
                    r_dict = {"r_id": reimb[0], "amount": reimb[1], "submitted": reimb[2], "status_name": reimb[3],
                              "r_name": reimb[4], "description": reimb[5], "receipt": reimb[6].decode(),
                              "author": reimb[7]}
                    my_list_of_reimbursement_dicts.append(r_dict)

                return my_list_of_reimbursement_dicts

    def get_reimb_author_id(self, req_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT r.id, r.amount, r.submitted, est.status_name, ert.reimb_name, r.description, "
                            "r.receipt, CONCAT(eu.first_name , ' ', eu.last_name) AS employee_name "
                            "FROM ers_reimbursements r "
                            "JOIN ers_status_types est ON r.status_id = est.id "
                            "JOIN ers_reimbursement_types ert ON r.type_id = ert.id "
                            "JOIN ers_users eu ON r.author_id = eu.id "
                            "WHERE r.author_id = %s ORDER BY r.submitted", (req_id.get("user_id"),))
                my_list_of_reimbursement_dicts = []
                for reimb in cur:
                    r_dict = {"r_id": reimb[0], "amount": reimb[1], "submitted": reimb[2], "status_name": reimb[3],
                              "r_name": reimb[4], "description": reimb[5], "receipt": reimb[6].decode(),
                              "author": reimb[7]}
                    my_list_of_reimbursement_dicts.append(r_dict)

                return my_list_of_reimbursement_dicts

    def get_reimb_author_id_args(self, req_id, args):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT r.id, r.amount, r.submitted, est.status_name, ert.reimb_name, r.description, "
                            "r.receipt, CONCAT(eu.first_name , ' ', eu.last_name) AS employee_name "
                            "FROM ers_reimbursements r "
                            "JOIN ers_status_types est ON r.status_id = est.id "
                            "JOIN ers_reimbursement_types ert ON r.type_id = ert.id "
                            "JOIN ers_users eu ON r.author_id = eu.id "
                            "WHERE r.author_id = %s AND status_id = %s "
                            "ORDER BY r.submitted", (req_id.get("user_id"), args.get('status')))
                my_list_of_reimbursement_dicts = []
                for reimb in cur:
                    r_dict = {"r_id": reimb[0], "amount": reimb[1], "submitted": reimb[2], "status_name": reimb[3],
                              "r_name": reimb[4], "description": reimb[5], "receipt": reimb[6].decode(),
                              "author": reimb[7]}
                    my_list_of_reimbursement_dicts.append(r_dict)

                return my_list_of_reimbursement_dicts

    def get_all_reimb_args(self, req_id, args):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT r.id, r.amount, r.submitted, est.status_name, ert.reimb_name, r.description, "
                            "r.receipt, CONCAT(eu.first_name , ' ', eu.last_name) AS employee_name "
                            "FROM ers_reimbursements r "
                            "JOIN ers_status_types est ON r.status_id = est.id "
                            "JOIN ers_reimbursement_types ert ON r.type_id = ert.id "
                            "JOIN ers_users eu ON r.author_id = eu.id "
                            "WHERE r.author_id <> %s AND r.status_id = %s"
                            "ORDER BY r.submitted", (req_id.get("user_id"), args.get('status')))
                my_list_of_reimbursement_dicts = []
                for reimb in cur:
                    r_dict = {"r_id": reimb[0], "amount": reimb[1], "submitted": reimb[2], "status_name": reimb[3],
                              "r_name": reimb[4], "description": reimb[5], "receipt": reimb[6].decode(),
                              "author": reimb[7]}
                    my_list_of_reimbursement_dicts.append(r_dict)

                return my_list_of_reimbursement_dicts
