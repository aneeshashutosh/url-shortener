import base_62_converter

map = []

def shortenURL(url):
	# convert the url into a unique string 
	map.append(url)

def redirectToPage(url):
	index = base_62_converter.saturate(url)
	return map[index]

def main():
	# Wait for input or ask if you wanna redirect
	# Take in input
	input = "google.com"
	shortenedURL = shortenURL(input)
	redirectToPage("0")
	# add input and shortened url to the map

main()