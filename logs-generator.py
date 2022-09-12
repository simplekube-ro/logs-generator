#!/usr/bin/env python3

import sys
from random import randint
from time import sleep

from oslo_config import cfg
from oslo_log import log as logging

import lorem

LOG = logging.getLogger(__name__)
CONF = cfg.CONF
DOMAIN = "logs-generator"

logging.register_options(CONF)
CONF(sys.argv[1:])
logging.setup(CONF, DOMAIN)

while True:
    LOG.info(lorem.sentence())
    sleep(randint(0,5))
