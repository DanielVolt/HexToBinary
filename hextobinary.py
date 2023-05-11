import sys

def hex_to_binary(hex_file_path, bin_file_path):
    with open(hex_file_path, 'r') as hex_file:
        with open(bin_file_path, 'wb') as bin_file:
            for line in hex_file:
                line = line.strip()
                if line.startswith(':'):
                    byte_count = int(line[1:3], 16)
                    address = int(line[3:7], 16)
                    record_type = int(line[7:9], 16)
                    data = line[9:9 + (byte_count * 2)]
                    
                    if record_type == 0:  # Data Record
                        bin_file.write(bytes.fromhex(data))
                    elif record_type == 1:  # End of File Record
                        break
                    # Ignore other record types (e.g., Extended Linear Address)
    print(f"Conversion complete. Binary file saved at: {bin_file_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 hextobinary.py input.hex output.bin")
    else:
        hex_file_path = sys.argv[1]
        bin_file_path = sys.argv[2]
        hex_to_binary(hex_file_path, bin_file_path)
