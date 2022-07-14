from model.reimbursement import Reimbursement
from utility.db_connection import pool


class ReimbDao:

    def get_all_reimb_by_employee_id(self, emp_id):

        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_reimbursements WHERE author_id = %s", (emp_id,))
                my_list_of_reimbursement_objs = []
                for reimb in cur:
                    reimb_id = reimb[0]
                    amount = reimb[1]
                    submitted = reimb[2]
                    resolved = reimb[3]
                    status_id = reimb[4]
                    type_id = reimb[5]
                    description = reimb[6]
                    receipt = reimb[7]
                    author_id = reimb[8]
                    resolver_id = reimb[9]

                    my_list_of_reimbursement_objs.append(Reimbursement(reimb_id,
                                                                       amount,
                                                                       submitted,
                                                                       resolved,
                                                                       status_id,
                                                                       type_id,
                                                                       description,
                                                                       receipt,
                                                                       author_id,
                                                                       resolver_id))

                return my_list_of_reimbursement_objs
