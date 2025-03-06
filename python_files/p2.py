import requests

url = "https://voicerss-text-to-speech.p.rapidapi.com/"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"src\"\r\n\r\nHello, world!\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"hl\"\r\n\r\nen-us\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"r\"\r\n\r\n0\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"c\"\r\n\r\nmp3\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"f\"\r\n\r\n8khz_8bit_mono\r\n-----011000010111000001101001--\r\n\r\n"
headers = {
	"x-rapidapi-key": "42ca5d8100msh5a934e581601320p1982c9jsne1698e981c88",
	"x-rapidapi-host": "voicerss-text-to-speech.p.rapidapi.com",
	"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())