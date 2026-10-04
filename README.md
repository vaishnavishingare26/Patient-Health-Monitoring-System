# Patient Health Monitoring System

An IoT-based patient health monitoring system designed to monitor vital health parameters in real time and provide alerts during abnormal conditions.

## 📌 Overview

The Patient Health Monitoring System combines IoT hardware, Python-based monitoring, and a web interface to enable remote monitoring of patient health parameters.

The system continuously collects health data from sensors and processes the readings to identify abnormal conditions. When a critical condition is detected, the system can generate alerts for timely attention.

## ✨ Features

- Real-time patient health monitoring
- Temperature monitoring
- Sensor-based health data collection
- Automatic abnormal-condition detection
- Audio alert system
- WhatsApp alert integration
- Live image capture
- Web-based monitoring dashboard
- Arduino/ESP-based hardware integration
- Remote health monitoring support

## 🏗️ System Architecture

```text
Health Sensors
      ↓
Arduino / ESP Hardware
      ↓
Sensor Data Collection
      ↓
Python Monitoring Engine
      ↓
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
Dashboard     Alert System    Image Capture
                  ↓
            WhatsApp Alert
