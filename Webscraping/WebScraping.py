# Check weather website can gave any response or not
# For this we are using requests library

# Before starting it check weather it is installed or not.
# To install request on terminal type pip install requests.



# import requests
import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Website is working"
        else:
            return f"Website is not working (Status code: {response.status_code})"
    except requests.ConnectionError:
        return "Website is not working (Connection error)"
    
    # Whenever there is any exception is raised the code returns the following.
    
    except requests.Timeout:
        return "Website is not working (Request timed out)"
    except requests.RequestException:
        return "Website is not working (Request exception)"

# Example usage:
website_url = "https://www.example.com" # Gave the url of website.
result = check_website(website_url)
print(result)



# we can also add looping to the above code to and add them in a list.
# To see a workign of large number of websites.