cmake_minimum_required(VERSION 2.8)
project(calibration-interface)


find_package(PythonInterp REQUIRED)

function(add_python_test)
    list(LENGTH ARGN NUM_ARGUMENTS)
    if (NOT ${NUM_ARGUMENTS} EQUAL 2)
        message(FATAL_ERROR
                "[ DectrisTesting ] add_python_test needs exactly two arguments (TestName, TestBinary)")
    endif()
    list(GET ARGN 0 TEST_NAME)
    list(GET ARGN 1 TEST_BINARY)
    add_test(NAME ${TEST_NAME} COMMAND ${PYTHON_EXECUTABLE} -m pytest ${TEST_BINARY} --junit-xml=${TEST_NAME}.pytest.xml)

    message(STATUS "[ DectrisTesting ] Added pytest ${TEST_NAME}")
endfunction()



enable_testing()

add_subdirectory(python)

#add_python_test(Test_ServoHand ${CMAKE_CURRENT_SOURCE_DIR}/tests/Test_ServoHand.py)
