import serial
from time import sleep
from operator import xor

MAX_GPIO = 5

IPMC_PIN_TO_GPIO_MAPPING = {
    24: 0,
    25: 2,
    26: 4,
    27: 6,
    28: 8,
    29: 10,
    30: 12,
    31: 14,
    32: 16,
    33: 18,
    35: 20,
    36: 22,
    37: 24,
    38: 26,
    39: 28,
    40: 30,
    41: 32,
    42: 34,
    43: 36,
    44: 38,
    46: 40,
    47: 42,
    48: 44,
    49: 45,
    50: 46,
    51: 47,
    52: 48,
    53: 49,
    54: 50,
    55: 51,
    63: 54,
    64: 55,
    78: 66,
    79: 68,
    81: 70,
    82: 72,
    84: 74,
    85: 76,
    87: 78,
    88: 80,
    90: 82,
    91: 84,
    92: 86,
    93: 88,
    94: 90,
    95: 92,
    96: 94,
    98: 96,
    103: 100,
    104: 102,
    105: 104,
    106: 106,
    146: 1,
    147: 3,
    148: 5,
    149: 7,
    150: 9,
    151: 11,
    152: 13,
    153: 15,
    154: 17,
    155: 19,
    157: 21,
    158: 23,
    159: 25,
    160: 27,
    161: 29,
    162: 31,
    163: 33,
    164: 35,
    165: 37,
    166: 39,
    168: 41,
    169: 43,
    183: 52,
    184: 53,
    186: 56,
    187: 57,
    188: 58,
    189: 59,
    191: 60,
    192: 61,
    194: 62,
    195: 63,
    197: 64,
    198: 65,
    200: 67,
    201: 69,
    203: 71,
    204: 73,
    206: 75,
    207: 77,
    209: 79,
    210: 81,
    212: 83,
    213: 85,
    214: 87,
    215: 89,
    216: 91,
    217: 93,
    218: 95,
    220: 97,
    221: 98,
    224: 99,
    225: 101,
    226: 103,
    227: 105,
    228: 107,
    229: 108,

    # PSGPIO
    120: 128,
    121: 129,
    242: 130,
    243: 131,
}

def gpio_absn_to_interface(absn):
    return (int(absn/32), absn - int(absn/32)*32)

IPMC_TO_CTRL_PIN_MAPPING = {
    (24, 146),
    (25, 147),
    (26, 148),
    (27, 149),
    (28, 150),
    (29, 151),
    (30, 152),
    (31, 153),
    (32, 154),
    (33, 155),
    (35, 157),
    (36, 158),
    (37, 159),
    (38, 160),
    (39, 161),
    (40, 162),
    (41, 163),
    (42, 164),
    (43, 165),
    (44, 166),
    (46, 46),
    (47, 47),
    (48, 48),
    (49, 49),
    (50, 50),
    (51, 51),
    (52, 52),
    (53, 53),
    (54, 54),
    (55, 55),
    (146, 24),
    (147, 25),
    (148, 26),
    (149, 27),
    (150, 28),
    (151, 29),
    (152, 30),
    (153, 31),
    (154, 32),
    (155, 33),
    (157, 35),
    (158, 36),
    (159, 37),
    (160, 38),
    (161, 39),
    (162, 40),
    (163, 41),
    (164, 42),
    (165, 43),
    (166, 44),
    (168, 168),
    (169, 169),
    (183, 183),
    (184, 184),
    (63, 186),
    (64, 187),
    (186, 63),
    (187, 64),
    (188, 188),
    (189, 189),
    (191, 191),
    (192, 192),
    (194, 194),
    (195, 195),
    (197, 197),
    (198, 198),
    (200, 78),
    (201, 79),
    (203, 81),
    (204, 82),
    (206, 84),
    (207, 85),
    (209, 87),
    (210, 88),
    (212, 90),
    (213, 91),
    (214, 92),
    (215, 93),
    (216, 94),
    (217, 95),
    (218, 96),
    (220, 98),
    (221, 221),
    (78, 200),
    (79, 201),
    (81, 203),
    (82, 204),
    (84, 206),
    (85, 207),
    (87, 209),
    (88, 210),
    (90, 212),
    (91, 213),
    (92, 214),
    (93, 215),
    (94, 216),
    (95, 217),
    (96, 218),
    (98, 220),

    # I2C
    (120, 120),
    (121, 121),
    (242, 242),
    (243, 243),
}

def gpio_get_direction(serial, gpio):
    t = "gpio" + str(gpio) + ".direction\r"
    serial.write(t.encode())
    serial.readline()
    r = serial.readline()
    hex = r.split("0x")[1].split("\r")[0]
    return int(hex, 16)

