# gersemi 

[![Build Status](https://travis-ci.com/BlankSpruce/gersemi.svg?token=jx3tcqsq9rGNwJNLQHdj&branch=master)](https://travis-ci.com/BlankSpruce/gersemi) [![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)

Tool to format CMake code. [WORK IN PROGRESS]

## Install gersemi

```
$ pip3 install git+https://github.com/BlankSpruce/gersemi
```

## Usage

```
$ gersemi CMakeLists.txt
if(TRUE)
    message(STATUS foo)
endif()
```

```
$ gersemi -i CMakeLists.txt
$ cat CMakeLists.txt
if(TRUE)
    message(STATUS foo)
endif()
```