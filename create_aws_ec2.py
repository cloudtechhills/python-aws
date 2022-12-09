import boto3

#CreatedBy TechN3rd

"""     
        TO-DO LIST:
        THIS FUNCTIONS CREATES AN AWS EC2 INSTANCE USING PYTHON BOTO3 LIBRARY FOR AWS SERVICES
"""


title_text = """
                     _         _____ ____     ____  
  ___ _ __ ___  __ _| |_ ___  | ____/ ___|   |___ \ 
 / __| '__/ _ \/ _` | __/ _ \ |  _|| |   _____ __) |
| (__| | |  __/ (_| | ||  __/ | |__| |__|_____/ __/
 \___|_|  \___|\__,_|\__\___| |_____\____|   |_____|

"""

    
def create_ec2_instance():
    try:
        print("Creating EC2 Instance...")
        
        #INITIALIZE THE EC2 CLIENT INSTANCE
        ec2_client = boto3.client('ec2')

        #USE THE RUN_INSTANCE METHOD FROM THE EC2_CLIENT INSTANCE TO CREATE AWS EC2 INSTANCE
        ec2_client.run_instances(
            ImageId='ENTER YOUR EC2 AMI ID',
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            KeyName='Enter Your Key-Pair')
        if True: 
            print("EC2 created successfully...")
        
    except Exception as e:
        print("{} Error was encountered...".format(e))

if __name__ == "__main__":
    print(title_text)
    print()
    create_ec2_instance()

