# Group A Discord Bot

Discord Webhook Bot via AWS Lambda Function on Python 3.8+ runtime. Must be deployed on AWS Lambda.

## Dependencies

- AWS Account
- AWS CLI v2
- Python 3.8+
- requests
- python-dotenv
- boto3

## Usage

1. Create `package` folder to hold Lambda deployment package
```
mkdir package
```

2. Install requirements in `package` directory
```
pip install -r requirements.txt -t package
```

3. Copy `lambda_function.py` to `package` directory
```
cp lambda_function.py package
```

4. Zip `package` directory
```
zip -r ../package.zip .
```

5. Create AWS Lambda Function

6. Upload `package.zip` to AWS Lambda Function

7. Add resource-based policy to AWS Lambda to accept wildcard AWS EventBridge Rule triggers
```
aws lambda add-permission --statement-id "InvokeLambdaFunction" \
--action "lambda:InvokeFunction" \
--principal "events.amazonaws.com" \
--function-name "arn:aws:lambda:<region>:<account-id>:function:<function-name>" \
--source-arn "arn:aws:events:<region>:<account-id>:rule/*"
```

8. Add `WEBHOOK_URL` to Lambda Function environment variables
