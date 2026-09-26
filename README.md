# NEO IoT-DSL

A Domain-Specific Language (DSL) for IoT automation using ESP32.

## Overview

NEO IoT-DSL is a custom programming language designed to simplify IoT automation.

Instead of writing complete Arduino C++ programs, users can write simple IoT-specific commands. The language is parsed using ANTLR and is designed to be translated into Arduino C++ code for ESP32.

The project also provides a Python-based IDE-style application where users can write IoT DSL programs, compile them, view syntax errors, and inspect the generated parse tree.

## Architecture

IoT DSL Program

        ↓

Lexer

        ↓

Parser

        ↓

Semantic Analysis

        ↓

Intermediate Representation

        ↓

Code Generator

        ↓

Arduino C++

        ↓

ESP32

## Current Features

- Custom IoT-specific programming language
- ANTLR-based lexer and parser
- User-defined device identifiers
- Device declarations for LED, temperature sensor, and button
- Device ON/OFF commands
- WAIT commands
- Sensor READ commands
- IF / ELSE / END conditions
- LOOP commands
- Syntax error detection
- Parse tree generation
- Python-based IDE-style application
- Example IoT programs for testing

## Example

```text
DEVICE myLED LED PIN 2
DEVICE roomTemp TEMP PIN 34
DEVICE myButton BUTTON PIN 4

myLED ON
WAIT 1000
myLED OFF

READ roomTemp

IF roomTemp > 30
    myLED ON
ELSE
    myLED OFF
END

LOOP 3
    myLED ON
    WAIT 500
    myLED OFF
    WAIT 500
END
'''