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


# Example usage
valid_auth_tokens = ["ah37j2ha483u", "safh34ywb0p5", "ba34wyi8t902"]
requests = [
    ["GET", "https://example.com/?token=347sd6yk8iu2&name=alex"],
    ["GET", "https://example.com/?token=safh34ywb0p5&name=sam"],
    ["POST", "https://example.com/?token=safh34ywb0p5&name=alex"],
    ["POST", "https://example.com/?token=safh34ywb0p5&csrf=ak2sh32dy&name=chris"]
]

result = parse_request(valid_auth_tokens, requests)
for res in result:
    print(res)
