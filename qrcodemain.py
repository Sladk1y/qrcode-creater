import qrcode
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1
)
qr.add_data(f'''
Ваш текст
''')
imp = qr.make_image()
imp.save('qrcode.png')
