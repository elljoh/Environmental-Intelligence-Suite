# API Auth Tokens

In order to programatically access Weather Operations Center (WOC) APIs for asset import and registration of custom geospatial queries, the user needs to generate a Bearer access token using their WOC API key.

Shell example with curl:

```bash
curl --request POST --url https://"token provider URL"/Auth/GetBearerForClient --header 'Content-Type: application/json' --header 'cache-control: no-cache' --data '{apiKey:"xxxxxxxxxxxxxx", clientId:"ibm-agro-api"}'
```

Example output:
```{"access_token":"ey ..... 6Mg","expires_in":600,"token_type":"Bearer"}```

IBM Tech Sales shall provide customers with the correct token provider URL and WOC API key to be able retrieve tokens for their organization.
