def parse_request(valid_auth_tokens, requests):
    result = []

    for req in requests:
        method, url = req
        params = {}
        valid_request = True

        # Extract parameters from URL
        url_params = url.split('?')[1].split('&')
        for param in url_params:
            key, value = param.split('=')
            # Remove leading/trailing spaces from key and value
            key = key.strip()
            value = value.strip()
            params[key] = value

        # Check authentication token
        auth_token = params.get('token')
        if auth_token not in valid_auth_tokens:
            result.append("INVALID")
            valid_request = False

        # Check CSRF token for POST requests
        if method == "POST":
            csrf_token = params.get('csrf')
            if not csrf_token or not csrf_token.isalnum() or len(csrf_token) < 8:
                result.append("INVALID")
                valid_request = False

        # Construct parameter string for valid request
        if valid_request:
            param_string = ','.join([f"{key},{value}" for key, value in params.items() if key != 'token'])
            result.append(f"VALID,{param_string}")

    return result


# New valid authentication tokens
valid_auth_tokens = ["et51u8i9p1q7", "r5b019lmlp09"]

# Example requests
requests = [
    ["GET", "https://example.com/?token=et51u8i9p1q7&id=2e3rt&name=alex"],
    ["POST", "https://example.com/?token=r5b019lmlp09&csrf=a&name=chris"]
]

result = parse_request(valid_auth_tokens, requests)
for res in result:
    print(res)
