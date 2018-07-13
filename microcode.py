import const

microcode = {
    # NOOP
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: 0x0000,
    0x0003: 0x0000,

    # LDA
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['RO'] | const.SIGNALS['MI'],
    0x0003: const.SIGNALS['RO'] | const.SIGNALS['AI'],

    # STA
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['RO'] | const.SIGNALS['MI'],
    0x0003: const.SIGNALS['AO'] | const.SIGNALS['RI'],

    # LDAI
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['RO'] | const.SIGNALS['AI'],
    0x0003: 0x0000,

    # LDB
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['RO'] | const.SIGNALS['MI'],
    0x0003: const.SIGNALS['RO'] | const.SIGNALS['BI'],

    # STB
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['RO'] | const.SIGNALS['MI'],
    0x0003: const.SIGNALS['BO'] | const.SIGNALS['RI'],

    # LDBI
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['RO'] | const.SIGNALS['BI'],
    0x0003: 0x0000,

    # STE
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['RO'] | const.SIGNALS['MI'],
    0x0003: const.SIGNALS['EO'] | const.SIGNALS['RI'],

    # ADD
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['EO'] | const.SIGNALS['AI'],
    0x0003: 0x0000,

    # SUB
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['SU'] | const.SIGNALS['EO'] | const.SIGNALS['AI'],
    0x0003: 0x0000,

#     'HLT' - 0x0800
#     'MI'  - 0x4000
#     'RI'  - 0x2000
#     'RO'  - 0x1000
#     'AI'  - 0x0800
#     'AO'  - 0x0400
#     'BI'  - 0x0200
#     'BO'  - 0x0100
#     'EO'  - 0x0080
#     'SU'  - 0x0040
#     'OI'  - 0x0020
#     'CE'  - 0x0010
#     'CO'  - 0x0008
#     'J'   - 0x0004
#     'II'  - 0x0002
#     'RN'  - 0x0001

    # OUT
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['RO'] | const.SIGNALS['MI'],
    0x0003: const.SIGNALS['RO'] | const.SIGNALS['OI'],

    # OUTI
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['RO'] | const.SIGNALS['OI'],
    0x0003: 0x0000,

    # OUTA
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['AO'] | const.SIGNALS['OI'],
    0x0003: 0x0000,

    # OUTB
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['BO'] | const.SIGNALS['OI'],
    0x0003: 0x0000,

    # HLT
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['RO'] | const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0002: const.SIGNALS['HLT'],
    0x0003: 0x0000,
}
