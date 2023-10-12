"""Kalabash compatibility matrix."""

COMPATIBILITY_MATRIX = {
    "1.8.1": {
        "kalabash-pdfcredentials": "<=1.1.0",
        "kalabash-sievefilters": "<=1.1.0",
        "kalabash-webmail": "<=1.1.5",
    },
    "1.8.2": {
        "kalabash-pdfcredentials": ">=1.1.1",
        "kalabash-sievefilters": ">=1.1.1",
        "kalabash-webmail": ">=1.2.0",
    },
    "1.8.3": {
        "kalabash-pdfcredentials": ">=1.1.1",
        "kalabash-sievefilters": ">=1.1.1",
        "kalabash-webmail": ">=1.2.0",
    },
    "1.9.0": {
        "kalabash-pdfcredentials": ">=1.1.1",
        "kalabash-sievefilters": ">=1.1.1",
        "kalabash-webmail": ">=1.2.0",
    },
    "2.1.0": {
        "kalabash-pdfcredentials": None,
        "kalabash-dmarc": None,
        "kalabash-imap-migration": None,
    },
}

EXTENSIONS_AVAILABILITY = {
    "kalabash-contacts": "1.7.4",
}
