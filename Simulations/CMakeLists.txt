CMAKE_MINIMUM_REQUIRED(VERSION 3.9 FATAL_ERROR)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

PROJECT(geant4-chibis)

FIND_PACKAGE(Geant4 REQUIRED ui_all vis_all)

IF (NOT Geant4_FOUND)
    MESSAGE(FATAL_ERROR "Geant4 not found!")
ENDIF (NOT Geant4_FOUND)

INCLUDE(${Geant4_USE_FILE})

set(CMAKE_CONFIGURATION_TYPES Release)

find_package(Protobuf REQUIRED)
include_directories(${Protobuf_INCLUDE_DIRS})
INCLUDE(${Geant4_USE_FILE})

INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/include)
FILE(GLOB sources ${PROJECT_SOURCE_DIR}/src/*.cc)

# Здесь добавлять proto файлы
PROTOBUF_GENERATE_CPP(PROTO_SRCS PROTO_HDRS proto/satellite.proto proto/histogram.proto)
protobuf_generate_python(PY_SOURCES proto/satellite.proto proto/histogram.proto)
add_custom_target(py_proto ALL DEPENDS ${PY_SOURCES})

ADD_EXECUTABLE(geant4-chibis.exe main.cc
        ${sources}
        ${PROTO_SRCS}
        ${PROTO_HDRS}
        )

target_include_directories(geant4-chibis.exe
        PUBLIC
        ${CMAKE_CURRENT_BINARY_DIR}
        )

TARGET_LINK_LIBRARIES(geant4-chibis.exe
        ${Geant4_LIBRARIES} ${Protobuf_LIBRARIES}
)


# Здесь добавлять gdml и mac файлы чтобы скопировать их в место сборки
set(PROGRAM_SCRIPTS
        init_vis.mac
        macros/init.mac
        gdml/satellite.gdml
        )

foreach(_script ${PROGRAM_SCRIPTS})
    configure_file(
            ${PROJECT_SOURCE_DIR}/${_script}
            ${PROJECT_BINARY_DIR}/${_script}
            COPYONLY
    )
endforeach()
