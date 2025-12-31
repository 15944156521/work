cmake_minimum_required(VERSION 3.10)
project(compiler)

set(CMAKE_CXX_STANDARD 14)

add_executable(compiler
    main.cpp
    lexicalAnalysis.cpp
    # grammaticalAnalysis.cpp
    # SymbolTable.cpp
    # QuadrupleGenerator.cpp
    # 如有其它 .cpp 文件也一并添加
)

set(CMAKE_EXE_LINKER_FLAGS "-static")