
build_lib(
  LIBNAME npaf
  SOURCE_FILES
    model/npaf-stats-packet-source.cc
    model/npaf-stats-packet-sink.cc
    model/npaf-stats-header.cc
    model/npaf-stats-data.cc
    model/npaf-stats-hist.cc
    helper/npaf-stats-helper.cc
  HEADER_FILES
    model/npaf-stats-packet-source.h
    model/npaf-stats-packet-sink.h
    model/npaf-stats-header.h
    model/npaf-stats-data.h
    model/npaf-stats-hist.h
    helper/npaf-stats-helper.h
  LIBRARIES_TO_LINK ${libinternet}
                    ${libconfigstore}
                    ${libstats}
  TEST_SOURCES

)
