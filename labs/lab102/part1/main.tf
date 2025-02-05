provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}

variable "publicID" {
  default = ""
}

/*terraform {
  required_providers {
    time={
      source="hashicorp/time"
      version = "0.12.1"
    }
  }
}*/


resource "null_resource" "check_public_ip" {
  provisioner "local-exec" {
    command = <<EOT
      if [ -z "${var.publicID}" ]; then
        echo "ERROR: Public IP address tomer was not assigned." >&2
        exit 1
      fi

        echo "im trying again..."
        if [ -n "${aws_instance.vm.public_ip}" ]; then
          echo "you got an amazing ip!"
        fi
      
    EOT
  }
  /*triggers = {
    timestamp = "${timestamp()}"
  }
  */
}

resource "aws_security_group" "sg" {
ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "vm" {
  ami           = "ami-0ff8a91507f77f867" # Amazon Linux 2 AMI in us-east-1
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.sg.id]
  

  tags = {
    Name = "TomerK-vm"
  }
}




output "vm_public_ip" {
  value       = aws_instance.vm.public_ip
  description = "Public IP address of the VM"
  depends_on = [null_resource.check_public_ip]
}



# to see all the details. 
#aws ec2 describe-instances --instance-ids i-0919a052c41cf3309 --query "Reservations[*].Instances[*].[InstanceId, PublicIpAddress, State.Name, InstanceType, SecurityGroups[*].GroupId]" --output table
# or 
#aws ec2 describe-instances --filters "Name=tag:Name,Values=TomerK-vm" --output table
