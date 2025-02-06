provider "aws" {
 region = var.region
}

variable "region" {
 default = "us-east-1"
}

variable "ami" {}

variable "machinetype" {}

variable "machinename" {}

variable "portlist" {
  description = "List of ports for ingress rules"
  type        = list(number)
  default     = [22]  # Default to port 22 if not specified
}

resource "aws_security_group" "sg" {
  // Ingress rules based on the portlist variable
  dynamic "ingress" {
    for_each = var.portlist
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  // Egress rule (same as before)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_instance" "vm" {
 ami           = var.ami
 instance_type = var.machinetype
 vpc_security_group_ids = [aws_security_group.sg.id]

 tags = {
   Name = var.machinename
 }
}

output "vm_public_ip" {
 value       = aws_instance.vm.public_ip
 description = "Public IP address of the VM"
 depends_on = [ null_resource.check_public_ip ]
}

                  
resource "null_resource" "check_public_ip" {
 provisioner "local-exec" {
   command = <<EOT
     if [ -z "${aws_instance.vm.public_ip}" ]; then
       echo "ERROR: Public IP address was not assigned." >&2
       exit 1
       else
       echo "We got the IP! ${aws_instance.vm.public_ip}"
     fi
   EOT
 }


 depends_on = [aws_instance.vm]
}

output "print_ami" {
  value = var.ami
}

output "print_machine_name" {
  value=var.machinename
}
output "DockDock" {
  value="This is a check message"
}

output "ingress_ports" {
  description = "The list of ports used in the ingress rules"
  value       = var.portlist
}

output "created_ingress_rules" {
  description = "The ingress rules created in the security group"
  value = aws_security_group.sg.ingress
}