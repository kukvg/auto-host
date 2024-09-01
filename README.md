# Script for Automating Tasks of a Hosting Company Employee

This script is designed for employees of hosting companies to automate their daily tasks. It allows users to search for domain compliance with specific guidelines, such as identifying domains originating from a particular hosting company based on the domain name. If a domain does not meet the guidelines, the script analyzes the IP address with a separate command and compares it with expected results (e.g., `000.0` - indicating our IP). Based on this analysis, the script will return whether the domain meets the criteria of originating from a specified company. A result of "NO" indicates compliance with the guidelines and the inability to delist.

## Features

- **Domain WHOIS Check**: Uses the whois command to fetch domain registration details and checks for specific keywords or patterns such as "x.yzx.", "cloudflare" to determine if a domain meets the criteria.
- **IP Address Verification**: If the initial domain check does not meet the criteria, the script further analyzes the domain's IP address using the host command to ensure it does not match any restricted IP patterns (e.g., 00.0 or 000.00).
- **MX Record Analysis**: If the domain still does not meet the criteria, it performs a dig mx command to check the domain's MX (Mail Exchange) records and further verifies the host information for these records.
- **Automated Reporting**: Writes the results to an output file (wynik.txt), indicating "NIE" (NO in Polish) if the domain does not meet the criteria and leaving it blank otherwise.
  
## Prerequisites

- Paramiko library for Python to establish an SSH connection to the remote server.
- Access to a remote server that supports SSH, where whois, host, and dig commands can be executed.
- A text file (dane.txt) containing the list of domains to check, with each domain on a new line.

## Getting Started

1. **Clone the Repository**: Ensure you have access to the repository containing the script.
   ```bash
   git clone https://github.com/kukvg/auto-host.git
   ```
2. **Install Dependencies**: Install any required dependencies needed for the script to function properly.
   ```bash
   pip install paramiko
   ```
   
3. **Run the Script**: Execute the script in your preferred environment.
   ```bash
   python host.py
   ```

## Built With

- **Python** - The main programming language used for scripting.
- **Paramiko** - A Python library that provides the capability to make SSH2 connections to remote machines, used here for remote server management and task automation.
- **WHOIS, Host, Dig Commands** - Used on the remote server to perform domain and IP address lookups.

## Usage

1. Prepare your dane.txt file with the domains you want to check.
   
2. Run the script after configuring your SSH credentials and environment.
   ```bash
   python host.py
   ```
  
3. Review the wynik.txt file for the results of the checks.

## Author

- **Dominik Kuka**

## License

This project is licensed under the MIT License.

## Inspiration

This script was created to simplify and automate routine checks performed by hosting company employees, ensuring efficient and accurate domain management.
