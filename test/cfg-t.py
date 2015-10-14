#!/usr/bin/env python
# encoding: utf-8

from oslo_config import cfg
import sys

opts = [
    cfg.StrOpt('bind_host',default='0.0.0.0'),
]
cli_opts = [
    cfg.IntOpt('bind_port',default=9876),
]
gs_group = cfg.OptGroup(name='gs',title='golden state player numbers')
#gs_Thompson_opt = cfg.IntOpt('Thompson',default=0)
#gs_Curry_opt = cfg.IntOpt('Curry',default=0)
gs_group_opts = [
    cfg.IntOpt('Thompson',default=0),
    cfg.IntOpt('Curry',default=0),
]

#def register_gs_opts(conf):
#    conf.register_group(gs_group)
#    # options can be registered under a group in either of these ways:
#    conf.register_opt(gs_Thompson_opt, group=gs_group)
#    conf.register_opt(gs_Curry_opt, group='gs')
def register_any_group_opts(conf,group_to_regist=None,opts=[]):
    conf.register_group(group_to_regist)
    for i in opts:
        conf.register_cli_opt(i,group=group_to_regist)


CONF = cfg.CONF
CONF.register_opts(opts)
CONF.register_cli_opts(cli_opts)
#register_gs_opts(CONF)
register_any_group_opts(CONF,gs_group,gs_group_opts)

#print CONF.gs.Thompson
#print CONF.gs.Curry
#print CONF.bind_host
#print CONF.bind_port

CONF(args=sys.argv[1:])
print CONF.bind_host
print CONF.bind_port
print CONF.gs.Thompson
print CONF.gs.Curry


