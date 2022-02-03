# garden
An automated gardening monitoring application.
Intended to be ran on a Raspberry Pi with GPIO pins, network connectivity,
an hygrometer, temperature, light sensors and LED strips.

## Description

A Flask API with PyGPIO bindings. The API exposes a /metrics endpoint that
displays the status of the various sensors hooked to it. It also controls
the time table of when the LED strips should be light up and which light type
should be emitted.

A Grafana instance with Prometheus scraping the /metrics endpoint of the API
and displaying in a dashboard the state of the garden, sending Push notifications
should sensors pick up anomalies.

The whole application stack can be deployed via an Ansible playbook.



## Buying list

| Material | Status | Link |
|----------|--------|------|
| Hygrometer         | Not buyed yet       |      |
| Temperature         | Not buyed yet       |      |
| Light         |        |      |
| LED Strips         |        |      |
|          |        |      |