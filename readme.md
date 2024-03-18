# **README for AWS IAM Role Policy Converter Script**

## **Overview**

This Python script is designed to automate the process of converting inline policies attached to IAM roles into managed policies in AWS (Amazon Web Services). The script reads a list of IAM role names, retrieves their associated inline policies, creates equivalent managed policies, and then attaches these managed policies to the respective roles. It also records the roles that were modified during the process.

## **Prerequisites**

Before you use this script, ensure that you have:

- AWS CLI installed and configured with appropriate credentials.
- Python 3.x installed.
- Boto3 library installed (**`pip install boto3`**).
- A file named **`roles.txt`** in the same directory as the script, containing the names of the IAM roles to be processed, each on a new line.

## **Usage**

1. **Prepare the Roles File:**
Create a **`roles.txt`** file in the script's directory, listing the IAM role names you wish to process, one per line.
2. **Run the Script:**
Execute the script using Python:
    
    ```
    python inline-to-managed-0.1.py
    ```
    
3. **Output:**
The script will output the process logs to the console and record the names of roles whose policies were converted in **`modified_roles.txt`**.

## **Key Functions**

- **List Role Policies:** Lists the inline policies attached to a role.
- **Get Role Policy:** Retrieves a specific inline policy from a role.
- **Create Policy:** Creates a managed policy from an inline policy.
- **Attach Policy:** Attaches the created managed policy to the role.
- **Delete Role Policy:** Deletes the inline policy from the role.

## **Error Handling**

The script handles various exceptions, such as inability to list policies for a role or errors during policy creation. It logs these errors to the console for review.

## **Important Notes**

- Ensure that your AWS credentials have the necessary permissions to perform these actions.
- This script simulates policy creation, association, and deletion for demonstration purposes.
- Test this script in a non-production environment to verify its functionality before running it in a production setting.