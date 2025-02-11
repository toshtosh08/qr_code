import qrcode

# Tire information
tire_data = {
    "serial_number": "TYRE123456789",
    "manufacturing_date": "2025-02-11",
    "batch_number": "BATCH001",
    "brand": "ToshTyres"
}

# Convert data to a string
data_string = "\n".join([f"{key}: {value}" for key, value in tire_data.items()])

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data_string)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("tire_qr_code.png")
print("QR code generated and saved as 'tire_qr_code.png'.")