# irunasroot.servicenow

[![GitHub License](https://img.shields.io/github/license/irunasroot/ansible-servicenow?style=for-the-badge&logo=github)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/irunasroot/ansible-servicenow/linter.yml?style=for-the-badge&label=Lint%20Codebase&logo=github)](https://github.com/marketplace/actions/super-linter)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/irunasroot/ansible-servicenow/molecule.yml?style=for-the-badge&logo=GitHub&label=Molecule%20Tests)](https://ansible.readthedocs.io/projects/molecule/)
[![Code style: black](https://img.shields.io/badge/Code%20Style-black-000000.svg?style=for-the-badge&logo=github)](https://github.com/psf/black)

Collection version 2.0.0

- [Description](#description)
- [Plugin Index](#plugin-index)

## Description

A collection to manage ServiceNow

> [!CAUTION]
> The refactoring to v2 breaks all functionalities of v1. Please migrate your
> playbooks to the proper variables.

Author:

- Dennis Whitney <[denniswhitney@irunasroot.com](denniswhitney@irunasroot.com)>

Supported ansible-core versions:

- 2.10.0 or newer

## Plugin Index

These are the plugins in the irunasroot.servicenow collection:

### Modules

- [irunasroot.servicenow.agent_client_collector][1] - Install Agent Client Collector

[1]: docs/irunasroot.servicenow.agent_client_collector.md
