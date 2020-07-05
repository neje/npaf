## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    module = bld.create_ns3_module('npaf', ['internet', 'config-store','stats'])
    module.source = [
        'model/stats-packet-source.cc',
        'model/stats-packet-sink.cc',
        'model/stats-header.cc',
        'model/stats-data.cc',
        'model/stats-hist.cc',
        'helper/stats-helper.cc',
        ]

    applications_test = bld.create_ns3_module_test_library('npaf')
    applications_test.source = [
        ]

    headers = bld(features='ns3header')
    headers.module = 'npaf'
    headers.source = [
        'model/stats-packet-source.h',
        'model/stats-packet-sink.h',
        'model/stats-header.h',
        'model/stats-data.h',
        'model/stats-hist.h',
        'helper/stats-helper.h',
        ]
    
    if (bld.env['ENABLE_EXAMPLES']):
        bld.recurse('examples')

    #bld.ns3_python_bindings()
