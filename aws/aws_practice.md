
# How to Create an AWS Account

Follow these steps to set up your Amazon Web Services (AWS) account.

## Step 1: Visit the AWS Website

1. Open your web browser.
2. Navigate to the [AWS website](https://aws.amazon.com/).

## Step 2: Start the Sign-Up Process

1. Click the **"Create an AWS Account"** button (top right corner).
2. Enter your **email address**, choose an **account name**, and create a **password**.
3. Click **Continue**.

## Step 3: Provide Personal or Business Information

1. Choose **Personal** or **Professional** account type.
2. Fill in your details:
   - Full Name
   - Phone Number
   - Country/Region
   - Address
   - City, State, Postal Code
3. Click **Continue**.

## Step 4: Add Payment Information

1. Enter valid **credit or debit card** details.
2. AWS may perform a small authorization charge to verify the card.
3. Click **Verify and Continue**.

## Step 5: Verify Your Identity

1. Choose your **phone verification method** (text message or call).
2. Enter the code sent to your phone.
3. Click **Verify Code**.

## Step 6: Select a Support Plan

1. Choose one of the following plans:
   - **Basic (Free)** — Ideal for learning and experimenting.
   - **Developer** — For development environments.
   - **Business** — For production workloads.

2. Click **Continue**.

## Step 7: Access the AWS Management Console

1. Once registration is complete, you’ll receive a confirmation email.
2. Return to the [AWS Console](https://aws.amazon.com/console/).
3. Log in with your credentials!


# AWS IAM (Identity and Access Management)

AWS IAM is a service that helps you securely control access to AWS resources. It allows you to manage users, groups, roles, and permissions.

## Key Concepts

- **Users**: Individuals or applications that need access to AWS services.
- **Groups**: Collections of users with shared permissions.
- **Roles**: Assumed by entities (like EC2 instances) to access resources.
- **Policies**: JSON documents that define permissions.
- **Access Keys**: Credentials for programmatic access to AWS.

## Features

- **Granular Permissions**: Control access at the resource level.
- **Federation**: Use external identity providers.
- **MFA (Multi-Factor Authentication)**: Enhance security with additional authentication layers.

## Best Practices

- Follow the principle of **Least Privilege**.
- Use **Roles** instead of long-term credentials.
- Enable **MFA** for sensitive operations.
- Regularly audit **IAM policies** and access logs.

IAM is foundational for AWS security — it ensures the right people and systems have the right access!

# IAM Passport Policy

In AWS Identity and Access Management (IAM), a **passport policy** isn't a standard AWS term, but if you're referring to identity federation or access control through temporary credentials, it may involve setting up policies for secure, time-limited access.

## 🛡️ **Key Concepts**

- **Identity Federation:** Allows users to access AWS using credentials from an external identity provider (IdP), like Google, Facebook, or corporate directories.
- **Temporary Security Credentials:** Issued via services like AWS STS (Security Token Service) for short-term access.
- **IAM Policies:** JSON documents defining permissions for users, groups, and roles.

## 🏗️ **Example Policy**
A sample IAM policy for temporary access:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::example-bucket"
        }
    ]
}

```

# AWS CLI and SDK

## 🖥️ AWS CLI (Command Line Interface)  
The **AWS CLI** is a tool that lets you interact with AWS services through the command line. It helps manage resources, automate tasks, and control AWS services directly from your terminal.

- **Use Cases:** Manage S3 buckets, launch EC2 instances, configure IAM users, and more.
- **Example Command:**  
   ```bash
   aws s3 ls

# AWS SDK (Software Development Kit)

The **AWS SDK** is a set of libraries and tools that help developers integrate AWS services into their applications. It simplifies making requests to AWS services by handling tasks like authentication, retries, and error handling.

## 📘 Key Features  
- **Language Support:** Available for Python, JavaScript, Java, C#, Ruby, PHP, Go, and more.  
- **Service Integration:** Access services like S3, EC2, DynamoDB, and others with minimal setup.  
- **Simplified API Calls:** Abstracts complex API requests into simple method calls.  

## 🛠️ Example (Python with Boto3)  
Here’s how you can list S3 buckets using the **Boto3** library in Python:  
```python
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List buckets
response = s3.list_buckets()

# Print bucket names
for bucket in response['Buckets']:
    print(bucket['Name'])


