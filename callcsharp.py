from pydotnet.clr import CLRApi

clr = CLRApi(hostname='127.0.0.1')

obj = clr.new("DataAccessExport.DataAccess")


for i in range(1200000):
    for customer in obj.GetCustomers():
        print("{0} - {1}".format(customer.Name, customer.Id))

clr.close()
