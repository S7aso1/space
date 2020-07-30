#-------------Global variables-------------
variable "server_port" {
    description = "port for http requests"
    default = 8080
}
#-------------Security group configuration-------------

resource "aws_security_group" "instance"{
    name = "terraform-example-instance"

    ingress {
        from_port = "${var.server_port}"
        to_port = "${var.server_port}"
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}
#-------------Launch config creates instances before it destroys them-------------

resource "aws_launch_configuration" "launchConfig" {
    image_id = "paste ami id here"
    instance_type = "paste type of desired instance "
    security_groups = ["${aws_security_group.instance.id}"]
    lifecycle {
        create_before_destroy = true
    }
}
#-------------For the Autoscaling group to work we need launch configuration and AZs configured-------------

resource "aws_autoscaling_group" "autoScale" {
    launch_configuration = "${aws_launch_configuration.launchConfig.id}"
    availability_zones = ["${data.aws_availability_zones.all.names}"]

    min_size = 2
    max_size = 10 

    tag {
        key = "Name"
        value = "terraform-autoscale-group"
        propagate_at_launch = true
    }
}
#-------------Load balancer configuration-------------

resource "aws_elb" "loadBalancer" {
    name = "load-balancer-for-asg"
    availability_zones = ["${data.aws_availability_zones.all.name}"]
    security_groups = ["${$aws_security_group.sg4elb.id}"]

    listener {
        lb_port = 80
        lb_protocol = "http"
        instance_port = "${var.server_port}"
        instance_protocol = "http"
    }

    health_check {
        healthy_threshold = 2 
        unhealthy_threshold = 2
        timeout = 3
        interval = 30
        target = "HTTP:${var.server_port}/"
    }
#--threshold 2 = 2x30sec = 1 min--
}
#-------------ELB doesn't allow incoming/outgoing traffic so we need new explicit SG for it-------------

resource "aws_security_group" "sg4elb" {
    name = "sg-for-elb"

    ingress {
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}
