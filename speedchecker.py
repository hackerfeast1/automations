import speedtest

st = speedtest.Speedtest()

ds_bps = st.download()
ds_mbps = ds_bps/(1024 * 1024)

print("Download speed:", ds_mbps)

us_mbps = st.upload()/(1024**2)

print("Upload speed:", us_mbps)

st.get_servers([])
print("Ping:", st.results.ping,"ms")
