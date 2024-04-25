import json
import smtplib
from email.message import EmailMessage
import boto3

def get_secret():
    # Creating a Secrets Manager client obejct
    # I have stored secret with the key "AgileTrackSecret""
    client = boto3.client('secretsmanager')

    response = client.get_secret_value(SecretId='AgileTrackSecret')
    if 'SecretString' in response:
        secret = json.loads(response['SecretString'])
        return secret
    else:
        raise Exception('Unable to fetch secret')

def send_email(recipient, subject, body):
    secret = get_secret()
    email = secret.get('EMAIL')
    password = secret.get('EMAIL_PASSWORD')

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = recipient
    msg.set_content(body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email, password)
        server.send_message(msg)
        server.quit()
        return {'message': 'Email sent successfully'}
    except Exception as e:
        return {'error': str(e)}

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        recipient = data.get('recipient')
        subject = data.get('subject')
        body = data.get('body')
        if not recipient or not subject or not body:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing required fields'})
            }

        response = send_email(recipient, subject, body)
        status_code = 200 if 'message' in response else 500
        return {
            'statusCode': status_code,
            'body': json.dumps(response)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
