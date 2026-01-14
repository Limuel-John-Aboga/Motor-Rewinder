# Motor-Rewinder

**Motor-Rewinder** is the source code and control system for a compact stepper-motor-based **motor rewinding device** using a Raspberry Pi Pico W microcontroller.  
This system performs controlled winding and rewinding operations with memory-based turn counting for enhanced reliability and fail-safe behavior.

---

## Table of Contents

1. **About**
2. **Features**
3. **Hardware Components**
4. **Software Structure**
5. **Functional Description**
6. **Installation**
7. **Usage**
8. **File Overview**
9. **Limitations and Notes**
10. **Contributing**
11. **License**

---

## About

The Motor-Rewinder project implements a stepper-motor control system that executes forward and backward rotation steps to assist with motor rewinding operations. It integrates:

- **Raspberry Pi Pico W** (control logic)
- **Tactile push button**
- **28BYJ-48 stepper motor and driver**
- **Turn-count memory** to preserve state across power cycles

The system moves the motor forward by a fixed number of steps, then performs an inverse motion, and retains the turn count for safety and consistency.

---

## Features

- Precise stepper motor control for rewinding tasks
- Memory storage of turn count for fail-safe restarts
- Simple, compact control logic in Python
- Runnable on **Raspberry Pi Pico W** using MicroPython

---

## Hardware Components

To build and run this system, you need:

- **Raspberry Pi Pico W**
- **28BYJ-48 stepper motor**
- **ULN2003 / stepper motor driver board**
- **One tactile push button**
- Power supply (module-appropriate voltage)

The Pico W handles all motor stepping and input logic.

---

## Software Structure

The repository includes:

| File | Purpose |
|------|---------|
| `main.py` | Primary entry point controlling loops and button events |
| `stepper.py` | Stepper motor control functions and movement logic |
| `turns.txt` | Persistent storage of accumulated turns |
| `README.md` | Project documentation and usage overview |

---

## Functional Description

**Operation Flow**

1. On boot, the system reads `turns.txt` to get the saved turn count.
2. The user actuates the **push button** to trigger a motor movement.
3. The controller:
   - Moves the stepper motor forward (configured number of steps/revolutions)
   - Optionally performs a backward (inverse) movement
4. After movement, the system updates the turn count to persistent memory.
5. The turn count allows the rewinder to resume reliably after power loss.

This logic makes the system suitable for repeated rewinding operations without losing progress.

---

## Installation

1. Install **MicroPython** on Raspberry Pi Pico W.
2. Upload the repository files (`main.py`, `stepper.py`, `turns.txt`) to the Pico filesystem.
3. Ensure the stepper wiring matches the pin configuration referenced in the code.

Tools like **Thonny IDE** make Pico file uploads straightforward.

---

## Usage

1. Power up the Raspberry Pi Pico W.
2. Confirm power to the stepper driver and motor.
3. Actuate the push button to perform a rewind or forward motion.
4. The system will update the turn count after each cycle.

Modify logic in `main.py` to adjust steps, speeds, or button behavior.

---

## File Overview

### main.py

Handles:

- Button input
- Turn direction logic
- Integration with stepper control functions

### stepper.py

Defines:

- Motor stepping functions
- Direction control
- Timing and step count parameters

### turns.txt

Stores:

- Integer representing the total completed turns
- Used on restart to restore state

---

## Limitations and Notes

- Designed for **demo and simple rewinding tasks only**
- Only one push button input supported for control logic
- Turn-count persistence depends on text file integrity
- Not intended for high-speed industrial applications

---

## License

Distributed under open source terms (refer to repository license).

---

