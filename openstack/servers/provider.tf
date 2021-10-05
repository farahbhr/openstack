terraform {
  required_providers {
      openstack = { 
            source = "terraform-provider-openstack/openstack"
      }
  }
}


# Configurformie the OpenStack Provider
provider "openstack" {
  user_name   = "admin"
  tenant_name = "admin"
  password    = var.passwd
  auth_url    = var.auth_url
  region      = "RegionOne"
  use_octavia   = true
}
