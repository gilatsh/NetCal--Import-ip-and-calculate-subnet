import ipaddress

def calculate_subnet(ip_address, subnet_mask):
    # Parse the IP address and subnet mask
    network = ipaddress.IPv4Network(f'{ip_address}/{subnet_mask}', strict=False)

    # Network details
    network_address = network.network_address
    broadcast_address = network.broadcast_address

    # Calculate usable hosts
    num_ip_addresses = len(list(network.hosts()))
    first_ip = network_address + 1
    last_ip = broadcast_address - 1

    # Output results
    print(f"Network Address: {network_address}")
    print(f"Broadcast Address: {broadcast_address}")
    print(f"Number of Usable IP Addresses: {num_ip_addresses}")
    print(f"First Usable IP Address: {first_ip}")
    print(f"Last Usable IP Address: {last_ip}")

# Example usage:
ip_address = '192.168.1.0'   # IP address of the network
subnet_mask = 24             # Subnet mask in CIDR notation (e.g., /24)

calculate_subnet(ip_address, subnet_mask)
