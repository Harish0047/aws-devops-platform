variable "region" {
  type    = string
  default = "ap-south-1"
}

variable "project" {
  type    = string
  default = "aws-devops-platform"
}

variable "instance_type" {
  description = "t3.small has 2 GB RAM, enough for the app, Prometheus and Grafana"
  type        = string
  default     = "t3.small"
}

variable "my_ip_cidr" {
  description = "Your public IP in CIDR form, for example 203.0.113.10/32"
  type        = string
}

variable "public_key_path" {
  type    = string
  default = "~/.ssh/aws-devops-key.pub"
}
