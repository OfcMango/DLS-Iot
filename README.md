# NEO IoT-DSL

A Domain-Specific Language (DSL) for IoT automation using ESP32.

## Overview

NEO IoT-DSL is a custom programming language designed to simplify IoT automation.

Instead of writing complete Arduino C++ programs, users can write simple IoT-specific commands. The language is parsed and later translated into Arduino C++ code for ESP32.

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

## Example

```text
DEVICE LED PIN 2
DEVICE TEMP PIN 34

READ TEMP

IF TEMP > 30
    LED ON
ELSE
    LED OFF
END