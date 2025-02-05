provider "aws" {
  region = "us-east-1"  # ודא שאתה משתמש באזור הנכון
}

data "aws_instance" "yaniv_vm" {

  instance_id = "i-09df7e0ed385f871b"
}

output "yaniv_vm_public_ip" {
  value       = data.aws_instance.yaniv_vm.public_dns                        
  description = "The public IP address of Yaniv's VM"
}

variable "emptyip" {
    default = "3333"
}

resource "null_resource" "check_public_ip" {
  provisioner "local-exec" {
    command = <<EOT
      if [ -z "${var.emptyip}" ]; then
        echo "ERROR: Public IP address was not assigned." >&2
        exit 1
        else
        echo "We got the IP! ${var.emptyip}"
      fi
    EOT
  }
}
#   depends_on = [aws_instance.vm]
