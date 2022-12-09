import boto3
from time import sleep


""" 
    THIS PYTHON SCRIPT USES AWS S3 API SERVICE TO PERFORM CRUD ON S3 BUCKET.

"""

intro_text = """ 
   ___        ______    ____   _____       _    ____ ___ 
   / \ \      / / ___|  / ___| |___ /      / \  |  _ \_ _|
  / _ \ \ /\ / /\___ \  \___ \   |_ \     / _ \ | |_) | |
 / ___ \ V  V /  ___) |  ___) | ___) |   / ___ \|  __/| |
/_/   \_\_/\_/  |____/  |____(_)____/___/_/   \_\_|  |___|
                                   |_____|
"""


def create_s3_bucket():
    
    #""" This Function Creates AWS S3 Bucket In The Default Region... """

    #INITIALIZE THE S3 CLIENT SERVICE
    client = boto3.client('s3')

    #COLLECT NAME OF BUCKET TO BE CREATED
    bucket_name = str(input("Enter Unique S3 Bucket Name: "))

    #CREATE BUCKET
    response = client.create_bucket(Bucket=bucket_name)

    if True:  
        print("S3 Bucket Created Successfully...")
    

def delete_s3_bucket():

#""" This Function Deletes AWS S3 Bucket In The Default Region... """

    #INITIALIZE THE S3 CLIENT SERVICE
    client = boto3.client('s3')

    #COLLECT NAME OF BUCKET TO BE DELETED
    bucket_name = str(input("Enter S3 Bucket Name to be deleted: "))

    response = client.delete_bucket(Bucket=bucket_name)

    if True:
        print("S3 Bucket Deleted Successfully...")

def uploadFile_s3_bucket():
    
    s3 = boto3.resource('s3')

    #COLLECT NAME OF BUCKET TO BE DELETED
    bucket_name = str(input("Enter S3 Bucket Name for File Upload: "))
    file_name = str(input("Enter S3 File Name to be Uploaded to {}: ".format(bucket_name)))
    new_name = str(input("Enter New Name for S3 Bucket File: "))


    s3.meta.client.upload_file(file_name, bucket_name, new_name)

def downloadFile_s3_bucket():
    
    s3 = boto3.resource('s3')

    #COLLECT NAME OF BUCKET TO BE DELETED
    bucket_name = str(input("Enter S3 Bucket Name for File Download: "))
    obj_name = str(input("Enter S3 Object Name to be Downloaded: "))
    file_name = str(input("Enter file name to save to local repo: "))
    


    s3.meta.client.download_file(bucket_name, obj_name, file_name)
    if True:
        print("FIle Downloaded Successfully...")


def list_s3_buckets():
    
    client = boto3.client('s3')
    
    response = client.list_buckets()
    
    print(response)
    

def listObjects_s3_buckets():
    
    client = boto3.client('s3')
    
    bucket_name = str(input("Enter S3 Bucket Name to List Objects: "))
    response = client.list_objects(Bucket=bucket_name)
    
    print(response)



if __name__ == "__main__":
    print(intro_text)
    create_s3_bucket()
    sleep(1)
    print("==============================================")
    list_s3_buckets()
    # uploadFile_s3_bucket()
    # sleep(1)
    print("==============================================")
    delete_s3_bucket()
    
