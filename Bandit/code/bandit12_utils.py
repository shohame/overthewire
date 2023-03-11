
def hexdump_to_binary(hexdump_file, output_file):

    bytes_ = b''
    with open(hexdump_file, 'r') as f:
        for line in f:
            hexdump = line[10:49]
            bytes_ += bytes.fromhex(hexdump)


    with open(output_file, 'wb') as f:
        # write the binary data to the output file
        f.write(bytes_)


def determine_file_type(filepath):
    with open(filepath, 'rb') as f:
        # read the first few bytes of the file
        header = f.read(32)

        # determine the file type based on the magic number
        if header.startswith(b'\x89PNG\r\n\x1a\n'):
            return 'PNG'
        elif header.startswith(b'\xff\xd8\xff\xe0\x00\x10JFIF'):
            return 'JPEG'
        elif header.startswith(b'\x47\x49\x46\x38\x37\x61') or header.startswith(b'\x47\x49\x46\x38\x39\x61'):
            return 'GIF'
        elif header.startswith(b'\x42\x4d'):
            return 'BMP'
        elif header.startswith(b'\x52\x49\x46\x46'):
            return 'RIFF'
        elif header.startswith(b'\x00\x00\x01\x00'):
            return 'ICO'
        elif header.startswith(b'\x1f\x8b\x08'):
            return 'GZIP'
        elif header.startswith(b'\x1f\x9d'):
            return 'COMPRESS'
        elif header.startswith(b'\x1f\x0b'):
            return 'TAR'
        elif header.startswith(b'\x7fELF'):
            return 'ELF'
        elif header.startswith(b'\xca\xfe\xba\xbe'):
            return 'MACHO'
        elif header.startswith(b'\xce\xfa\xed\xfe') or header.startswith(b'\xcf\xfa\xed\xfe'):
            return 'MACHO'
        elif header.startswith(b'\x7fCGC'):
            return 'CGC'
        elif header.startswith(b'\x42\x5a\x68'):
            return 'BZIP2'
        else:
            return 'Unknown'
