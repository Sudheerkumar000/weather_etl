import boto3
import os
from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_name="weather_log.csv", bucket_name="sudheer-s3tos3", s3_file_name="weather_log.csv"):
    try:
        print(f"📦 Uploading {file_name} to S3 bucket: {bucket_name} as {s3_file_name}")

        # ✅ Check if the file exists
        if not os.path.exists(file_name):
            print(f"❌ File '{file_name}' does not exist in the current directory.")
            return
        else:
            print(f"✅ File '{file_name}' found. Proceeding to upload...")

        # 🔁 Upload to S3
        s3 = boto3.client('s3', region_name='us-east-2')
        s3.upload_file(file_name, bucket_name, s3_file_name)
        print(f"✅ Uploaded {file_name} to s3://{bucket_name}/{s3_file_name}")

    except FileNotFoundError:
        print(f"❌ File {file_name} not found.")
    except NoCredentialsError:
        print("❌ AWS credentials not found.")
    except Exception as e:
        print(f"❌ Failed to upload to S3: {e}")
