# Scripts

## generatePolygon.py

### Usage

```bash
generatePolygon.py <latitude> <longitude> [FieldName]
```

_Mandatory args:_ **latitude**, **longitude**

_Optional arg:_ **FieldName**; if not provided, will be constructed using lat/lon

### Example

```bash
python generatePolygon -101.162714000941 41.0464218322353 field-A
```

### Relevant details

1. For each lat/lon, the script would generate a unique file containing the polygon - meaning it'd be interpreted as an independent field containing 1 subfield
2. There is an option to provide a field/file name as input besides the lat/lon - if it's not provided, the code uses the lat/lon to generate a unique hash and uses that as the field/file name.
3. Radius is preset to 1000 meters and number of points in the polygon is preset to 20 - either/both can be changed in code.

### Library dependencies

```bash
pip install geog
pip install shapely
```
