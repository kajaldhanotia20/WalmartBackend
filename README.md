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
1. Download the repository folder and unzip it.
2. Make sure python 3 is installed in your system.
3. Make sure your input file is inside the inputs folder in the repo directory.
4. Goto command line and cd to the location where repo folder is present. Then run the file main.py using command ``` python main.py <input file location> ```. If you do not change the structire, the input file location is /inputs/input.txt.
5. You can see that the output will be returned to the file output.txt
6. To run the test cases, run the tests.py file using the command ``` python tests.py ``` and you will see the output on the commandline window.

