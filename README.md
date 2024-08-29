# Media Service For Outfit Finder

This service is responsible for storing and serving all media files for the Outfit Finder application.

## Features
- Store images
- Serve images


## API Endpoints

| Endpoint     | Method | Description       |
|--------------|--------|-------------------|
| /            | POST   | Upload media file |
| /{file_name} | GET    | Get media file    |
| /{file_name} | DELETE | Delete media file |
| /{file_name} | PUT    | Update media file |

## Installation

1. Clone the repository
2. Install the dependencies
3. setup environment variables
    ```
    S3_ACCESS_KEY=your_s3_access_key (required)
    S3_SECRET_KEY=your_s3_secret_key (required)
    BUCKET_NAME=your_bucket_name (optional)
    S3_REGION=your_s3_region (optional)
    S3_TYPE=your_s3_type (optional - default: aws)
    ```
4. Run the application


## S3 types available
- aws
- minio