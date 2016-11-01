
#file(GLOB dectris_python_dectris RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "*.py")
#message(STATUS "DECTRIS ${dectris_python_dectris}")

# this file is only needed for development as shall not be packed as dependency is 
# satisfied by the python-dectris package in the RPM 
#list(REMOVE_ITEM dectris_python_dectris "__init__.py")
#python_add_files(var_dectris_python_dectris ${dectris_python_dectris} INSTALL ${PYTHON_INSTDIR}/dectris)
#file(GLOB eiger2_files_pyx RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "*.py")
#list(REMOVE_ITEM eiger2_files_pyx "__init__.py")
#
#python_add_files(eiger2 "__init__.py" NUITKA ${eiger2_files_pyx} INSTALL ${PYTHON_INSTDIR}/dectris/resources/eiger2/ COMPONENT python)
#
#add_subdirectory(calibration)
#add_subdirectory(features)
add_subdirectory(tests)