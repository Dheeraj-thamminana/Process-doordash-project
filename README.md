# DoorDash Delivery Data Processing with AWS

This project automates the processing of daily delivery data from DoorDash using AWS services. The solution involves uploading JSON files containing delivery records to an Amazon S3 bucket, filtering these records with an AWS Lambda function, and then saving the filtered data to another S3 bucket. Notifications about the processing outcome are sent via Amazon SNS.

# Requirements
  
AWS Account

Amazon S3 Buckets

AWS Lambda

Amazon SNS

AWS IAM

AWS CodeBuild

GitHub for version control

Python with pandas library

Email subscription for SNS notifications


# Setup Guide
   1. S3 Buckets Setup
      
      Create two Amazon S3 buckets:
      
          my-doordash-landing-zn: #For incoming raw files.
          my-doordash-target-zn:  #For storing processed files.
      
   2. Amazon SNS Topic Setup

      Create an Amazon SNS topic for processing notifications and subscribe your email to receive these notifications.

  3. IAM Role for Lambda
   
      Create an IAM role with permissions to:

        Read from my-doordash-landing-zn.
     
        Write to my-doordash-target-zn.
     
        Publish messages to your SNS topic.
     
        Ensure the IAM policy allows s3:GetObject on my-doordash-landing-zn/* and s3:PutObject on my-doordash-target-zn/*.

  4. AWS Lambda Function

      Create a Lambda function with the following specifications:

        Runtime: Python 3.8 or higher.
     
        Trigger: Set to be invoked upon file uploads to my-doordash-landing-zn.

        Code: Include logic to read the JSON file into a pandas DataFrame, filter records by "delivered" status, and write the filtered DataFrame to a new JSON file in my-doordash-target-zn. 

        Finally, publish a success message to the SNS topic.
     
   5. AWS CodeBuild for CI/CD

       Host your Lambda function code on GitHub. Set up an AWS CodeBuild project linked to your GitHub repository to automate the deployment of your Lambda function code updates.

	
   6. Steps to Set Up CI/CD with AWS CodeBuild
				
		 > Prepare Your Lambda Function Code

        Ensure your Lambda function code is in a GitHub repository. This code should include:
				
        The Python script for your Lambda function.

        Any dependencies listed in a requirements.txt file, if you're using external libraries.

        A buildspec.yml file that specifies build commands and settings for CodeBuild.

   7. Testing and Verification
      
       Upload Sample JSON: Upload a sample JSON file to my-doordash-landing-zn and verify that the Lambda function triggers correctly.

       Check Processed File: Look in my-doordash-target-zn for the processed file and confirm its contents match the expected output.

       SNS Notification: Ensure you receive an email notification upon processing completion.

   8. Sample Test Event JSON for Lambda
      
       To test the Lambda function, use the following event template, incase if you are tesing with any other json file uploading in the landing S3 bucket then replacew the "2024-03-09-raw_input.json" with the file name you're testing:

	{
    "Records": [
    {
      "s3": {
        "bucket": {
          "name": "my-doordash-landing-zn"
        },
        "object": {
          "key": "2024-03-09-raw_input.json"
        }
      }
    }
	]
    }


# Troubleshooting

there are the common troubleshoots you might be facing while implementing the process, make sure to ensure as suggested below.

 **Access Denied Errors:** Ensure your IAM role has the correct permissions and there are no conflicting bucket policies.

 **Function Not Triggering:** Verify the S3 trigger configuration in your Lambda function.




**All the required input documents were already attached to this repository, you can either clone or verify them before implementing**
