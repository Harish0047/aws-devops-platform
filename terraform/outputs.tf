output "public_ip" {
  value = aws_instance.server.public_ip
}

output "instance_id" {
  value = aws_instance.server.id
}

output "ssh_command" {
  value = "ssh -i ~/.ssh/aws-devops-key ubuntu@${aws_instance.server.public_ip}"
}

output "grafana_url" {
  value = "http://${aws_instance.server.public_ip}:3000"
}
