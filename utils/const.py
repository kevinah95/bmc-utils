TABLE_GENETIC_CODE_FULL = {
    'UUU': 'Fenilalanina', 'UUC': 'Fenilalanina', 'UUA': 'Leucina', 'UUG': 'Leucina', 'CUU': 'Leucina',
    'CUC': 'Leucina', 'CUA': 'Leucina', 'CUG': 'Leucina', 'AUU': 'Isoleucina', 'AUC': 'Isoleucina',
    'AUA': 'Isoleucina', 'AUG': 'Metionina', 'GUU': 'Valina', 'GUC': 'Valina', 'GUA': 'Valina',
    'GUG': 'Valina', 'UCU': 'Serina', 'UCC': 'Serina', 'UCA': 'Serina', 'UCG': 'Serina',
    'CCU': 'Prolina', 'CCC': 'Prolina', 'CCA': 'Prolina', 'CCG': 'Prolina', 'ACU': 'Treonina',
    'ACC': 'Treonina', 'ACA': 'Treonina', 'ACG': 'Treonina', 'GCU': 'Alanina', 'GCC': 'Alanina',
    'GCA': 'Alanina', 'GCG': 'Alanina', 'UAU': 'Tirosina', 'UAC': 'Tirosina', 'UAA': '------',
    'UAG': '------', 'CAU': 'Histidina', 'CAC': 'Histidina', 'CAA': 'Glutamina', 'CAG': 'Glutamina',
    'AAU': 'Asparagina', 'AAC': 'Asparagina', 'AAA': 'Lisina', 'AAG': 'Lisina', 'GAU': 'AcidAspartico',
    'GAC': 'AcidAspartico', 'GAA': 'AcidGlutamico', 'GAG': 'AcidGlutamico', 'UGU': 'Cisteina', 'UGC': 'Cisteina',
    'UGA': '------', 'UGG': 'Triptofano', 'CGU': 'Arginina', 'CGC': 'Arginina', 'CGA': 'Arginina',
    'CGG': 'Arginina', 'AGU': 'Serina', 'AGC': 'Serina', 'AGA': 'Arginina', 'AGG': 'Arginina',
    'GGU': 'Glicina', 'GGC': 'Glicina', 'GGA': 'Glicina', 'GGG': 'Glicina'
}

# 3-letter aa dictionary
TABLE_GENETIC_CODE_THREE_LETTERS = {
    #             Second Base
    #    U              C             A             G
    # U
    'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',  # UxU
    'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',  # UxC
    'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',  # UxA
    'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp',  # UxG
    # C
    'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',  # CxU
    'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',  # CxC
    'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',  # CxA
    'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',  # CxG
    # A
    'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',  # AxU
    'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',  # AxC
    'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',  # AxA
    'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',  # AxG
    # G
    'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',  # GxU
    'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',  # GxC
    'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',  # GxA
    'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'  # GxG
}

# single-letter aa dictionary
TABLE_GENETIC_CODE_SINGLE_LETTER = {'Cys': 'C', 'Asp': 'D', 'Ser': 'S', 'Gln': 'Q', 'Lys': 'K', 'Trp': 'W', 'Thr': 'T', 'Asn': 'N', 'Pro': 'P', 'Phe': 'F',
                     'Ala': 'A', 'Gly': 'G', 'Ile': 'I', 'Leu': 'L', 'His': 'H', 'Arg': 'R', 'Met': 'M', 'Val': 'V', 'Glu': 'E', 'Tyr': 'Y', '---': '*'}
