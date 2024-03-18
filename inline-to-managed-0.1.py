import json
import boto3
from botocore.exceptions import ClientError

# Reading role names from a file
with open('roles.txt', 'r') as file:
    roles = file.read().splitlines()

account_id = '000999999999'
client = boto3.client("iam")
resource = boto3.resource('iam')

# File to record modified roles
with open('modified_roles.txt', 'w') as modified_roles_file:

    for role_name in roles:
        print(f"Processing role: {role_name}\n")
        try:
            response = client.list_role_policies(RoleName=role_name)
        except ClientError as error:
            print(f"Could not list policies for the role {role_name}: {error}\n")
            continue

        for policy_name in response["PolicyNames"]:
            try:
                response = client.get_role_policy(RoleName=role_name, PolicyName=policy_name)
                policy_document = json.dumps(response["PolicyDocument"])
                print(f"Policy= {policy_name}\nFor role= {role_name}\nFound...\n")

                # Simulating policy creation
                response = client.create_policy(
                    PolicyName=policy_name, PolicyDocument=policy_document
                )
                policy_arn = f'arn:aws:iam::{account_id}:policy/{policy_name}'
                print(f"Creating policy {policy_name} for {role_name}.\n")
                print(f"Arn: {policy_arn}\n")

                # Simulating associating the policy to the role
                role = resource.Role(role_name)
                print(f"Associating policy {policy_name} with {role_name}.\n")
                role.attach_policy(PolicyArn=policy_arn)
                #Simulating deletion of the inline policy
                client.delete_role_policy(
                    RoleName=role_name,
                    PolicyName=policy_name
                )
                print(f"Policy {policy_name} converted to managed for the role {role_name}.\n")
                modified_roles_file.write(f"{role_name}\n")

            except ClientError as error:
                if error.response['Error']['Code'] == 'EntityAlreadyExists':
                    print(f"The policy {policy_name} for the role {role_name} already exists.\n")
                else:
                    print(f"Error processing {policy_name} in {role_name}: {error}\n")

print("Process completed. See modified_roles.txt for the list of modified roles.")
