import exifread
import argparse
from geopy.geocoders import Nominatim
from PIL import Image

def extract_image_metadata(image_path):
    try:
        # Open the image file using Pillow
        with Image.open(image_path) as img:
            # Extract image metadata using Exifread
            tags = exifread.process_file(img.fp, details=False)
        
        return tags

    except Exception as e:
        print(f"Error extracting metadata: {e}")
        return None

def get_location_from_gps(tags):
    try:
        latitude = tags.get('GPS GPSLatitude')
        longitude = tags.get('GPS GPSLongitude')

        if latitude and longitude:
            # Convert latitude and longitude to decimal degrees
            lat_degrees = latitude.values[0].num / latitude.values[0].den
            lat_minutes = latitude.values[1].num / latitude.values[1].den
            lat_seconds = latitude.values[2].num / latitude.values[2].den

            lon_degrees = longitude.values[0].num / longitude.values[0].den
            lon_minutes = longitude.values[1].num / longitude.values[1].den
            lon_seconds = longitude.values[2].num / longitude.values[2].den

            lat_decimal = lat_degrees + (lat_minutes / 60) + (lat_seconds / 3600)
            lon_decimal = lon_degrees + (lon_minutes / 60) + (lon_seconds / 3600)

            return lat_decimal, lon_decimal

        return None, None

    except Exception as e:
        print(f"Error extracting GPS coordinates: {e}")
        return None, None

def reverse_geocode(lat, lon):
    try:
        geolocator = Nominatim(user_agent="image-metadata-tool")
        location = geolocator.reverse(f"{lat}, {lon}", exactly_one=True)
        return location.address if location else "Location not found"

    except Exception as e:
        print(f"Error reverse geocoding: {e}")
        return "Location not found"

def generate_html_report(metadata, location):
    report = f"""
    <html>
    <head>
        <title>Image Metadata Report</title>
    </head>
    <body>
        <h1>Image Metadata Report</h1>
        <h2>Metadata:</h2>
        <ul>
    """
    for tag, value in metadata.items():
        report += f"<li><strong>{tag}:</strong> {value}</li>"

    report += "</ul>"
    report += f"<h2>Location:</h2><p>{location}</p>"
    report += "</body></html>"

    with open("image_metadata_report.html", "w") as report_file:
        report_file.write(report)
    
    print("Report generated as 'image_metadata_report.html'")

def main():
    parser = argparse.ArgumentParser(description="Extract image metadata from an image file.")
    parser.add_argument("image_path", help="Path to the image file")

    args = parser.parse_args()

    image_path = args.image_path
    metadata = extract_image_metadata(image_path)
    lat, lon = None, None

    if metadata:
        for tag, value in metadata.items():
            print(f"{tag}: {value}")

        lat, lon = get_location_from_gps(metadata)
        if lat is not None and lon is not None:
            location = reverse_geocode(lat, lon)
            print(f"GPS Location (Latitude, Longitude): {lat}, {lon}")
        else:
            location = "GPS coordinates not found."
            print(location)

        generate_html_report(metadata, location)
    else:
        print("Metadata extraction failed.")

if __name__ == "__main__":
    main()
