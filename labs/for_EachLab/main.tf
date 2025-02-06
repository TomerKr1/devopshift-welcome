variable "enabled_services" {
    type    = set(string)
  default = ["prod"]
}

variable "s3_buckets" {
  type    = set(string)
  default = ["prod", "dev"]
}

resource "aws_s3_bucket" "buckets" {
  #for_each = { for service in var.s3_buckets : service => service if contains(var.enabled_services, service) }

for_each = toset([for service in var.s3_buckets : service if contains(var.enabled_services, service)])

  bucket = "my-app-${each.key}"


  tags = {
    Name        = "Bucket for ${each.key}"
    Environment = "${each.key}"
  }
}
