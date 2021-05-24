## IBM Environmental Intelligence Suite extension for Custom Geospatial Queries </h1>

IBM Environmental Intelligence Suite combines the power of geospatial analytics, alerts and dashboards into a single, modernized user experience. Release 1.0 empowers our customers with basic support for visualizing results of a geospatial query and share their findings operationally through dashboard interactive map.

__Action__: Contact your IBM representative to get your IBM Environmental Intelligence Suite `API_KEY` and `username | password`.

## Perform Data Exploration and Experimentation using IBM Environmental Intelligence Suite - Geospatial Analytics Component

 ### Identify Datasets

 Log into IBM Environmental Intelligence Suite (weatheroperationscenter.ibm.com), navigate to Geospatial Analytics using left-nav menu and use Data Explorer to search for relevant datasets.

 ### Areas of Interest

 Draw a point/polygon, or look for an area of interest (like "Austin Texas" or "New South Wales"). Select relevant layers, etc and perform experimental queries.

 ![alt text](https://github.com/IBM/Weather-Operations-Center/blob/master/docs/resources/woc-geospatial-03.png?raw=true)

 ### Data Science Experiments

 Optionally, create a new project in a data science environment (e.g, IBM Watson Studio), import your business assets and optionally, use one (or more) of the experimental queries from prior step to bring in data from PAIRS into your notebook. Do further experiments, feature selection, model construction/training, execution and persist output of model execution into a PAIRS data layer. Tutorials on how to construct and use geospatial queries are located here - https://pairs.res.ibm.com/tutorial/tutorials/api/index.html
 
### Visualization of data from EIS Geospatial Component (PAIRS)
 
 Once you have identified a specific layer in PAIRS that has the data for the time-interval of your interest, form a query similar to the example shown below, specifying your own `spatial:coordinates`, `temporal:intervals` and `layers:id`.  Subsequently, proceed to Day 0 below to operationalize it for viewing within Dashboard Visualization component of WOC.

<b>Example geospatial `QUERY_PAYLOAD` that is ready to be operationalized </b>:

``` shell
{
 "spatial": {
    "type":"square",
    "aoi":null,
    "coordinates":[38,-122,39,-121]
  },
 "temporal":{
   "intervals":[{
     "start":"2020-08-01",
     "end":"2020-08-31"
     }]
  },
 "layers":[{
    "id":"51",
    "type":"raster"
  }]
 }
```

## Day 0: Register Analytics for visualization in Environmental Intelligence Suite - Dashboard Visualization Component

### Generate JWT token

Get an access token:
1. Follow the steps in [Geospatial Analytics API - Obtaining an Access Token](./geospatial-api.md#obtaining-an-access-token) to obtain the token indicated by `<ACCESS_JWT>`
2. Copy the value corresponding to `<ACCESS_JWT>` from the step above to use in the Import API call below.

### Registration Part # 1 - Platform metadata

<a id="user-content-access-jwt-ex1" href="#access-jwt-ex1"></a><b>Substitute `ACCESS_JWT`, your `QUERY_PAYLOAD` and `ANALYTICS_NAME` below - and make the curl request in a terminal window : </b>:

``` shell
curl -X POST "https://foundation.agtech.ibm.com/v2/layer/analytics/metadata" \
  -H "accept: application/json" \
  -H "Authorization: Bearer <ACCESS_JWT>" \
  -H "Content-Type: application/json; charset=UTF-8" \
  -d "{\"pairsPayload\":\"<QUERY_PAYLOAD>\",\"analyticsName\":\"<ANALYTICS_NAME>\"}"
```

<b>Example Response</b>:

``` json
[
  {
    "analyticsUuid": "1f2d5a9e-39c5-4ca4-bebc-14ac43646960",
    "layerId": "51",
    "baseComputationId": "1607533200_04490762"
  }
]
```

### Registration Part # 2 - Visualization metadata


 Before making the sample request below, modify the <b>`id`</b> to be something unique, set the desired <b>`displayName`</b> and substitute the correct <b>`dataAttributes:uuid`</b> using the `analyticsUuid` value from the response above. <a id="user-content-access-jwt-ex2" href="#access-jwt-ex2"></a>Also, substitute ACCESS_JWT

 Adjust `styleProperties:palette` and `unit` as appropriate. Contact your IBM representative or Expert Labs to discuss adjusting additional properties relevant to your specific geospatial analytics use-case.


``` shell
curl --location --request PUT 'https://api.wsitrader.com/api/v1/IMAP/put-layer-config-block' \
--header 'Authorization: Bearer <ACCESS_JWT>' \
--header 'Content-Type: application/json' \
--data '{"VIEWERSHIP_ROLE" : "ALL", "CONFIG_BLOCK": {
    "id": "customQuery-staging-test01",
    "modelRegistryId": null,
    "displayName": "Staging Test - Custom Query 01",
    "provider": null,
    "layerType": "grid",
    "isSelected": false,
    "isActive": false,
    "enableValidity": false,
    "lastUpdatedUtc": null,
    "coverageArea": "Custom",
    "dataAttributes": {
      "url": "https://foundation.agtech.ibm.com/v2",
      "uuid": "1f2d5a9e-39c5-4ca4-bebc-14ac43646960"
    },
    "menuIconUrl": null,
    "legendUrl": "",
    "styleProperties": {
      "palette": {
        "COLOR_STEPS": [
          { "step": -1, "rgba": [ 0, 0, 8, 255 ] },
          { "step": 0, "rgba": [ 11, 0, 251, 255 ] },
          { "step": .2, "rgba": [ 236, 0, 34, 255 ] },
          { "step": .4, "rgba": [ 250, 93, 7, 255 ] },
          { "step": .6, "rgba": [ 250, 249, 0, 255 ] },
          { "step": .8, "rgba": [ 0, 239, 0, 255 ] },
          { "step": 1, "rgba": [ 1, 49, 1, 255 ] }
        ]
      },
      "unit": "C",
      "isInterpolated": true,
      "extendMinimumColor": false,
      "extendMaximumColor": true,
      "invalidDataValue": -9999
    }
  }}'
```

<b>Example response</b>:

`Response: 200
Block Added.`






## Navigate to IBM Environmental Intelligence Suite - Dashboard Visualization 

1. Login to IBM Environmental Intelligence Suite with your username and password by launching http://weatheroperationscenter.ibm.com - and navigate to Dashboard Visualization -> Interactive Map

![alt text](https://github.com/IBM/Weather-Operations-Center/blob/master/docs/resources/woc-maximo01.png?raw=true)


2. Click on Map Layers and Overlays:

![alt text](https://github.com/IBM/Weather-Operations-Center/blob/master/docs/resources/woc-maximo02.png?raw=true)


3. Select the Custom Layer under "Custom" tab in Map Layers and Overlays:

![alt text](https://github.com/IBM/Weather-Operations-Center/blob/master/docs/resources/woc-geospatial-04.png?raw=true)


4. Visualize and interact with the query results:

![alt text](https://github.com/IBM/Weather-Operations-Center/blob/master/docs/resources/woc-geospatial-07.png?raw=true)


## Day 1 and beyond


### For a subsequent query run, the query temporal interval could change (for instance to 2020-09-01 to 2020-09-30)


<b>Call to</b>:

``` shell
curl --location --request POST 'https://pairs.res.ibm.com/v2/query' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <ACCESS_JWT>' \
--data '{
    "spatial": {
        "type": "square",
        "coordinates": [
            38,-122,
            39,-121
        ]
    },
    "temporal": {
        "intervals": [
            {
                "start": "2020-09-01",
                "end": "2020-09-30"
            }
        ]
    },
    "layers": [
        {
            "id": "51",
            "type": "raster"
        }
    ]
}'
```

<b>Example Response</b>:

``` json
{
    "id": "1607533200_04577287"
}
```

### Merge the new job with original baseComputationId from Day 0 - Registration Part # 1 above

<a id="user-content-access-jwt-ex3" href="#access-jwt-ex3"></a><b>Merge Jobs</b>:

``` shell
curl --location --request PUT 'https://pairs.res.ibm.com/v2/queryjobs/1607533200_04490762/merge/1607533200_04577287' \
--header 'Authorization: Bearer <ACCESS_JWT>'
```

As a consequence of the above operation, the output in Dashboard Visualization component would reflect computation from Sept 2020 (Day 1) rather than the original one from Aug 2020 (Day 0).

Navigate to Environmental Intelligence Suite and verify that the query results reflect computational change due to temporal movement from Day 0 to Day 1.
