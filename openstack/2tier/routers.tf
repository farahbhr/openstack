
resource "openstack_networking_router_v2" "router_1" {
  name           = "router_1"
  admin_state_up = "true"
  external_network_id = "${openstack_networking_network_v2.external.id}"
}

resource "openstack_networking_router_interface_v2" "int_web" {
  router_id  = "${openstack_networking_router_v2.router_1.id}"
  subnet_id  = "${openstack_networking_subnet_v2.subnet_web.id}"
}

resource "openstack_networking_router_v2" "router_2" {
  name           = "router_2"
  admin_state_up = "true"
}

