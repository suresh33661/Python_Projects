import pytest
from WebScraping import check_website

# Test case for a working website
def test_working_website():
    website_url = "https://www.example.com"
    result = check_website(website_url)
    assert result == "Website is working"

# Test case for a non-working website (status code 404)
def test_non_working_website():
    website_url = "https://www.example.com/nonexistent"
    result = check_website(website_url)
    assert result == "Website is not working (Status code: 404)"

# Add more test cases for other scenarios as needed

if __name__ == "__main__":
    pytest.main()