def gpio_set_direction(serial, gpio, value):
    t = "gpio" + str(gpio) + ".direction " + hex(value) + "\r"
    serial.write(t.encode())
    serial.readline()

def gpio_direction_bit(serial, gpio, bit, input):
    d = gpio_get_direction(serial, gpio)
    if (input == True):
        d = d | (1 << bit)
    else:
        d = d & ~(1 << bit)
    gpio_set_direction(serial, gpio, d)

def gpio_read(serial, gpio):
    t = "gpio" + str(gpio) + ".read\r"
    serial.write(t.encode())
    serial.readline()
    r = serial.readline()
    hex = r.split("0x")[1].split("\r")[0]
    return int(hex, 16)

def gpio_read_bit(serial, gpio, bit):
    t = "gpio" + str(gpio) + ".read\r"
    serial.write(t.encode())
    serial.readline()
    r = serial.readline()
    hex = r.split("0x")[1].split("\r")[0]
    return ((int(hex, 16) & (1 << bit)) != 0)

def gpio_write(serial, gpio, value):
    t = "gpio" + str(gpio) + ".write " + hex(value) + "\r"
    serial.write(t.encode())
    serial.readline()

def gpio_write_bit(serial, gpio, bit, high):
    v = gpio_read(serial, gpio)
    if (high == True):
        v = v | (1 << bit)
    else:
        v = v & ~(1 << bit)
    gpio_write(serial, gpio, v)

def default_card(target):
    for i in range(0,MAX_GPIO):
        gpio_set_direction(target, i, 0xffffffff)
        gpio_write(target, i, 0)

def gpio_to_pin(gpio, bit):
    for pin in IPMC_PIN_TO_GPIO_MAPPING:
        p = gpio_absn_to_interface(IPMC_PIN_TO_GPIO_MAPPING[pin])
        if p[0] == gpio and p[1] == bit:
            return pin

    raise NameError("GPIO pin not found!")

def gpio_range_for_direction(direction):
    r = 0;
    for i in range(0,32):
        if direction & (1 << i):
            r += 1
        else:
            break

    return r

def run_hwaddr_test(ipmc):
    print("--RUNNING HARDWARE ADDRESS TEST--")

    tests_total = 1
    tests_passed = 0
    tests_failed = 0

    summary = []

    hwaddr = gpio_read(ipmc, 5)

    if hwaddr != 0xAA:
        tests_failed += 1
        fault = "Hardware Adress is invalid (expected 0x73, read " + hex(hwaddr) + ")"
        summary.append(fault)
        print(fault)
    else:
        tests_passed += 1

    print("--END OF TESTING--")

    return [tests_total, tests_failed, summary]

def run_pinshort_test(ipmc):
    print("--RUNNING PIN SHORT DETECTION TEST--")

    tests_total = 0
    tests_passed = 0
    tests_failed = 0

    summary = []

    # Configuration
    default_card(ipmc)

    gpio_defaults = [None] * MAX_GPIO
    for i in range(0,MAX_GPIO):
        gpio_defaults[i] = gpio_read(ipmc, i)

    gpio_ranges = [None] * MAX_GPIO
    for i in range(0,MAX_GPIO):
        gpio_ranges[i] = gpio_range_for_direction(gpio_get_direction(ipmc, i))

    for pin in IPMC_PIN_TO_GPIO_MAPPING:
        failed = False
        tests_total = tests_total + 1

        target = gpio_absn_to_interface(IPMC_PIN_TO_GPIO_MAPPING[pin])

        print("## Test " + str(tests_total) + ": IPMC pin " + str(pin))

        # print("Testing IPMC pin " + str(pin) + " (GPIO " + str(gpio) + "->" + str(target) + ")")

        gpio_direction_bit(ipmc, target[0], target[1], False)

        for polarity in [False]: # Add True to list if desired to check high polarity
            # Set pin to low and check others
            gpio_write_bit(ipmc, target[0], target[1], polarity)

            gpio_readings = [None] * MAX_GPIO
            for i in range(0,MAX_GPIO):
                gpio_readings[i] = gpio_read(ipmc, i)

            # Compare
            for i in range(0,MAX_GPIO):
                # Create mask
                mask = 0xffffffff
                if i == target[0]:
                    mask &= ~(1 << target[1])

                read = gpio_readings[i] & mask
                expected = gpio_defaults[i] & mask
                xored = read ^ expected

                if (xored != 0):
                    # Short detected, detect which ones
                    failed = True
                    for k in range(0,gpio_ranges[i]):
                        b = xored & (1 << k)
                        if b != 0:
                            p = gpio_to_pin(i, k)

                            fault = "Short detected between pin " + str(pin) + " and pin " + str(p)
                            summary.append(fault)
                            print(fault)


        gpio_direction_bit(ipmc, target[0], target[1], True)

        if failed == True:
            tests_failed += 1
        else:
            tests_passed += 1

    print("--END OF TESTING--")

    return [tests_total, tests_failed, summary]

