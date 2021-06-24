ticket = 37750;
def ticket_cal(adults,children):

        cost = ticket*adults+(ticket/3)*children
        with_tax_cost = cost + (cost*0.07)
        final_cost = with_tax_cost - (with_tax_cost*0.1)
        return final_cost
a = int(input("Enter the number of Adults "))
c = int(input("Enter the number of childrens"))

x = ticket_cal(a,c)
print("Total Ticket Cost:",x)