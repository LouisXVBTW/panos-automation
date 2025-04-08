resource "panos_address_object" "destination-server" {
  name        = "destination-server"
  value       = "192.168.80.5/32"
  description = "Address object 1 from Terraform"

  lifecycle {
    create_before_destroy = true
  }
}

resource "panos_address_object" "source-server" {
  name        = "source-server"
  value       = "192.168.120.8/32"
  description = "Address object 2 from Terraform"

  lifecycle {
    create_before_destroy = true
  }
}