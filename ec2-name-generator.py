import random
import string



def ec2_names_generator():
    allowed_departments = ('Marketing', 'marketing', 'Accounting', 'accounting', 'FinOps', 'Finops', 'finops' )
    department_name = input ("What department do you work for? ")

    if department_name not in allowed_departments:
        print ('Sorry, you are not allowed to use the EC2 Name Generator')
    else:
        num_instances = int(input("Enter the number of EC2 Instance names to generate: "))

        for _ in range(num_instances):
             random_numbers = random.randint(1000,9000)
             instance_name = f"{department_name}-{random_numbers}"
             print (instance_name)



ec2_names_generator ()


