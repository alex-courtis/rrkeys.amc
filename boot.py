NO_HIDE = True

import supervisor

import board
import digitalio
import storage
import usb_cdc
import usb_hid

supervisor.set_next_stack_limit(4096 + 4096)

# Use most furthest or nearest key to enter usb storage mode
col1 = digitalio.DigitalInOut(board.GP15)
row1 = digitalio.DigitalInOut(board.GP21)
col2 = digitalio.DigitalInOut(board.GP12)
row2 = digitalio.DigitalInOut(board.GP16)
col1.switch_to_output(value=True)
row1.switch_to_input(pull=digitalio.Pull.DOWN)
col2.switch_to_output(value=True)
row2.switch_to_input(pull=digitalio.Pull.DOWN)

if not NO_HIDE:
    if not (row1.value or row2.value):
        storage.disable_usb_drive()
        usb_cdc.disable()
        usb_hid.enable(boot_device=1)

row1.deinit()
col1.deinit()
row2.deinit()
col2.deinit()
