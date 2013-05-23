#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Caracal - A highly scalable load testing tool"""

__appname__ = "caracal"
__author__ = "Kingshuk Dasgupta (rextrebat/kdasgupta)"
__version__ = "0.0pre0"
#__license__ = "GNU GPL 3.0 or later"

import logging
logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s'
        )


def send_request():
    pass


def request_timer():
    pass


if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(description=__doc__,
            version="%%prog v%s" % __version__)
    #parser.add_option('-v', '--verbose', action="store_true", dest="verbose",
    # default=False, help="Increase verbosity")
    parser.add_option('-r', '--rate', type="float", dest="tps_rate", help="TPS Rate")

    opts, args = parser.parse_args()

    print "Starting TPS: %f" % (opts.tps_rate)
