
# AWS Serverless Image Processing API

## Overview
A serverless AWS project that uploads an image to S3, triggers Lambda, resizes the image, and saves it to a destination bucket.

## Services Used
- AWS S3
- AWS Lambda
- API Gateway
- IAM

## Features
- Auto image resize
- Event‑driven architecture
- Serverless and scalable

## Folder Structure
- lambda_function.py  
- requirements.txt  
- template.yaml  

## Deployment
zip -r function.zip .
aws lambda update-function-code --function-name ImageProcessor --zip-file fileb://function.zip
