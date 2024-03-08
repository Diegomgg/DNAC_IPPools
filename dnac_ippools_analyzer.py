#!python3
import radkit_client
import radkit_common
from radkit_client.sync.helpers import CiscoDNACenter as DNAC
from radkit_client.sync.helpers import SWIMSException
from radkit_client.sync.login import sso_login
import radkit_cli
import ipverifications
import argparse
import time

version = '1.0.1'

from radkit_client.sync import (
    create_context
)
'''
def startup():
    email = "digranad@cisco.com"
    domain = "PROD"
    string = "vh2a-6ow9-8tqk"
    #service = radkit_cli.radkit_login(email,domain,string)
    client = sso_login(identity=email, domain=domain)
    #service = client.service(string).wait()
    with sso_login() as client:
        service = client.service(string).wait()
        print(service.inventory)
        return (service)   
''' 
    

def ippool_analyzer(dnac_name, service):

    dnac_Object = DNAC(service.inventory[dnac_name])
    
    session = dnac_Object.admin_terminal().wait()

    curl_token = f"TOKEN=$(curl -k -s -X POST -u digranad https://kong-frontend.maglev-system.svc.cluster.local/api/system/v1/identitymgmt/token | jq -r .Token)"
    #curl_pools = f"curl -vT /DNA_Analyzer/dna_analyzer_logs/* -u {case_number} https://cxd.cisco.com/home/"
    session.write(curl_token.encode())
    print(session.readline().decode("utf-8"))
    session.write(b"Merch123\n")
    
    token_opt = radkit_cli.get_any_single_output(dnac_name,curl_token,service)
    print(token_opt)

    #session.write(curl_commend.encode())
    #print(f"Uploading analyzer logs to case with SR {case_number}")

    #curl_commend = f"curl -vT /DNA_Analyzer/dna_analyzer_reports/* -u {case_number} https://cxd.cisco.com/home/"
    #session.write(curl_commend.encode())
    #session.write(token.encode())

    token_cmd = "echo $TOKEN"
    nconfst_opt = radkit_cli.get_any_single_output(dnac_name,token_cmd,service)
    print(nconfst_opt)

    session.close()

    return



# ensures that when we import thsi file which we should for other projects we can simply use it without commenting or deleting rest of teh code and still use the methods defined.
if __name__ == '__main__':
    with create_context():
        global service

        email = "digranad@cisco.com"
        domain = "PROD"
        string = "vh2a-6ow9-8tqk"
        #service = radkit_cli.radkit_login(email,domain,string)
        client = sso_login(identity=email, domain=domain)
        #service = client.service(string).wait()
        with sso_login() as client:
            service = client.service(string).wait()
            print(service.inventory)

            client = service.client

            print("Cliente")
            print(client)
            
            output =  service.inventory
            
            print("Please add the Cisco DNA Center IP Address")
            
            dnac_ip = ipverifications.ip_validator_input("Cisco DNA Center IP: ")

            dnac_name = radkit_cli.find_device(service, dnac_ip)

            print(dnac_name)

            print(f"Status is {client.status} for '{client.identity}' on domain '{client.domain}' using {client.authentication_method}")

            ippool_analyzer(dnac_name,service)

