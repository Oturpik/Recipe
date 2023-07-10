provider "aws" {
  region = "us-east-1"  # Replace with your desired AWS region
}

resource "aws_s3_bucket" "ToDo_bucket" {
  bucket = "terraform-s3-todo-bucket"
  acl    = "private"
}

resource "aws_iam_user" "my_user" {
  name = "todo-iam-user"
}

resource "aws_iam_policy" "bucket_access" {
  name        = "bucket-access-policy"
  description = "Allows read and write access to the S3 bucket"
  policy      = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::terraform-s3-todo-bucket",
        "arn:aws:s3:::terraform-s3-todo-bucket/*"
      ]
    }
  ]
}
EOF
}