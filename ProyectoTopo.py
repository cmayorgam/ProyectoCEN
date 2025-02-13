#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='33.111.44.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch, failMode='standalone')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, failMode='standalone')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')
    info('*** Add hosts\n')
    h5 = net.addHost('h5', cls=Host, ip='33.111.44.5', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='33.111.44.6', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='33.111.44.7', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='33.111.44.8', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='33.111.44.9', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='33.111.44.10', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='33.111.44.11', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='33.111.44.12', defaultRoute=None)
