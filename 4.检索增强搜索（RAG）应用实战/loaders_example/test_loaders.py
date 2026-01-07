from langchain_community.document_loaders import BiliBiliLoader

loader = BiliBiliLoader(
    [
        "https://www.bilibili.com/video/BV1MUmCBxECT/?spm_id_from=333.337.search-card.all.click&vd_source=99818a3df596c69ba400b78354d691da",
    ],
    sessdata = r"e62e1570%2C1771299952%2Cfdecb%2A81CjCRpQ4SDzcyUh3HwdvDC5OtxlsfY8v9Gi-txirrJ7IgQkDQwL7uwZxdAe8scIOI9H0SVmRSbGlvbEpUMGxXR2lqekEyVFoybEYwZE5hZ19rRTdpNmd0N2pMeV9BLUNSWllMV055eEUwZk9udmFmVUpWNTJ0VWJPVkdCb3VfZ0pJZ2hQczNyZl9RIIEC",
    buvid3 = r"6F928973-22A2-7AA9-3E89-7B9995C70A7759804infoc",
    bili_jct = r"5bb8dda27dac87380a28f60d19efdf28"
)

docs = loader.load()
print(docs)