# irunasroot.servicenow.agent_client_collector - Installs ServiceNow Agent Client Collector

This module is part of the irunasroot.servicenow collection (version 2.0.0).

To check whether it is installed, run `ansible-galaxy collection list`.

To install it, use: `ansible-galaxy collection install irunasroot.servicenow`.

To use it in a playbook, specify: `irunasroot.servicenow.agent_client_collector`.

- [Synopsis](#synopsis)
- [Requirements](#requirements)
- [Parameters](#parameters)
- [Notes](#notes)
- [Examples](#examples)

## Synopsis

- Installs Agent Client Collector using Ansible Modules (no custom plugins).
- Supports both Linux and Windows systems; macOS systems are untested with this module.
- Only Agent Client Collector versions 2.7.0 and above are supported due to
  configuration differences in order versions.
- Please read some important information in the [Notes](#notes) section

## Requirements

If using Windows you will need the required packages and tools for a login
method as [outlined by Ansible](https://docs.ansible.com/ansible/latest/user_guide/windows_winrm.html#authentication-options).

## Parameters

### Base Parameters

| Parameter                                                    | Comments                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| agent_client_collector_package_name<br/>string               | The name of the Linux package to install.<br/>Default: agent-client-collector                                                                                                                                                                             |
| agent_client_collector_version<br/>string                    | The version of Agent Client Collector you want to install.                                                                                                                                                                                                |
| agent_client_collector_download_path<br/>string              | If not using a package manager on Linux you can specify a path.<br/>For Windows this would be the URL, UNC, or Local path to the MSI.                                                                                                                     |
| agent_client_collector_product_code<br/>string                   | On Windows you can specify the ProductCode of the installed version. If this is not specified then an attempt will be made to determine based off the MSI installer                                                                                       |
| agent_client_collector_config_file_path<br/>string           | The file path to `acc.yml`.<br/>On Windows this defaults to: `C:\ProgramData\ServiceNow\agent-client-collector\config\acc.yml`.<br/>On Linux this defaults to `/etc/servicenow/agent-client-collector/acc.yml`                                            |
| agent_client_collector_check_allow_list_file_path<br/>string | The file path to `check-allow-list.json`.<br/>On Windows this defaults to: `C:\ProgramData\ServiceNow\agent-client-collector\config\check-allow-list.json`.<br/>On Linux this defaults to: `/etc/servicenow/agent-client-collector/check-allow-list.json` |

### Config acc.yml Parameters

| Parameter                                                                           | Comments                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| agent_client_collector_config_name</br>string                                       | The name of the agent<br/>Default: {{ ansible_fqdn }}                                                                                                                                                                                                                                                                                                                                                                                  |
| agent_client_collector_config_backend_url<br/>list / elements=string                | A list of backend URL's of MID servers.<br/>Default: []                                                                                                                                                                                                                                                                                                                                                                                |
| agent_client_collector_config_api_key<br/>string                                    | The ServiceNow API token. Should be the encrypted value of the key. See the [notes](#notes) section.                                                                                                                                                                                                                                                                                                                                   |
| agent_client_collector_config_agent_key_id<br/>string                               | The agent key id for encrypting the API key. See the [notes](#notes) sections.                                                                                                                                                                                                                                                                                                                                                         |
| agent_client_collector_config_user<br/>string                                       | If not using an api key you can specify a username/password.                                                                                                                                                                                                                                                                                                                                                                           |
| agent_client_collector_config_password<br/>string                                   | If not using an api key you can specify a username/password.                                                                                                                                                                                                                                                                                                                                                                           |
| agent_client_collector_config_log_level<br/>string                                  | The logging level of the agent.<br/>Default: info                                                                                                                                                                                                                                                                                                                                                                                      |
| agent_client_collector_config_skip_tls_verify<br/>boolean                           | Set true to skip MID server TLS certificate verification.<br/>Default: true                                                                                                                                                                                                                                                                                                                                                            |
| agent_client_collector_config_trusted_ca_file<br/>string                            | File path to the CA certificate for MID server connection.                                                                                                                                                                                                                                                                                                                                                                             |
| agent_client_collector_config_allow_list<br/>string                                 | File path to the `check-allow-list.json`. Default: {{ agent_client_collector_check_allow_list_file_path }}                                                                                                                                                                                                                                                                                                                             |
| agent_client_collector_config_redact<br/> list / elements=string                    | A list of values to redact from data being sent to ServiceNow.<br/>Default: ["username","bearer_token","auth_algorithm","access_key","enrollment_number","auth_method","client_id","ea_credential","certificate","cert_alias","secret_key","password","passwd","pass","api_key","api_token","private_key","secret","ssh_private_key","ssh_passphrase","authentication_key","authentication_protocol","privacy_key","privacy_protocol"] |
| agent_client_collector_config_verify_plugin_signature<br/>boolean                   | Set to true to validate ACC plugins.<br/>Default: true                                                                                                                                                                                                                                                                                                                                                                                 |
| agent_client_collector_config_max_running_checks<br/>integer                        | Max number of checks to run.<br/>Default: 10                                                                                                                                                                                                                                                                                                                                                                                           |
| agent_client_collector_config_agent_cpu_threshold_cpu_percentage_limit<br/>integer  | The max percentage of CPU to limit to.<br/>Default: 5                                                                                                                                                                                                                                                                                                                                                                                  |
| agent_client_collector_config_agent_cpu_threshold_repeated_high_cpu_num<br/>integer | The max number of times to hit the CPU limit.<br/>Default: 3                                                                                                                                                                                                                                                                                                                                                                           |
| agent_client_collector_config_agent_cpu_threshold_monitor_interval_sec<br/>integer  | The number of seconds to monitor the CPU threshold.<br/>Default: 60                                                                                                                                                                                                                                                                                                                                                                    |
| agent_client_collector_config_agent_cpu_threshold_agent_cpu_threshold_disabled<br/>boolean | Set to true to disable CPU threshold monitoring.<br/>Default: false |
| agent_client_collector_config_agent_cpu_threshold_proxy_cpu_percentage_limit<br/>integer | The max percentage of CPU proxy to limit to.<br/>Default: 15 |
| agent_client_collector_config_disable_sockets<br/>boolean | Set to true to disable sockets.<br/>Default: true |
| agent_client_collector_config_statsd_disable<br/>boolean | Set to true to disable statsd checks.<br/>Default: true |
| agent_client_collector_config_check_commands_prefer_installed<br/>boolean | Set to true to prefer check commands packaged with plugins first.<br/>Default: false |
| agent_client_collector_config_enable_auto_mid_selection<br/>boolean | Set to true to auto select MID server.<br/>Default: true |

### Config check-allow-list.json Parameters

| Parameter                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| agent_client_collector_check_allow_list<br/>list / elements=dictonary | A list of rulesets that go into the `check-allow-list.json` file. Each element requires three paramters to be specified:<br/><ul><li>exec: The name of the executable script.</li><li>skip_arguments: Set to true if arguments passed to the script should be skipped.</li><li>args: A list of allowed arguments that can be passed into the script. By default this list will be blank if not defined.</li></ul>Default: [{"exec":"check-cpu.rb","skip_arguments":"true"},{"exec":"check-disk-usage.rb","skip_arguments":"true"},{"exec":"check-head-redirect.rb","skip_arguments":"true"},{"exec":"check-kube-apiserver-available.rb","skip_arguments":"true"},{"exec":"check-kube-pods-restarting.rb","skip_arguments":"true"},{"exec":"check-kube-pods-running.rb","skip_arguments":"true"},{"exec":"check-kube-pods-runtime.rb","skip_arguments":"true"},{"exec":"check-kube-service-available.rb","skip_arguments":"true"},{"exec":"check-load.rb","skip_arguments":"true"},{"exec":"check-log-sudo.sh","skip_arguments":"true"},{"exec":"check-log.rb","skip_arguments":"true"},{"exec":"check-memcached-stats.rb","skip_arguments":"true"},{"exec":"check-memory-percent.rb","skip_arguments":"true"},{"exec":"check-mongodb-metric.rb","skip_arguments":"true"},{"exec":"check-mysql-alive.rb","skip_arguments":"true"},{"exec":"check-mysql-query-result-count.rb","skip_arguments":"true"},{"exec":"check-mysql-threads.rb","skip_arguments":"true"},{"exec":"check-nginx-status.rb","skip_arguments":"true"},{"exec":"check-oracle-alive.rb","skip_arguments":"true"},{"exec":"check-ping.rb","skip_arguments":"true"},{"exec":"check-ports.rb","skip_arguments":"true"},{"exec":"check-process.rb","skip_arguments":"true"},{"exec":"check-rabbitmq-alive.rb","skip_arguments":"true"},{"exec":"check-rabbitmq-messages.rb","skip_arguments":"true"},{"exec":"check-rabbitmq-node-usage.rb","skip_arguments":"true"},{"exec":"check-redis-info.rb","skip_arguments":"true"},{"exec":"check-redis-ping.rb","skip_arguments":"true"},{"exec":"check-snmp.rb","skip_arguments":"true"},{"exec":"check-swap-percent.rb","skip_arguments":"true"},{"exec":"check-threads-count.rb","skip_arguments":"true"},{"exec":"check_discover.rb","skip_arguments":"false"},{"exec":"cscript","args":["check_ad.vbs //nologo"],"skip_arguments":"false"},{"exec":"endpoint_discovery.rb","skip_arguments":"true"},{"exec":"running_processes.rb","skip_arguments":"false"},{"exec":"tcp_connections.rb","skip_arguments":"false"},{"exec":"file_systems.rb","skip_arguments":"false"},{"exec":"network_adapters.rb","skip_arguments":"false"},{"exec":"serial_numbers.rb","skip_arguments":"false"},{"exec":"storage_devices.rb","skip_arguments":"false"},{"exec":"metrics-apache-graphite.rb","skip_arguments":"true"},{"exec":"metrics-cpu-pcnt-usage.rb","skip_arguments":"true"},{"exec":"metrics-cpu.rb","skip_arguments":"true"},{"exec":"metrics-curl.rb","skip_arguments":"true"},{"exec":"metrics-disk-capacity.rb","skip_arguments":"true"},{"exec":"metrics-disk-usage.rb","skip_arguments":"true"},{"exec":"metrics-disk.rb","skip_arguments":"true"},{"exec":"metrics-docker-info.rb","skip_arguments":"true"},{"exec":"metrics-docker-stats.rb","skip_arguments":"true"},{"exec":"metrics-jmx.rb","skip_arguments":"true"},{"exec":"metrics-k8s.rb","skip_arguments":"true"},{"exec":"metrics-load.rb","skip_arguments":"true"},{"exec":"metrics-memcached-graphite.rb","skip_arguments":"true"},{"exec":"metrics-memcached-socket-graphite.rb","skip_arguments":"true"},{"exec":"metrics-memory-percent.rb","skip_arguments":"true"},{"exec":"metrics-memory-vmstat.rb","skip_arguments":"true"},{"exec":"metrics-memory.rb","skip_arguments":"true"},{"exec":"metrics-mongodb.rb","skip_arguments":"true"},{"exec":"metrics-mysql-graphite.rb","skip_arguments":"true"},{"exec":"metrics-mysql-processes.rb","skip_arguments":"true"},{"exec":"metrics-mysql-query-result-count.rb","skip_arguments":"true"},{"exec":"metrics-nginx.rb","skip_arguments":"true"},{"exec":"metrics-oracle.rb","skip_arguments":"true"},{"exec":"metrics-ping.rb","skip_arguments":"true"},{"exec":"metrics-process-status.rb","skip_arguments":"true"},{"exec":"metrics-query-oracle.rb","skip_arguments":"true"},{"exec":"metrics-rabbitmq-exchange.rb","skip_arguments":"true"},{"exec":"metrics-rabbitmq-overview.rb","skip_arguments":"true"},{"exec":"metrics-rabbitmq-queue.rb","skip_arguments":"true"},{"exec":"metrics-redis-graphite.rb","skip_arguments":"true"},{"exec":"metrics-snmp-bulk-sn.rb","skip_arguments":"true"},{"exec":"metrics-snmp.rb","skip_arguments":"true"},{"exec":"osqueryi","args":["--logger_min_status 1","--json","\"select network_name, last_connected, captive_portal FROM wifi_networks WHERE captive_portal=1\"","\"select * from apps\"","\"select * from etc_hosts\"","\"select * from os_version\"","\"select DISTINCT processes.name, listening_ports.port, processes.pid FROM listening_ports JOIN processes USING (pid) WHERE listening_ports.address = '0.0.0.0'\"","\"select * from logged_in_users\"","\"select * from uptime\"","\"select name, path, pid FROM processes WHERE on_disk = 0\"","\"select u.username, g.gid, g.groupname FROM users u JOIN user_groups ug USING (uid) JOIN groups g ON ug.gid = g.gid WHERE uid > 500\"","\"select pid, name, uid, resident_size from processes order by resident_size desc limit 10\"","\"select * from system_info\"","\"select * from certificates\"","\"select path, type, round((blocks_available * blocks_size *10e-10),2) as gigs_free from mounts where path='/'\"","\"select * from chrome_extensions\"","\"select name from kernel_info\""],"skip_arguments":"false"},{"exec":"read-file.rb","skip_arguments":"true"},{"exec":"rebootcount.sh","skip_arguments":"false"},{"exec":"Restart","args":["agent"],"skip_arguments":"false"},{"exec":"winchecks","skip_arguments":"true"},{"exec":"acc","args":["self-test","self-test debug","self-test verbose"],"skip_arguments":"false"}] |

## Notes

### Installing On Windows

For Windows installations, Ansible will read the MSI file's ProductCode to
search the registry to determine if the package is already installed or not.
If the package version is different then it will try to install that version.
Do note that with ACC if you are downgrading you will need to be sure to
uninstall the current version before installing the new version.

If the path is a URL, know that Ansible will download that file to a temporary
location in order to gather the metadata of the package. You can avoid this by
setting `agent_client_collector_product_code` to the actual ProductCode of
said package.

This is a list of current known ProductCodes for the version of ACC being
installed. Feel free to update the list in a PR with future versions.

| version | product_id                             |
|---------|----------------------------------------|
| 2.7.0   | {B197E891-E6EB-40B9-94C4-AB0C802503F9} |
| 2.8.2   | {FA1D07AC-4DED-4A93-A32C-34184997386F} |
| 3.0.0   | {3179BAED-D98B-43D9-AB06-9C256372F564} |

### Agent ID & API Key

ACC agent will generate its own agent-key-id for encrypting the API key; meaning
 every agent has its own unique agent-key-id. The API key is then rewritten at
 runtime in the `acc.yml` configuration file as an encrypted hash. What this
 means is that we lose idempotent execution on the configuration file. To get
 around this you can specify the same agent-key-id and encrypted api-key across
 all your agents. The only way to do this initially is to install the agent
 somewhere with the API key, then collect the two variables; I suggest putting
 this information in a vault of some kind.

What does this mean from a security standpoint? All agents using the same
api-key will be configured to decrypt it using the same hash value provided.
At the end of the day, you're most likely not using one api-key per agent,
so in my mind the risk is fairly low in doing this. Should the api-key be
compromised, the actor would essentially be able to mimic any agent
regardless of which agent-key-id was used to gain that access.

However, by using this method of sharing the agent-key-id across all your agents
, you are accepting the whatever risk comes with that.

### Uninstalling Agents

When the agent is first installed, it will generate an agent id in order to
uniquely present itself to ServiceNow. The agent id is stored in a binary file
on the running system's filesystem. When registering itself to ServiceNow
for the first time, a record is created in the `sn_agent_cmdb_ci_agent` table
storing this id in the `agent_id` field.

When doing upgrades, configuration changes, etc is done to the agent, ServiceNow
will always know that the running agent is matched to this record. The issue
comes when uninstalling the agent as this binary file is then removed from the
filesystem. So, if you are downgrading and trying to uninstall the agent, do
know that a new record will be created in the `sn_agent_cmdb_ci_agent` table.

I have been able to successfully read the binary file to get the agent id (no
other information is stored in the file... for now), and rewrite that file
after a reinstall in order to maintain the same system record in ServiceNow.
Currently this module does not do this.

## Examples

```yaml
- name: Install and configure ACC agent
  collections:
    - irunasroot.servicenow
  hosts: servers
  vars:
    agent_client_collector_version: "2.8.2"
    agent_client_collector_config_backend_url:
      - "wss://mid1.irunasroot.com:8800/ws/events"
    agent_client_collector_config_api_key: "encrypted:<encrypted key>"
    agent_client_collector_config_agent_key_id: "<agent key id>"
  roles:
    - name: "irunasroot.servicenow.agent_client_collector"


- name: Install with added values to check-allow-list.json
  collections:
    - irunasroot.servicenow
  hosts: servers
  vars:
    agent_client_collector_version: "2.8.2"
    agent_client_collector_config_backend_url:
      - "wss://mid1.irunasroot.com:8800/ws/events"
    agent_client_collector_config_api_key: "encrypted:<encrypted key>"
    agent_client_collector_config_agent_key_id: "<agent key id>"
    my_check_allow_list:
      - exec: myscript1.rb
        skip_arguments: true
      - exec: myscript2.rb
        skip_arguments: false
        args:
          - "--safe-arg1"
          - "--safe-arg2 myvalue"
    agent_client_collector_check_allow_list: "{{ agent_client_collector_check_allow_list + my_check_allow_list }}"
  roles:
    - name: "irunasroot.servicenow.agent_client_collector"


- name: Install and configure ACC agent on my Windows servers using psrp
  collections:
    - irunasroot.servicenow
  hosts: windows_servers
    agent_client_collector_version: "2.8.2"
    agent_client_collector_product_code: "{FA1D07AC-4DED-4A93-A32C-34184997386F}"
    agent_client_collector_download_path: "\\\\mydomain.local\\SYSVOL\\mydomain.local\\packages\\agent-client-collector-2.8.2-windows-x64.msi"
    agent_client_collector_config_backend_url:
      - "wss://mid1.irunasroot.com:8800/ws/events"
    agent_client_collector_config_api_key: "encrypted:<encrypted key>"
    agent_client_collector_config_agent_key_id: "<agent key id>"
    ansible_become_method: runas
    ansible_connection: psrp
    ansible_psrp_auth: kerberos
    ansible_psrp_cert_validation: ignore
  roles:
    - name: "irunasroot.servicenow.agent_client_collector"
```
