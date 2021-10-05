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

resource "openstack_compute_keypair_v2" "test-keypair" {
  count= var.count_web
  name = "my-keypair"
}


resource "openstack_compute_instance_v2" "web_server1" {
  count           = var.count_web
  name            = "web_server1"
  image_id        = var.image_id
  flavor_id       = "2"
  network {
    name = "network_web"
  }
}

resource "openstack_networking_floatingip_v2" "fip_1" {
  pool = "external"
}

resource "openstack_compute_floatingip_associate_v2" "fip_1" {
  floating_ip = "${openstack_networking_floatingip_v2.fip_1.address}"
  instance_id = "${openstack_compute_instance_v2.web_server1[0].id}"
}

resource "openstack_compute_instance_v2" "app1" {
  count           = var.count_app
  name            = "app1"
  image_id        = var.image_id
  flavor_id       = "1"
  security_groups = ["${openstack_compute_secgroup_v2.secgroup_app.id}"]


  network {
    name = "network_app"
  }
}


resource "openstack_compute_instance_v2" "data" {
  count           = var.count_data
  name            = "data"
  image_id        = var.image_id
  flavor_id       = "1"
  security_groups = ["${openstack_compute_secgroup_v2.secgroup_data.id}"]


  network {
    name = "network_data"
  }
}




