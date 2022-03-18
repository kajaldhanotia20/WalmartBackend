# Movie Theatre Seating Challange

### Language Used- Python

#### The algorithm fulfills the below conditions:
1. There are 10*20 seats
2. There is a buffer of 3 seats or one row between different groups/customers
3. We start seating customers from the first row.
4. We try to accomodate as many people as possible.


#### Assumptions made:
1. It is considered safe to seat people from one group together. If there is a different group/different customer, we ensure the distance rule is followed.
2. We assume that the input file has all reservation IDs in order eg- R001, R002, R003 and so on.
3. We cannot make a reservation if the number of seats demanded is greater than the number of seats available, or if the input number is negative, or zero.


#### How do we ensure customer satisfaction?
By ensuring that we accomodate the maximum number of customers possible, we are ensuring that most customers are satisfies that they are being provided a seat. Also, the group members coming together will be seated together, which would add tot he overall experience.

#### How do we ensure customer safety?
We are following the safety protocols as in the requirement. There is a buffer of three seats or one row between different groups and customers which ensures customer safety.

### Steps to reproduce:

