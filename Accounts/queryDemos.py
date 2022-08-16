
customers = Customer.objects.all()

firstCustomer = Customer.objects.first()

lastCustomers = Customer.objects.last()

customerbyName = Customer.objects.get(name = 'Peter Piper')

customerbyId = Customer.objects.get(Id = 4)

firstCustomer.order_set.all()

order = Order.objects.first()
parentName = order.customer.name

products = Products.objects.filter(Category="Out Door")

leasttoGreatest = Product.objects.all().order_by('id')
greatesttoLeast = Product.objects.all().order_by('-id')

procuctsFiltered = Product.objects.filter(tags__name="Sports")

ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

#Returns total count for each product orderd
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(Customer)
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()