def run_continuity_test(ipmc, ctrl):
    print("--RUNNING PIN CONTINUITY TEST--")

    tests_total = 0
    tests_passed = 0
    tests_failed = 0

    summary = []

    # Configuration
    default_card(ipmc)
    default_card(ctrl)

    for pin in IPMC_TO_CTRL_PIN_MAPPING:
        tests_total = tests_total + 1

        ipmc_gpio = IPMC_PIN_TO_GPIO_MAPPING[pin[0]]
        ctrl_gpio = IPMC_PIN_TO_GPIO_MAPPING[pin[1]]

        ipmc_target = gpio_absn_to_interface(ipmc_gpio)
        ctrl_target = gpio_absn_to_interface(ctrl_gpio)

        print("## Test " + str(tests_total) + ": IPMC pin " + str(pin[0]) + " to CTRL pin " + str(pin[1]))

        # print("Testing IPMC pin " + str(pin[0]) + " (GPIO " + str(ipmc_gpio) + "->" + str(ipmc_target) + ")")
        # print("Control IPMC pin " + str(pin[1]) + " (GPIO " + str(ctrl_gpio) + "->" + str(ctrl_target) + ")")

        gpio_direction_bit(ipmc, ipmc_target[0], ipmc_target[1], False)

        # Check high value
        gpio_write_bit(ipmc, ipmc_target[0], ipmc_target[1], True)
        rhigh = gpio_read_bit(ctrl, ctrl_target[0], ctrl_target[1])
        # if (rhigh != True):
        #     print("ipmc[dir] = " + hex(gpio_get_direction(ipmc, ipmc_target[0])))
        #     print("ipmc[val] = " + hex(gpio_read(ipmc, ipmc_target[0])))
        #     print("ctrl[dir] = " + hex(gpio_get_direction(ctrl, ctrl_target[0])))
        #     print("ctrl[val] = " + hex(gpio_read(ctrl, ctrl_target[0])))
        #     print("FAILED, expected HIGH")

        # Check low value
        gpio_write_bit(ipmc, ipmc_target[0], ipmc_target[1], False)
        rlow = gpio_read_bit(ctrl, ctrl_target[0], ctrl_target[1])
        # if (rlow != False):
        #     print("ipmc[dir] = " + hex(gpio_get_direction(ipmc, ipmc_target[0])))
        #     print("ipmc[val] = " + hex(gpio_read(ipmc, ipmc_target[0])))
        #     print("ctrl[dir] = " + hex(gpio_get_direction(ctrl, ctrl_target[0])))
        #     print("ctrl[val] = " + hex(gpio_read(ctrl, ctrl_target[0])))
        #     print("FAILED, expected LOW")

        gpio_direction_bit(ipmc, ipmc_target[0], ipmc_target[1], True)

        if (rhigh != True or rlow != False):
            fault = "IPMC pin " + str(pin[0]) + " (ctrl pin " + str(pin[1]) + ") seems "
            if (rhigh == True and rlow == True):
                fault += "to be stuck at HIGH"
            elif (rhigh == False and rlow == False):
                fault += "to be stuck at LOW"
            else:
                fault += "to show reversed readings"

            summary.append(fault)

            print("IPMC pin " + str(pin[0]) + " FAILED testing, seems " + fault)
            tests_failed = tests_failed + 1
        else:
            tests_passed = tests_passed + 1

    # Put cards in a well known state
    default_card(ipmc)
    default_card(ctrl)

    print("--END OF TESTING--")

    # print("Summary: " + str(tests_passed) + "/" + str(tests_total) + " tests passed. " + str(tests_failed) + " faults detected.")
    # for fault in summary:
    #     print("Fault: " + fault)

    return [tests_total, tests_failed, summary]

def main():
    ipmc = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
    ctrl = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)

    results = [0, 0, []]

    test1 = run_hwaddr_test(ipmc)
    test2 = run_pinshort_test(ipmc)
    test3 = run_continuity_test(ipmc, ctrl)

    # Add results
    for i in [test1, test2, test3]:
        for k in range(0,3):
            results[k] += i[k]

    print("Summary: " + str(results[0] - results[1]) + "/" + str(results[0]) + " tests passed. " + str(results[1]) + " faults detected.")
    for fault in results[2]:
        print("Fault: " + fault)

    ipmc.close()
    ctrl.close()

if __name__== "__main__":
    main()
