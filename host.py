import paramiko

file = open("dane.txt", 'r')
res_file = open("wynik.txt", 'w')

domain_string = file.read()
domain_list = domain_string.split()

count = len(domain_list)

# ENTER YOUR DATA TO SSH CONNECTION

SSH_HOST = 'YOUR_SSH_HOST'
SSH_USERNAME = 'YOUR_SSH_USERNAME'
SSH_PASSWORD = 'YOUR_SSH_PASSW'


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_client.connect(SSH_HOST, username=SSH_USERNAME, password=SSH_PASSWORD)

    '''
    000.0 - here you can enter any ip that interest you
    x.xyz - here you can enter any domain that interest you
    '''
    for domain in domain_list:
        command = f'whois {domain}'
        stdin, stdout, stderr = ssh_client.exec_command(command)
        whois_output = stdout.read().decode("utf-8")

        found_sequence_sh = any(("x.yzx." in line) for line in whois_output.splitlines())
        found_sequence_cf = any(("cloudflare" in line) for line in whois_output.splitlines())
        found_sequence_whois = any(("undergoing proceeding" in line) for line in whois_output.splitlines())
        if found_sequence_sh or found_sequence_cf or found_sequence_whois:
            res_file.write(f'{domain} NIE\n')
        else:
            command = f'host {domain}'
            stdin, stdout, stderr = ssh_client.exec_command(command)
            host_output = stdout.read().decode("utf-8")

            found_sequence_host = any(("00.0" in line or "000.00" in line) for line in host_output.splitlines())
            if found_sequence_host:
                res_file.write(f'{domain} NIE\n')
            else:
                command = f'dig mx {domain}'
                stdin, stdout, stderr = ssh_client.exec_command(command)
                dig_output = stdout.read().decode("utf-8")

                command = f'host {dig_output}'
                stdin, stdout, stderr = ssh_client.exec_command(command)
                host_mx_output = stdout.read().decode("utf-8")

                found_sequence_mx = any(("00.0" in line or "000.00" in line) for line in host_mx_output.splitlines())
                if found_sequence_mx:
                    res_file.write(f'{domain} NIE\n')
                else:
                    res_file.write(f'{domain} \n')

except Exception as e:
    print("conn error:", e)

ssh_client.close()
file.close()
res_file.close()
