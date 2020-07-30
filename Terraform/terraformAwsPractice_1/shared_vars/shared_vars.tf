output "vpcid" {
    value = "${local.vpcid}"
}

output "publicsubnetid2" {
    value = "${local.publicsubnetid1}"
}

output "publicsubnetid2" {
    value = "${local.publicsubnetid2}"
}

output "privatesubnetid" {
    value = "${local.privatesubnetid}"
}

output "env_suffix" {
    value = "${local.env}"
}

locals {
    env = "${terraform.workspace}"
########################################################
    vpcid_env {
        default = "paste vpc id here"
        staging = "paste vpc id here"
        production = "paste vpc id here"
    }
    vpcid = "${lookup(local.vpcid_env, local.env)}"
########################################################
    publicsubnetid1_env {
        default = "paste pub subnet id here"
        staging = "paste pub subnet id here"
        production = "paste pub subnet id here"
    }
    publicsubnetid1_env = "${lookup(local.publicsubnetid1_env, local.env)}"
########################################################
    publicsubnetid2_env {
        default = "paste pub subnet id here"
        staging = "paste pub subnet id here"
        production = "paste pub subnet id here"
    }
    publicsubnetid2_env = "${lookup(local.publicsubnetid2_env, local.env)}"
########################################################
    privatesubnetid_env {
        default = "paste priv subnet id here"
        staging = "paste priv subnet id here"
        production = "paste priv subnet id here"
    }
    privatesubnetid = "${lookup(local.privatesubnetid_env, local.env)}"
}
