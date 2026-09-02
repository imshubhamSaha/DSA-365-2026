# Unoccupied Computers

class Solution:
    
    def solve(self, n, s):
        m = len(s)
        if (m // 2) < n :
            return 0
        assigned_customers = [False] * 26
        not_assigned_customer = [False] * 26
        assigned_system = 0
        not_assigned_cust_cnt = 0
        for customer in s :
            cust_id = ord(customer) - ord('A')
            if assigned_customers[cust_id] :
                assigned_customers[cust_id] = False
                assigned_system -= 1
            elif assigned_system == n :
                if not not_assigned_customer[cust_id] :
                    not_assigned_cust_cnt += 1
                not_assigned_customer[cust_id] = True
            elif  not not_assigned_customer[cust_id] :
                assigned_customers[cust_id] = True
                assigned_system += 1
        
        return not_assigned_cust_cnt
        
