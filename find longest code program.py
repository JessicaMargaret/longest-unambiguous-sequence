def longeststrand(string):
    acceptable = "A", "a", "G", "g", "C", "c", "T", "t"
    longestlist = []
    placeholder = []
    for letter in string:
        temp = len(placeholder)
        longest = len(longestlist)
        if letter in acceptable:
            placeholder.append(letter)
            if temp >= longest:
                longestlist.clear()
                longestlist = placeholder[:]
        else:
            placeholder.clear()
    return "".join(longestlist)
            
JM2 = "WAWtKgACAAWKgGCGAAAGCCtgAtCCAGCCAtgCCGCGtgtKtTAAGAAgGtCttCgGAWtKtaAAgCACWWWAAKWWKggAggAAgggCAWWAACCWAAWACKWWAKWtttWttACKttACCKACAKAAWAADCACCKKCWAACWCWtWtCCAKCAKCCKCKgWAAWACAKAKKKtKCAAgCBttAAWCBgAAWWACtKKKCKWAAADCBCBCBWaKKWtKtWCBWWAADWWtKAWtttAAAWCCCCBggCWCAACCWtKKAACWtCAWWCAAAACWtWCKAgCWADAKWAWtKWAKAgggtKKtKgAAWWWcCWWtWWAgCSKWWAAAWWCYWAWAWAWAWKAAKKAAC"