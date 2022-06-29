## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    module = bld.create_ns3_module('npaf', ['internet', 'config-store','stats'])
    module.source = [
        'model/npaf-stats-packet-source.cc',
        'model/npaf-stats-packet-sink.cc',
        'model/npaf-stats-header.cc',
        'model/npaf-stats-data.cc',
        'model/npaf-stats-hist.cc',
        'helper/npaf-stats-helper.cc',
        ]

    applications_test = bld.create_ns3_module_test_library('npaf')
    applications_test.source = [
        ]

    headers = bld(features='ns3header')
    headers.module = 'npaf'
    headers.source = [
        'model/npaf-stats-packet-source.h',
        'model/npaf-stats-packet-sink.h',
        'model/npaf-stats-header.h',
        'model/npaf-stats-data.h',
        'model/npaf-stats-hist.h',
        'helper/npaf-stats-helper.h',
        ]
    
    if (bld.env['ENABLE_EXAMPLES']):
        bld.recurse('examples')

    #bld.ns3_python_bindings()
