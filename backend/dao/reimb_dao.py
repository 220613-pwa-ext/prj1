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
                            "WHERE r.author_id <> %s "
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

    def update_reimb_by_reimb_id(self, reimb_id, status):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE ers_reimbursements SET status_id = %s, resolved = Now() WHERE id = %s RETURNING *"
                            , (status, reimb_id))
                reimb = cur.fetchone()
                if reimb:
                    return Reimbursement(reimb[0], reimb[1], reimb[2], reimb[3], reimb[4], reimb[5], reimb[6],
                                         reimb[7], reimb[8], reimb[9])
                else:
                    return None

    def get_reimb_by_reimb_id(self, reimb_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_reimbursements WHERE id = %s;", (reimb_id,))
                reimb = cur.fetchone()
                if reimb:
                    return Reimbursement(reimb[0], reimb[1], reimb[2], reimb[3], reimb[4], reimb[5], reimb[6],
                                         reimb[7], reimb[8], reimb[9])
                else:
                    return None