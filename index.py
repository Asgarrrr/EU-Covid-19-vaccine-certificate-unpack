#!/usr/bin/env python3

# —— Import libraries for base45, qrcode reader, and image processing

import sys
import os
import json
import base45
import cbor2
import zlib
import argparse

from cose.messages import CoseMessage
from pyzbar.pyzbar import decode
from PIL import Image

# —— Create a parser for the arguments
parser = argparse.ArgumentParser( )

# —— Add the arguments
parser.add_argument( "input", nargs = 1, help= "The image to read the QR code from" )
parser.add_argument( "-o", "--output", help= "The output file", action= "store_true" )

args = parser.parse_args()

if __name__ == "__main__":

    # —— Verify that the input file exists
    if not os.path.isfile( args.input[0] ):
        print( "The input file does not exist" )
        sys.exit( 1 )

    # —— Read the image
    image = Image.open( args.input[0] )

    # —— Decode the QR code
    decoded = decode( image )

    # —— Verify that the QR code was decoded
    if len( decoded ) == 0:
        print( "No QR code was decoded" )
        sys.exit( 1 )

    # —— Extract the payload from the QR code
    payload = decoded[0].data.decode( "utf-8" )

    # —— Remove first 4 bytes from the payload
    payload = payload[4:]

    # —— Decode the QR code with base45
    decoded = base45.b45decode( payload )

    # —— Decompress the data
    decompressed = zlib.decompress( decoded )

    # —— Decode COSE
    decoded = CoseMessage.decode(decompressed)

    # —— Decode CBOR
    decoded = cbor2.loads( decoded.payload )

    # —— Check if the output flag was set
    if args.output:
        # —— Write the data to a file
        with open( "output.json", "w" ) as f:
            json.dump( decoded, f, indent=4 )
        print( "The data was written to output.json" )
    else:
        # —— Print the data to the screen
        print( json.dumps( decoded, indent=4 ) )
