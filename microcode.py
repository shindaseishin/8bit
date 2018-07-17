import const

microcode = {
    # NOOP
    0x0000: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0001: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'] | const.SIGNALS['PSS'],
    0x0002: 0x0000,
    0x0003: 0x0000,

    # LDA
    0x0100: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0101: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0102: const.SIGNALS['ROA'] | const.SIGNALS['MI'],
    0x0103: const.SIGNALS['ROD'] | const.SIGNALS['AI'],

    # STA
    0x0200: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0201: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0202: const.SIGNALS['ROA'] | const.SIGNALS['MI'],
    0x0203: const.SIGNALS['AO'] | const.SIGNALS['RI'],

    # LDAI
    0x0300: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0301: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0302: const.SIGNALS['ROD'] | const.SIGNALS['AI'] | const.SIGNALS['PSS'],
    0x0303: 0x0000,

    # LDAE
    0x0400: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0401: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0402: const.SIGNALS['EO'] | const.SIGNALS['AI'] | const.SIGNALS['PSS'],
    0x0403: 0x0000,

    # LDB
    0x0500: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0501: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0502: const.SIGNALS['ROA'] | const.SIGNALS['MI'],
    0x0503: const.SIGNALS['ROD'] | const.SIGNALS['BI'],

    # STB
    0x0600: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0601: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0602: const.SIGNALS['ROA'] | const.SIGNALS['MI'],
    0x0603: const.SIGNALS['BO'] | const.SIGNALS['RI'],

    # LDBI
    0x0700: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0701: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0702: const.SIGNALS['ROD'] | const.SIGNALS['BI'] | const.SIGNALS['PSS'],
    0x0703: 0x0000,

    # LDBE
    0x0800: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0801: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0802: const.SIGNALS['EO'] | const.SIGNALS['BI'] | const.SIGNALS['PSS'],
    0x0803: 0x0000,

    # STE
    0x0900: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0901: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0902: const.SIGNALS['ROA'] | const.SIGNALS['MI'],
    0x0903: const.SIGNALS['EO'] | const.SIGNALS['RI'],

    # ADD
    0x0A00: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0A01: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0A02: const.SIGNALS['EE'] | const.SIGNALS['PSS'],
    0x0A03: 0x0000,

    # SUB
    0x0B00: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0B01: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0B02: const.SIGNALS['SU'] | const.SIGNALS['EE'] | const.SIGNALS['PSS'],
    0x0B03: 0x0000,

    # JMP
    0x0C00: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0C01: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0C02: const.SIGNALS['J']  | const.SIGNALS['ROA'] | const.SIGNALS['PSS'],
    0x0C03: 0x0000,

    #JMPC
    0x0D00: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0D01: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0D02: const.SIGNALS['SU'] | const.SIGNALS['EE'],
    0x0D03: const.SIGNALS['JZ'] | const.SIGNALS['ROA'],

    #JMPO
    0x0E00: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x0E01: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x0E02: const.SIGNALS['JO'] | const.SIGNALS['ROA'] | const.SIGNALS['PSS'],
    0x0E03: 0x0000,

    # OUT
    0x1B00: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x1B01: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x1B02: const.SIGNALS['ROA'] | const.SIGNALS['MI'],
    0x1B03: const.SIGNALS['ROD'] | const.SIGNALS['OI'],

    # OUTI
    0x1C00: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x1C01: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x1C02: const.SIGNALS['ROD'] | const.SIGNALS['OI'] | const.SIGNALS['PSS'],
    0x1C03: 0x0000,

    # OUTA
    0x1D00: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x1D01: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x1D02: const.SIGNALS['AO'] | const.SIGNALS['OI'] | const.SIGNALS['PSS'],
    0x1D03: 0x0000,

    # OUTB
    0x1E00: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x1E01: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x1E02: const.SIGNALS['BO'] | const.SIGNALS['OI'] | const.SIGNALS['PSS'],
    0x1E03: 0x0000,

    # HLT
    0x1F00: const.SIGNALS['MI'] | const.SIGNALS['CO'],
    0x1F01: const.SIGNALS['CE'] | const.SIGNALS['II'] | const.SIGNALS['RN'],
    0x1F02: const.SIGNALS['HLT'] | const.SIGNALS['PSS'],
    0x1F03: 0x0000,
}
