import os
import pyttsx3
import getpass
name = input('Enter you name')
pyttsx3.speak("Hello welcome to my program" + name + "Have a nice day. Please enter your password")
inpass = getpass.getpass('enter your password')
apass = 'lw'

if inpass != apass:
    pyttsx3.speak("Wrong Password. See you soon")
    print("Incorrect password")
    exit()
    
else:
    pyttsx3.speak("Password accepted. please Choose what you want to do from the following list of commands.")


    import os


    print('\t\t\t\t\t\t    AWS Automation     ')
    print()
    print()


    while True:
        print("\t\t\t\t\tPress 1 to Configure AWS Cloud")
        print('\t\t\t\t\tPress 0 to Exit')
        print('\t\t\t\t\t\t => ', end='')
        cmd=input()
        print()

        if cmd=='1':
            print('\t\t\t\t\tPress 1 to Create Key Pair')
            print('\t\t\t\t\tPress 2 to Create Security Group')
            print('\t\t\t\t\tPress 3 to Add Ingress Rules to Existing Security Group')
            print('\t\t\t\t\tPress 4 to Launch Instance on Cloud')
            print('\t\t\t\t\tPress 5 to Create EBS Volume')
            print('\t\t\t\t\tPress 6 to Attach EBS Volume to EC2 Instance')
            print('\t\t\t\t\tPress 7 to Configure WebServer')
            print('\t\t\t\t\tPress 8 to Create Static Partiton and Mount /var/www/html folder on EBS volume')
            print('\t\t\t\t\tPress 9 to Create S3 Bucket')
            print('\t\t\t\t\tPress 10 to put Object inside S3 bucket and make it public accessible')
            print('\t\t\t\t\tPress 11 to remove specific Object from S3 bucket')
            print('\t\t\t\t\tPress 12 to delete Specific S3 Bucket')
            print('\t\t\t\t\tPress 13 to create Cloudfront distribution providing S3 as Origin')
            print('\t\t\t\t\tPress 14 to delete Key Pair')
            print('\t\t\t\t\tPress 15 to Stop EC2-Instances')
            print('\t\t\t\t\tPress 16 to Start Ec2-Instances')
            print('\t\t\t\t\tPress 17 to terminate Ec2-Instances')
            print('\t\t\t\t\tPress 18 to delete Security group')
            print('\t\t\t\t\tPress 19 to Go back to previous menu')
            print('\t\t\t\t\t\t =>  ', end='')
            cmd2=input()
            if cmd2=='1':
                print('Enter key name to create :-  ', end='')
                key_name=input()
                os.system('aws ec2 create-key-pair --key-name {}'.format(key_name))
            elif cmd2=='2':
                print('Enter Security Name :-  ', end='')
                sg_name=input()
                print('Enter VPC Id :-  ', end='')
                vpc_id=input()
                os.system('aws ec2 create-security-group --group-name {} --description "SG Created" --vpc-id {}'.format(sg_name , vpc_id))
            elif cmd2=='3':
                print('Enter Security Group Id :-  ', end='')
                sg_id=input()
                print('Enter IP Protocol ( ie. tcp ) :-  ', end='')
                ip_protocol=input()
                print('Enter Port No :-  ', end='')
                port_no=input()
                cidr=input('Input Ip Ranges :-  ')
                os.system('aws ec2 authorize-security-group-ingress --group-id {} --ip-permissions IpProtocol={},FromPort={},ToPort={},IpRanges=[{}]'.format(sg_id , ip_protocol , port_no , port_no , cidr))
            elif cmd2=='4':
                print('Enter AMI id to Launch Instance :-  ', end='')
                ami=input()
                print('Enter Instance type :-  ', end='')
                itype=input()
                print('Enter Number of Instances to launch :-  ', end='')
                count=input()
                print('Enter Security Group Id to attach to the Instance :-  ', end='')
                sg_id=input()
                print('Enter Key name to attach to ec2 Instance :-  ', end='')
                key=input()
                os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id subnet-0892eab4da13f00a5 --security-group-ids {} --key-name {}'.format(ami , itype , count , sg_id , key))
            elif cmd2=='5':
                print('Enter Availablity Zone to Create EBS Volume :-  ', end='')
                az=input()
                print('Enter Size to create EBS Volume :-  ', end='')
                ebs_size=input()
                os.system('aws ec2 create-volume --availability-zone {} --size {}'.format(az , ebs_size))
            elif cmd2=='6':
                print('Enter EBS Volume ID to Attach to EC2 Instance :-  ', end='')
                ebs_vid=input()
                print('Enter EC2 Instance ID to attach EBS Volume :-  ', end='')
                ec2_id=input()
                os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(ebs_vid , ec2_id))
            elif cmd2=='7':
                print('Enter Ip Address :-  ', end='')
                remote_ip=input()
                print('Enter key name to login inside Ec2 Instance :-  ', end='')
                key=input()
                os.system('ssh -l ec2-user {} -i {}.pem sudo yum install httpd -y'.format(remote_ip , key))
                os.system('ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd'.format(remote_ip , key))
                os.system('ssh -l ec2-user {} -i {}.pem sudo systemctl enable httpd'.format(remote_ip , key))
            elif cmd2=='8':
                print('Enter Ip Address to Remote Login :-  ', end='')
                ip=input()
                print('Enter Keyname :-  ', end='')
                key=input()
                os.system('ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/xvdf'.format(ip , key))
                print('Enter Partition Name to format and  Mount /var/www/html folder  :-   ', end='')
                name=input()
                os.system('ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{}'.format(ip , key , name))
                os.system('ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html'.format(ip , key , name))
            elif cmd2=='9':
                print('Enter S3 bucket name that must be unique :-  ', end='')
                s3_name=input()
                os.system('aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1'.format(s3_name))
            elif cmd2=='10':
                print('Enter Object name to put inside S3 bucket :-  ', end='')
                object_name=input()
                print('Enter S3 Bucket name :-  ', end='')
                s3_name=input()
                os.system('aws s3 cp /root/{} s3://{} --acl public-read'.format(object_name , s3_name))
            elif cmd2=='11':
                print('Enter S3 bucket name :-  ', end='')
                object_name=input()
                print('Enter object name :-  ', end='')
                s3_name=input()
                os.system('aws s3 rm s3://{}/{}'.format(object_name , s3_name))
            elif cmd2=='12':
                print('Enter S3 Bucket name :-  ', end='')
                s3_name=input()
                os.system('aws s3api delete-bucket --bucket {} --region ap-south-1'.format(s3_name))
            elif cmd2=='13':
                print('Enter S3 bucket name :-  ', end='')
                s3_name=input()
                os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(s3_name))
            elif cmd2=='14':
                print('Enter key name to delete :-  ', end='')
                key_name=input()
                os.system('aws ec2 delete-key-pair --key-name {}'.format(key_name))
            elif cmd2=='15':
                print('Enter Instance id to stop Ec2 instances :-  ', end='')
                id=input()
                os.system('aws ec2 stop-instances --instance-ids {}'.format(id))
            elif cmd2=='16':
                print('Enter Instance id to start Ec2 instances :-  ', end='')
                id=input()
                os.system('aws ec2 start-instances --instance-ids {}'.format(id))
            elif cmd2=='17':
                print('Enter Instance id to terminate Ec2 instances :-  ', end='')
                id=input()
                os.system('aws ec2 terminate-instances --instance-ids {}'.format(id))
            elif cmd2=='18':
                sg_id=input('Enter Security group id you want to delete :-  ')
                os.system('aws ec2 delete-security-group --group-id {}'.format(sg_id))
            elif cmd2=='19':
                continue
            else:
                print('Please enter valid command')

        elif cmd=='0':

            print('\n\t\t\t\t\t\t\tPlease Choose Valid Options mention above')
            break
        else:
            print('\n\t\t\t\t\t\t\tPlease Choose Valid Options mention above')
