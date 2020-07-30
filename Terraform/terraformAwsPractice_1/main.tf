provider "aws"{
    profile = "name of profile"
    region = "us-east-2"
}

module "network_module"{
    source = "./network_module"
}

module "loadbalabcer_module" {
    source = "./loadbalabcer_module"
    publicsg_id = "${module.network_module.publicsg_id}"
}