module "EC2Builder_1" {
  source = "./moudles/ec2"
  ami = "ami-0c02fb55956c7d316"
  machinetype = "t2.micro"
  machinename ="Tomer"
}

output "print_module_ami" {
  value = module.EC2Builder_1.print_ami
}
output "print_module_publicIP" {
  value = module.EC2Builder_1.vm_public_ip
}

output "print_machineName" {
  value = module.EC2Builder_1.print_machine_name
}
output "test" {
  value=module.EC2Builder_1.DockDock
}