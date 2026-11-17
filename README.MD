# Autonomous Mobile Robot

Autonomous Mobile Robot is a AI-powered robotics project built on a Yahboom four-wheel mobile platform and Raspberry Pi 5. The project aims to progressively develop autonomous capabilities, including obstacle avoidance, computer vision, autonomous navigation and intelligent decision making. 


## Overview

The project is being developed incrementally, starting with low-level hardware control and progressing toward more advanced capabilities such as computer vision, obstacle avoidance, autonomous navigation, and AI-based decision-making. Rather than relying entirely on manufacturer-provided control functions, the project implements its own hardware abstraction and control layers to provide a deeper understanding of the robot and greater control over the software architecture. The system is designed to remain modular, allowing higher-level components to operate independently of hardware-specific implementation details. Ultimately, the goal is to transform a simple mobile robot into an intelligent autonomous system through the progressive integration of robotics and AI capabilities.

## Current Features

- Abstract drive interface
- Yahboom motor-control implementation using low-level I²C communication
- Normalized wheel-speed control in the range `[-1.0, 1.0]`
- Hardware-independent testing using fake drive and I²C implementations
- Automated unit testing with `pytest`

## Archtecture

The project follows a modular architecture that separates high-level robot logic from hardware-specific implementation details. `DriveBase` defines a common interface for controlling the robot's drive system, while `YahboomDrive` implements this interface for the physical Yahboom platform and handles the underlying I²C communication. This separation allows future components, such as navigation, perception, and AI-based decision-making, to control the robot without depending directly on Yahboom-specific hardware details. It also enables hardware-independent testing through fake implementations.

```text
Future High-Level Components
┌──────────────────────────────┐
│   Perception / AI            │
│   Planning / Navigation      │
│   Autonomous Decision-Making │
└──────────────┬───────────────┘
               │
               ▼
        ┌─────────────┐
        │  DriveBase  │
        └──────┬──────┘
               │
        ┌──────┴───────┐
        ▼              ▼
 ┌─────────────┐  ┌──────────────┐
 │  FakeDrive  │  │ YahboomDrive │
 └─────────────┘  └──────┬───────┘
                          │
                          ▼
                     ┌─────────┐
                     │ I²C Bus │
                     └────┬────┘
                          │
                          ▼
                  ┌────────────────┐
                  │ Motor Controller│
                  └────────────────┘
```

## Hardware

The project is built around a Raspberry Pi 5 and the Yahboom Raspbot mobile robotics platform.

- **Raspberry Pi 5 Model B — 4 GB RAM** — Main onboard computer responsible for running the robot software and, progressively, perception, navigation, and AI workloads.
- **Yahboom Raspbot AI Vision Robot Car** — Four-wheeled mobile robot platform providing the chassis, motors, motor-control electronics, camera system, and additional onboard hardware.
- **Camera** — Provides visual input for future computer-vision and perception capabilities.
- **64 GB SanDisk Extreme microSDXC (U3, V30, A2)** — Stores the Raspberry Pi operating system, project software, and related data.

The Raspberry Pi communicates with the Yahboom motor controller through **I²C**, with the current drive implementation using controller address `0x16`.

## Software Stack

- **Python 3.11+** — Primary programming language for robot control and future high-level robotics components.
- **pytest** — Unit testing framework used to verify hardware-independent and hardware-specific control logic.
- **SMBus / I²C** — Low-level communication interface between the Raspberry Pi and the Yahboom motor controller.
- **setuptools** — Python project packaging and editable installation through `pyproject.toml`.
- **Git & GitHub** — Version control and source-code management.
- **VS Code** — Primary development environment, including Remote SSH for development and testing on the Raspberry Pi.

## Project Structure

```text
autonomous-mobile-robot/
├── src/
│   └── autonomous_robot/
│       ├── __init__.py
│       ├── interfaces/
│       │   ├── __init__.py
│       │   └── drive_base.py
│       └── hardware/
│           ├── __init__.py
│           └── yahboom_drive.py
│
├── tests/
│   ├── fakes/
│   │   ├── __init__.py
│   │   ├── fake_drive.py
│   │   └── fake_i2c_bus.py
│   ├── test_fake_drive.py
│   └── test_yahboom_drive.py
│
├── docs/
├── .gitignore
├── pyproject.toml
└── README.md
```

### Directory Responsibilities

- **`src/autonomous_robot/interfaces/`** — Defines hardware-independent interfaces used by higher-level robot components.
- **`src/autonomous_robot/hardware/`** — Contains hardware-specific implementations, including the Yahboom drive system and its I²C communication logic.
- **`tests/`** — Contains automated tests for verifying the behavior of the robot software.
- **`tests/fakes/`** — Provides fake implementations of hardware-related components, allowing the software to be tested without requiring the physical robot.
- **`docs/`** — Reserved for additional technical documentation as the project grows.