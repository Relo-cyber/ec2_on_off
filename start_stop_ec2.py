import boto3
import sys
import os
import time
def get_ec2_con_for_give_region(my_region):
		    ec2_con_re=boto3.resource('ec2',region_name=myregion)
		    return ec2_con_re		
def list_instances_on_my_region(ec2_con_re):
	for each in ec2_con_re.instances.all():
		print each.id
def get_instant_state(ec2_con_re,in_id):
		for each in ec2_con_re.instances.filter(Filters=[{'Name' : 'instance-id',"values":[in_id]}]):
            pr_st=each.state['Name']
        return pr_st

def start_instance(ec2_con_re,in_id):
        pr_st=get_instant_state(ec2_con_re,in_id):
        if pr_st=="running":
            print"instance already running"
        else: 
            for each in ec2_con_re.instance.filter(Filters=[{'Name':'instance_id', "Values":[in_id]}]):
                each.start()
                print"starting instance... please wait"
                each.wait_until_running()
                print"running"
		return
def Thank_you():
        print"\n\n*******Script executed successfully*******"
        return None
def stop_instance(ec2_con_re,in_id):
        pr_st=get_instant_state(ec2_con_re,in_id):
        if pr_st=="stopped":
            print "already stopped"
        else:
            for each in ec2_con_re.instance.filter(Filters=[{'Name':'instance-id',"values":[in_id]}]):
                each.stop()
                print"stopping..., please wait"
                each.wait_until_stopped()
                print "now it stopped"
def welcome():
        print"This script is to help you start or stop ec2 instances based on the region and instance id"
        print"Time is Money"
        time.sleep(3)
def main():
        welcome()
        my_region=raw_input("Enter Region Name:")
        print "connecting..., please wait"
        ec2_con_re=get_ec2_con_for_give_region(my_region)
        print"listing all instances ids"
        list_instances_on_my_region(ec2_con_re)
        in_id=raw_input("Enter instance id:")
        start_stop=raw_input("start or stop")
        while True:
                if start_stop not in ["start","stop"]:
                        start_stop=raw_input("only start or stop command:")
                        continue
                else:
                        break
        if start_stop=="start":
                start_instance(ec2_con_re,in_id)
        else:
                stop_instance(ec2_con_re,in_id)
        Thank_you()
if___name___=='___main___':
    os.system('cls')
    main()
