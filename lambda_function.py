import boto3
from PIL import Image
import io

s3 = boto3.client("s3")

SOURCE_BUCKET = "source-bucket-name"
DEST_BUCKET = "processed-bucket-name"

def lambda_handler(event, context):
    key = event["Records"][0]["s3"]["object"]["key"]
    file_obj = s3.get_object(Bucket=SOURCE_BUCKET, Key=key)
    image_data = file_obj['Body'].read()

    img = Image.open(io.BytesIO(image_data))
    img = img.resize((500, int(img.height * (500 / img.width))))

    buffer = io.BytesIO()
    img.save(buffer, "JPEG")
    buffer.seek(0)

    s3.put_object(
        Bucket=DEST_BUCKET,
        Key=f"processed-{key}",
        Body=buffer,
        ContentType="image/jpeg"
    )

    return {"statusCode": 200, "body": f"Image processed: processed-{key}"}