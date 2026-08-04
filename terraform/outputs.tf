output "bucket_name" {
  value = aws_s3_bucket.avatars.bucket
}

output "table_name" {
  value = aws_dynamodb_table.users.name
}