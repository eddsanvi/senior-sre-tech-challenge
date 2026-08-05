output "bucket_name" {
  value = aws_s3_bucket.avatars.bucket
}

output "table_name" {
  value = aws_dynamodb_table.users.name
}

output "iam_role_name" {

  value = aws_iam_role.user_api_role.name

}