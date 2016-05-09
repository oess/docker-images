Basic setup required for others to use OE Toolkits. Can be used as a 
base image for other images requiring OE Tookits.
 
To pass the license, when running your images add this: 
`docker run ... -v /tmp/oe_license.txt:/tmp/oe_license.txt:ro ...`