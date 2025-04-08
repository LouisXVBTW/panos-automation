resource "panos_security_rule_group" "example_ruleset" {
  position_keyword = "bottom"
  rule {
    name                  = "example rule 1"
    source_zones          = ["any"]
    source_addresses      = [panos_address_object.source-server.name]
    source_users          = ["any"]
    destination_zones     = ["any"]
    destination_addresses = [panos_address_object.destination-server.name]
    applications          = ["ssh"]
    services              = ["any"]
    categories            = ["any"]
    action                = "allow"
  }
  rule {
    name                  = "example rule 2"
    source_zones          = ["trust"]
    source_addresses      = [panos_address_object.source-server.name]
    source_users          = ["any"]
    destination_zones     = ["any"]
    destination_addresses = [panos_address_object.destination-server.name]
    applications          = ["any"]
    services              = ["any"]
    categories            = ["any"]
    action                = "deny"
  }
  rule {
    name                  = "example rule 3"
    source_zones          = ["any"]
    source_addresses      = [panos_address_object.source-server.name]
    source_users          = ["any"]
    destination_zones     = ["any"]
    destination_addresses = [panos_address_object.destination-server.name]
    applications          = ["any"]
    services              = ["any"]
    categories            = ["any"]
    action                = "drop"
  }

  lifecycle {
    create_before_destroy = true
  }
}