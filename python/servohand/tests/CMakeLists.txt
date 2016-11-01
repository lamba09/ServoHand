#file(GLOB python_files RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "*.py")
#python_add_files(eiger2_test ${python_files} INSTALL ${PYTHON_INSTDIR}/dectris/resources/eiger2/features/test COMPONENT python-test)
#
#include(DectrisTesting)
#add_python_test(Test_Eiger2ConfigurationStructure ${CMAKE_CURRENT_BINARY_DIR}/Test_Eiger2ConfigurationStructure.py)
#add_python_test(Test_SeriesConfig ${CMAKE_CURRENT_BINARY_DIR}/Test_SeriesConfig.py)

add_python_test(Test_ServoHand ${CMAKE_CURRENT_SOURCE_DIR}/Test_ServoHand.py)
add_python_test(Test_ServoFinger ${CMAKE_CURRENT_SOURCE_DIR}/Test_ServoFinger.py)
add_python_test(Test_ServoControlBoard ${CMAKE_CURRENT_SOURCE_DIR}/Test_ServoControlBoard.py)
