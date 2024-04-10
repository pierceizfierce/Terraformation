# variables.tf - Input variables for the EC2 instance module

variable "ami_id" {
  description = "The AMI ID for the EC2 instance"
}

variable "instance_type" {
  description = "The type of EC2 instance to launch"
}

variable "key_name" {
  description = "The SSH key pair name to associate with the EC2 instance"
}

variable "subnet_id" {
  description = "The subnet ID in which to launch the EC2 instance"
}

variable "instance_name" {
  description = "The name tag for the EC2 instance"
  default     = "MyInstance"
}

variable "region" {
  description = "The AWS region to deploy resources"
  default     = "us-east-1"
}

