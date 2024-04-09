# main.tf - Terraform configuration using the EC2 instance module

provider "aws" {
  region = "us-west-2"  # Update with your desired AWS region
}

module "Mod_CreateEC2" {
  source = "./.terraform"  # Path to the directory containing the module

  ami_id        = "ami-12345678"  # Update with your desired AMI ID
  instance_type = "t2.micro"      # Update with your desired instance type
  key_name      = "my-keypair"    # Update with your SSH key pair name
  subnet_id     = "subnet-12345678"  # Update with your desired subnet ID
  instance_name = "MyEC2Instance" # Update with your desired instance name
}
