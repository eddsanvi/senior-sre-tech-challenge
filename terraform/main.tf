terraform {
  required_version = ">= 1.0"
}

provider "aws" {
  region = var.aws_region

  access_key = "test"
  secret_key = "test"

  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  s3_use_path_style = true

  endpoints {
    s3       = "http://localhost:4566"
    dynamodb = "http://localhost:4566"
  }
}

resource "aws_s3_bucket" "avatars" {
  bucket = var.bucket_name
}

resource "aws_dynamodb_table" "users" {

  name         = var.dynamodb_table
  billing_mode = "PAY_PER_REQUEST"

  hash_key = "email"

  attribute {
    name = "email"
    type = "S"
  }
}

resource "aws_iam_policy" "user_api_policy" {

  name = "user-api-policy"

  policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {
        Effect = "Allow"

        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket"
        ]

        Resource = "*"
      },

      {
        Effect = "Allow"

        Action = [
          "dynamodb:GetItem",
          "dynamodb:PutItem",
          "dynamodb:Scan"
        ]

        Resource = "*"
      }

    ]
  })
}

resource "aws_iam_role" "user_api_role" {

  name = "user-api-role"

  assume_role_policy = jsonencode({

    Version = "2012-10-17"

    Statement = [
      {

        Effect = "Allow"

        Principal = {
          Service = "eks.amazonaws.com"
        }

        Action = "sts:AssumeRole"

      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "user_api_attach" {

  role       = aws_iam_role.user_api_role.name

  policy_arn = aws_iam_policy.user_api_policy.arn

}