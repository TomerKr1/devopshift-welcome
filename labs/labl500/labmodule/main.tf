module "Em2Builder" {
  source = "./moudles/ec2"
  ami = "ami-0c02fb55956c7d316"
  machinetype = "t2.micro"
  machinename ="Tomer"
}

output "print_module_ami" {
  value = module.Em2Builder.print_ami
}
output "print_module_publicIP" {
  value = module.Em2Builder.vm_public_ip
}

output "print_machineName" {
  value = module.Em2Builder.print_machine_name
}
output "test" {
  value=module.Em2Builder.DockDock
}