import qrcode
import sys

sys.stdout.reconfigure(encoding="utf-8")

def generate(data):
    """Generate QR code using ASCII full block characters"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Get the QR code matrix
    qr_matrix = qr.modules
    
    # Convert to ASCII using full blocks
    ascii_qr = ""
    for row in qr_matrix:
        for cell in row:
            # Black = full block (█), White = space
            ascii_qr += "█" if cell else " "
        ascii_qr += "\n"
    
    # Print to console
    return ascii_qr
