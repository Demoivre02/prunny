import boto3
from PIL import Image
import io

def resize_image(image, size):
    with Image.open(image) as img:
        img.thumbnail(size)
        buf = io.BytesIO()
        img.save(buf, format='JPEG')
        buf.seek(0)
    return buf

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    
    # Get the source bucket and key
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    
    # Download the image from S3
    image = s3_client.get_object(Bucket=source_bucket, Key=source_key)['Body']
    
    # Resize the image
    resized_image = resize_image(image, (300, 300))
    
    # Upload the resized image to a destination bucket
    destination_bucket = 'resized-images-bucket'
    destination_key = f'resized-{source_key}'
    s3_client.put_object(Bucket=destination_bucket, Key=destination_key, Body=resized_image)
    
    return {
        'statusCode': 200,
        'body': f'Image resized and saved as {destination_key} in {destination_bucket}'
    }

# Example usage (this won't actually run in this environment)
event = {
    'Records': [{
        's3': {
            'bucket': {'name': 'source-images-bucket'},
            'object': {'key': 'example.jpg'}
        }
    }]
}
context = {}
result = lambda_handler(event, context)
print(result)