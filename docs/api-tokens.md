# API Auth Tokens

In order to access the APIs the user needs to generate a Bearer access token.

Shell example with curl:

```bash
curl --request POST --url https://"token provider URL"/Auth/GetBearerForClient --header 'Content-Type: application/json' --header 'cache-control: no-cache' --data '{apiKey:"xxxxxxxxxxxxxx", clientId:"ibm-agro-api"}'
```

Example output:
```{"access_token":"ey ..... 6Mg","expires_in":600,"token_type":"Bearer"}```

IBM Tech Sales shall provide customers with the correct URL and API key to be able retrieve tokens for their organization.
